# virs_scan_3_8_25.py
import os
import requests
import tkinter as tk
import time

virus_total_api_key = "606bbbd5f972fb43b113307beb576e6a2a201b5c9fca34d6ccf4fc6c207df871"

def iterate_files(folder_path):
    if not folder_path.strip():  # בדיקה אם המחרוזת ריקה או רווחים בלבד
        print("Error: No folder path specified.")
        return
    if not os.path.exists(folder_path):
        print(f"Error: The folder path does not exist: {folder_path}")
        return

    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)

        if os.path.isdir(full_path):
            iterate_files(full_path)
        else:
            scan_file(full_path)


def scan_file(file_path):
    response = upload_file(file_path)
    scan_id = response.get('scan_id')
    if scan_id:
        is_virus = get_report(scan_id)
        if is_virus:
            print("VIRUS DETECTED!!! Filepath: ", file_path)
        else:
            print("{} is not a virus".format(file_path))
    else:
        print("Unexpected response, no scan id found for file: ", file_path)

def upload_file(file_path):
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': virus_total_api_key}

    file_content = open(file_path, 'rb')
    filename = os.path.basename(file_path)
    files = {'file': (filename, file_content)}

    response = requests.post(url, files=files, params=params)
    return response.json()

def get_report(scan_id):
    print("Getting report for scan id", scan_id)
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': virus_total_api_key, 'resource': scan_id}

    response = requests.get(url, params=params)
    if not response:
        raise Exception("Unexpected Error in response")

    if response.status_code == 200:
        response = response.json()
        if response.get('response_code') != 1:
            print("Scan not completed...")
            time.sleep(5)
            return get_report(scan_id)
        else:
            return response.get("positives") > 0
    elif response.status_code == 204:
        print("Empty response...")
        time.sleep(5)
        return get_report(scan_id)
    else:
        print("Received unexpected response with status code:", response.status_code)
        return False

# GUI setup
root = tk.Tk()
root.title("Virus Scan")

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

button = tk.Button(root, text="Scan Folder", command=lambda: iterate_files(entry.get()))
button.pack(pady=5)

output_label = tk.Label(root, text="")
output_label.pack(pady=10)

root.mainloop()
