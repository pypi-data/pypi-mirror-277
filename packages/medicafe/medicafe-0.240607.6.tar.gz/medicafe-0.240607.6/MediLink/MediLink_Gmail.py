import sys
import os
import subprocess
import webbrowser
from MediLink_ConfigLoader import log, load_configuration

import requests
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl
import signal
from threading import Thread, Event

config, _ = load_configuration()
local_storage_path = config['MediLink_Config']['local_storage_path']
downloaded_emails_file = os.path.join(local_storage_path, 'downloaded_emails.txt')

server_port = 8000
cert_file = 'server.cert'
key_file = 'server.key'
openssl_cnf = 'openssl.cnf' # This file needs to be located in the same place as where MediCafe is run from (so MediBot folder?)

httpd = None  # Global variable for the HTTP server
shutdown_event = Event()  # Event to signal shutdown

class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Content-type', 'application/json')

    def do_OPTIONS(self):
        self.send_response(200)
        self._set_headers()
        self.end_headers()

    def do_POST(self):
        if self.path == '/download':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            links = data.get('links', [])

            # Log the content of links
            log("Received links: {}".format(links))

            file_ids = [link.get('fileId', None) for link in links if link.get('fileId')]
            log("File IDs received from client: {}".format(file_ids))
            
            # Proceed with downloading files
            download_docx_files(links)
            self.send_response(200)
            self._set_headers()  # Include CORS headers
            self.end_headers()
            response = json.dumps({"status": "success", "message": "All files downloaded", "fileIds": file_ids})
            self.wfile.write(response.encode('utf-8'))
            shutdown_event.set()
        elif self.path == '/shutdown':
            log("Shutdown request received.")
            self.send_response(200)
            self._set_headers()
            self.end_headers()
            response = json.dumps({"status": "success", "message": "Server is shutting down."})
            self.wfile.write(response.encode('utf-8'))
            stop_server()
        elif self.path == '/delete-files':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            file_ids = data.get('fileIds', [])
            log("File IDs to delete received from client: {}".format(file_ids))
            
            if not isinstance(file_ids, list):
                self.send_response(400)
                self._set_headers()
                self.end_headers()
                response = json.dumps({"status": "error", "message": "Invalid fileIds parameter."})
                self.wfile.write(response.encode('utf-8'))
                return
            
            self.send_response(200)
            self._set_headers()  # Include CORS headers
            self.end_headers()
            response = json.dumps({"status": "success", "message": "Files deleted successfully."})
            self.wfile.write(response.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def do_GET(self):
        if self.path == '/downloaded-emails':
            self.send_response(200)
            self._set_headers()
            self.end_headers()
            downloaded_emails = load_downloaded_emails()
            response = json.dumps({"downloadedEmails": list(downloaded_emails)})
            self.wfile.write(response.encode('utf-8'))
        else:
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'HTTPS server is running.')

def generate_self_signed_cert(cert_file, key_file):
    if not os.path.exists(cert_file) or not os.path.exists(key_file):
        log("Generating self-signed SSL certificate...")
        cmd = [
            'openssl', 'req', '-config', openssl_cnf, '-nodes', '-new', '-x509',
            '-keyout', key_file,
            '-out', cert_file,
            '-days', '365'
            #'-subj', '/C=US/ST=...' The openssl.cnf file contains default values for these fields, but they can be overridden by the -subj option.
        ]
        try:
            result = subprocess.call(cmd)
            if result != 0:
                raise RuntimeError("Failed to generate self-signed certificate")
            log("Self-signed SSL certificate generated.")
        except Exception as e:
            log("Error generating self-signed certificate: {}".format(e))
            raise

def run_server():
    global httpd
    try:
        server_address = ('0.0.0.0', server_port)  # Bind to all interfaces
        httpd = HTTPServer(server_address, RequestHandler)
        httpd.socket = ssl.wrap_socket(httpd.socket, certfile=cert_file, keyfile=key_file, server_side=True)
        log("Starting HTTPS server on port {}".format(server_port))
        httpd.serve_forever()
    except Exception as e:
        log("Error in serving: {}".format(e))
        stop_server()

def stop_server():
    global httpd
    if httpd:
        log("Stopping HTTPS server.")
        httpd.shutdown()
        httpd.server_close()
        log("HTTPS server stopped.")
    shutdown_event.set()  # Signal shutdown event

def load_downloaded_emails():
    downloaded_emails = set()
    if os.path.exists(downloaded_emails_file):
        with open(downloaded_emails_file, 'r') as file:
            downloaded_emails = set(line.strip() for line in file)
    log("Loaded downloaded emails: {}".format(downloaded_emails))
    return downloaded_emails

def download_docx_files(links):
    # Load the set of downloaded emails
    downloaded_emails = load_downloaded_emails()

    for link in links:
        try:
            url = link.get('url', '')
            filename = link.get('filename', '')
            
            # Log the variables to debug
            log("Processing link: url='{}', filename='{}'".format(url, filename))
            
            # Skip if email already downloaded
            if filename in downloaded_emails:
                log("Skipping already downloaded email: {}".format(filename))
                continue

            log("Downloading .docx file from URL: {}".format(url))
            response = requests.get(url, verify=False)  # Set verify to False for self-signed certs
            if response.status_code == 200:
                file_path = os.path.join(local_storage_path, filename)
                with open(file_path, 'wb') as file:
                    file.write(response.content)
                log("Downloaded .docx file: {}".format(filename))
                # Add to the set and save the updated list
                downloaded_emails.add(filename)
                with open(downloaded_emails_file, 'a') as file:
                    file.write(filename + '\n')
            else:
                log("Failed to download .docx file from URL: {}. Status code: {}".format(url, response.status_code))
        except Exception as e:
            log("Error downloading .docx file from URL: {}. Error: {}".format(url, e))

def open_browser_with_executable(url, browser_path=None):
    try:
        if browser_path:
            log("Attempting to open URL with provided executable: {} {}".format(browser_path, url))
            process = subprocess.Popen([browser_path, url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            if process.returncode == 0:
                log("Browser opened with provided executable path using subprocess.Popen.")
            else:
                log("Browser failed to open using subprocess.Popen. Return code: {}. Stderr: {}".format(process.returncode, stderr))
        else:
            log("No browser path provided. Attempting to open URL with default browser: {}".format(url))
            webbrowser.open(url)
            log("Default browser opened.")
    except Exception as e:
        log("Failed to open browser: {}".format(e))

def initiate_link_retrieval():
    log("Initiating link retrieval process.")
    url = "https://script.google.com/macros/s/AKfycbzlq8d32mDlLdtFxgL_zvLJernlGPB64ftyxyH8F1nNlr3P-VBH6Yd0NGa1pbBc5AozvQ/exec?action=get_link"
    downloaded_emails = list(load_downloaded_emails())
    payload = {"downloadedEmails": downloaded_emails}

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            log("Link retrieval initiated successfully.")
        else:
            log("Failed to initiate link retrieval. Status code: {}".format(response.status_code))
    except Exception as e:
        log("Error during link retrieval initiation: {}".format(e))

def signal_handler(sig, frame):
    log("Signal received: {}. Initiating shutdown.".format(sig))
    stop_server()
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    try:
        # Generate SSL certificate if it doesn't exist
        generate_self_signed_cert(cert_file, key_file)
        
        from threading import Thread
        server_thread = Thread(target=run_server)
        server_thread.daemon = True
        server_thread.start()
        initiate_link_retrieval()
        server_thread.join()  # Wait for the server thread to finish
        shutdown_event.wait() # Wait for the shutdown event to be set
        stop_server()
    except KeyboardInterrupt:
        stop_server()
        sys.exit(0)
    except Exception as e:
        log("An error occurred: {}".format(e))
        stop_server()
        sys.exit(1)