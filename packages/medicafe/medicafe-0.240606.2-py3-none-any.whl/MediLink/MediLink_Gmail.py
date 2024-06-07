import sys
import os
import subprocess
import webbrowser
from MediLink_ConfigLoader import log

import requests
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl

downloaded_emails_file = 'downloaded_emails.txt'
server_port = 8000

cert_file = 'server.cert'
key_file = 'server.key'

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/download':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            links = data.get('links', [])
            file_ids = [link['fileId'] for link in links]
            download_docx_files(links)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = json.dumps({"status": "success", "message": "All files downloaded", "fileIds": file_ids})
            self.wfile.write(response.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

def generate_self_signed_cert(cert_file, key_file):
    if not os.path.exists(cert_file) or not os.path.exists(key_file):
        print("Generating self-signed SSL certificate...")
        cmd = [
            'openssl', 'req', '-nodes', '-new', '-x509',
            '-keyout', key_file,
            '-out', cert_file,
            '-days', '365',
            '-subj', '/C=US/ST=Florida/L=Davie/O=TestMDOrg/OU=TestOrgUnitName/CN=localhost' # TODO This will need to be updated to pull from config
        ]
        subprocess.check_call(cmd)
        print("Self-signed SSL certificate generated.")

def run_server():
    server_address = ('', server_port)
    httpd = HTTPServer(server_address, RequestHandler)
    httpd.socket = ssl.wrap_socket(httpd.socket, certfile='./server.cert', keyfile='./server.key', server_side=True)
    print("Starting HTTPS server on port {}".format(server_port))
    httpd.serve_forever()

def download_docx_files(links):
    for link in links:
        try:
            url = link['url']
            filename = link['filename']
            print("Downloading .docx file from URL: {}".format(url))
            response = requests.get(url)
            if response.status_code == 200:
                with open(filename, 'wb') as file:
                    file.write(response.content)
                print("Downloaded .docx file: {}".format(filename))
            else:
                print("Failed to download .docx file from URL: {}. Status code: {}".format(url, response.status_code))
        except Exception as e:
            print("Error downloading .docx file from URL: {}. Error: {}".format(url, e))

def open_browser_with_executable(url, browser_path=None):
    """
    Opens a browser with the specified URL using a provided browser executable path or the default browser.
    """
    try:
        if browser_path:
            log("Attempting to open URL with provided executable: {} {}".format(browser_path, url))
            # Try to open the browser using subprocess.Popen
            process = subprocess.Popen([browser_path, url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            if process.returncode == 0:
                log("Browser opened with provided executable path using subprocess.Popen.")
            else:
                log("Browser failed to open using subprocess.Popen. Return code: {}. Stderr: {}".format(process.returncode, stderr))
        else:
            # Fall back to the default browser if no specific path is provided
            log("No browser path provided. Attempting to open URL with default browser: {}".format(url))
            webbrowser.open(url)
            log("Default browser opened.")
    except Exception as e:
        log("Failed to open browser: {}".format(e))

def initiate_link_retrieval():
    """
    Opens the web application through a direct URL that includes the action parameter.
    """
    log("Initiating link retrieval process.")
    # Direct URL that includes the action parameter to load the HTML content directly
    url = "https://script.google.com/macros/s/AKfycbzlq8d32mDlLdtFxgL_zvLJernlGPB64ftyxyH8F1nNlr3P-VBH6Yd0NGa1pbBc5AozvQ/exec?action=get_link"
    try:
        browser_path = sys.argv[1] if len(sys.argv) > 1 else None
        open_browser_with_executable(url, browser_path)
    except Exception as e:
        log("Error during link retrieval initiation: {}".format(e))

if __name__ == "__main__":
    # Generate SSL certificate if it doesn't exist
    generate_self_signed_cert(cert_file, key_file)
    
    from threading import Thread
    server_thread = Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()
    initiate_link_retrieval()