# README Link Checker
#
# This script checks the online status of links in a README.md file. It extracts all URLs from the README file
# and sends a HEAD request to each URL to determine if the link is online or not.
#
#     python check_readme_links.py path/to/README.md
#
# Author: Brandon Himpfen
# Website: himpfen.xyz

import requests
import re

def check_links(file_path):
    with open(file_path, 'r') as readme_file:
        contents = readme_file.read()

    # Extract all URLs from the README file
    urls = re.findall(r'\[.*\]\((http[s]?://.*?)\)', contents)

    for url in urls:
        try:
            response = requests.head(url)
            if response.status_code == 200:
                print(f"Link {url} is online.")
            else:
                print(f"Link {url} returned status code {response.status_code}.")
        except requests.exceptions.RequestException as e:
            print(f"Error occurred while checking link {url}: {str(e)}")

# Provide the path to your README.md file
readme_path = 'path/to/README.md'
check_links(readme_path)
