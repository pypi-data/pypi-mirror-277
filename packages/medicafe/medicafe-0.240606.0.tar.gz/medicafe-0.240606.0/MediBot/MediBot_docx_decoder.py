from docx import Document
import re
from lxml import etree
import zipfile
from datetime import datetime
import os
import sys
from collections import OrderedDict

# Add parent directory of the project to the Python path
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_dir)

try:
    import MediLink_ConfigLoader
except ImportError:
    from MediLink import MediLink_ConfigLoader

def parse_docx(filepath):
    try:
        doc = Document(filepath)  # Open the .docx file
    except Exception as e:
        MediLink_ConfigLoader.log("Error opening document: {}".format(e))  # Log error
        return {}

    patient_data = OrderedDict()  # Initialize OrderedDict to store data
    date_of_service = extract_date_of_service(filepath)  # Extract date of service

    for table in doc.tables:  # Iterate over tables in the document
        for row in table.rows:
            cells = [cell.text.strip() for cell in row.cells]
            if len(cells) > 4 and cells[3].startswith('#'):
                try:
                    patient_id = parse_patient_id(cells[3])
                    diagnosis_code = parse_diagnosis_code(cells[4])
                    left_or_right_eye = parse_left_or_right_eye(cells[4])
                    femto_yes_or_no = parse_femto_yes_or_no(cells[4])

                    if patient_id not in patient_data:
                        patient_data[patient_id] = {}

                    if date_of_service in patient_data[patient_id]:
                        MediLink_ConfigLoader.log("Duplicate entry for patient ID {} on date {}. Skipping.".format(patient_id, date_of_service))
                    else:
                        patient_data[patient_id][date_of_service] = [diagnosis_code, left_or_right_eye, femto_yes_or_no]
                except Exception as e:
                    MediLink_ConfigLoader.log("Error processing row: {}. Error: {}".format(cells, e))
    return patient_data

# Extract and parse the date of service from the .docx file
def extract_date_of_service(docx_path):
    extract_to = "extracted_docx"
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)
    with zipfile.ZipFile(docx_path, 'r') as docx:
        docx.extractall(extract_to)
    
    file_path = find_text_in_xml(extract_to, "Surgery Schedule")
    if file_path:
        return extract_date_from_file(file_path)
    return None

# Find the target text in the extracted XML files
def find_text_in_xml(directory, target_text):
    for root_dir, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.xml'):
                file_path = os.path.join(root_dir, file)
                tree = etree.parse(file_path)
                root = tree.getroot()
                for elem in root.iter():
                    if elem.text and target_text in elem.text:
                        return file_path
    return None

# Normalize month and day abbreviations
def normalize_text(text):
    month_map = {
        'JAN': 'JANUARY', 'FEB': 'FEBRUARY', 'MAR': 'MARCH', 'APR': 'APRIL', 
        'MAY': 'MAY', 'JUN': 'JUNE', 'JUL': 'JULY', 'AUG': 'AUGUST', 
        'SEP': 'SEPTEMBER', 'OCT': 'OCTOBER', 'NOV': 'NOVEMBER', 'DEC': 'DECEMBER'
    }
    day_map = {
        'MON': 'MONDAY', 'TUE': 'TUESDAY', 'WED': 'WEDNESDAY', 'THU': 'THURSDAY', 
        'FRI': 'FRIDAY', 'SAT': 'SATURDAY', 'SUN': 'SUNDAY'
    }
    
    for abbr, full in month_map.items():
        text = re.sub(r'\b' + abbr + r'\b', full, text, flags=re.IGNORECASE)
    for abbr, full in day_map.items():
        text = re.sub(r'\b' + abbr + r'\b', full, text, flags=re.IGNORECASE)
    
    return text

# Extract and parse the date from the file
def extract_date_from_file(file_path):
    tree = etree.parse(file_path)
    root = tree.getroot()
    collected_text = []
    
    for elem in root.iter():
        if elem.tag.endswith('t') and elem.text:
            collected_text.append(elem.text.strip())

    combined_text = ' '.join(collected_text)
    combined_text = re.sub(r'(\d{3}) (\d{1})', r'\1\2', combined_text)  # Fix OCR splitting years
    combined_text = normalize_text(combined_text)  # Normalize abbreviations
    combined_text = re.sub(r',', '', combined_text)  # Remove commas if they exist

    day_week_pattern = r"(MONDAY|TUESDAY|WEDNESDAY|THURSDAY|FRIDAY|SATURDAY|SUNDAY)"
    month_day_pattern = r"(JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER) \d{1,2}"
    year_pattern = r"\d{4}"

    day_of_week = re.search(day_week_pattern, combined_text, re.IGNORECASE)
    month_day = re.search(month_day_pattern, combined_text, re.IGNORECASE)
    year_match = re.search(year_pattern, combined_text, re.IGNORECASE)

    if day_of_week and month_day and year_match:
        date_str = "{} {} {}".format(day_of_week.group(), month_day.group(), year_match.group())
        try:
            date_obj = datetime.strptime(date_str, '%A %B %d %Y')
            return date_obj.strftime('%m-%d-%Y')
        except ValueError as e:
            MediLink_ConfigLoader.log("Error converting date: {}. Error: {}".format(date_str, e))
    else:
        MediLink_ConfigLoader.log("Date components not found or incomplete in the text.")

    return None

def parse_patient_id(text):
    try:
        return text.split()[0].lstrip('#')  # Extract patient ID number (removing the '#')
    except Exception as e:
        MediLink_ConfigLoader.log("Error parsing patient ID: {}. Error: {}".format(text, e))
        return None

def parse_diagnosis_code(text):
    try:
        if '(' in text and ')' in text:  # Extract the diagnosis code before the '/'
            full_code = text[text.index('(')+1:text.index(')')]
            return full_code.split('/')[0]
        return text.split('/')[0]
    except Exception as e:
        MediLink_ConfigLoader.log("Error parsing diagnosis code: {}. Error: {}".format(text, e))
        return "Unknown"

def parse_left_or_right_eye(text):
    try:
        if 'LEFT EYE' in text.upper():
            return 'Left'
        elif 'RIGHT EYE' in text.upper():
            return 'Right'
        else:
            return 'Unknown'
    except Exception as e:
        MediLink_ConfigLoader.log("Error parsing left or right eye: {}. Error: {}".format(text, e))
        return 'Unknown'

def parse_femto_yes_or_no(text):
    try:
        if 'FEMTO' in text.upper():
            return True
        else:
            return False
    except Exception as e:
        MediLink_ConfigLoader.log("Error parsing femto yes or no: {}. Error: {}".format(text, e))
        return False

# Placeholder function call (replace 'path_to_docx' with the actual file path)
filepath = "C:\\Users\\danie\\Downloads\\SS 5-22-2024 WEDNESDAY DR AKER & DR JON.docx"
patient_data_dict = parse_docx(filepath)

# Print the resulting dictionary
import pprint
pprint.pprint(patient_data_dict)
