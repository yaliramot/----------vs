import os
import requests

response = requests.get("https://example.com")
print(response.status_code)

import requests
import time
virus_total_api_key = "606bbbd5f972fb43b113307beb576e6a2a201b5c9fca34d6ccf4fc6c207df871"


def iterate_files(folder_path):
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
            print("{} is not virus".format(file_path))
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
    print("getting report for scan id", scan_id)
    url = 'https://www.virustotal.com/vtapi/v2/file/report'

    params = {'apikey': virus_total_api_key, 'resource': scan_id}

    response = requests.get(url, params=params)
    if not response:
        raise Exception("Unexecpred Error in response")
    
    if response.status_code == 200: # Received good response
        response = response.json()
        if response.get('response_code') != 1: # Scan not completed
            print("Scan not completed...")
            time.sleep(5)
            get_report(scan_id)
        else:
            return response.get("positives") > 0
    elif response.status_code == 204: # Received response without content
        print("Empty response...")
        time.sleep(5)
        get_report(scan_id)
    else: # Received unexecpted response
        print("Received unexpected response with status code:", response.status_code)
        return False


def main():
    iterate_files("C://Users//yalir//OneDrive//Desktop//פרוייקטים vs")

if __name__ == "__main__":
    main()