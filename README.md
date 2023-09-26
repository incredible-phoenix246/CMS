# CMS Detection and Security Assessment Script

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)

This Python script allows you to detect the Content Management System (CMS) used by a target website, identify common patterns associated with CMSs, scrape the CMS version information from the website, and check for common security issues.

## Features

- CMS Detection: The script identifies the CMS used by a target website by checking for common CMS-related patterns.

- Pattern Detection: It also detects and prints common patterns associated with the identified CMS.

- CMS Version Scraping: The script scrapes the CMS version information from the website's HTML.

- Security Assessment: It checks for common security issues associated with CMSs, including weak password usage and exposed sensitive files.

## Prerequisites

Before using this script, ensure you have the following installed:

- Python 3.x
- Requests library

  ```
  pip install requests
  ```

- BeautifulSoup4 library
  ```
  pip install beautifulsoup4
  ```

## Usage

1. Clone this repository or download the script (cms_detection_security.py) to your local machine.

2. Open a terminal and navigate to the directory containing the script.

3. Run the script using the following command:

   ```
   python cms.py
   ```

4. Enter the target URL in the format https://example.com when prompted.

5. The script will perform the following tasks:

- Detect the CMS used by the website.
- Identify common patterns associated with the CMS (if detected).
- Scrape the CMS version information.
- heck for common security issues.

6. Review the script's output to see the detected CMS, patterns, CMS version, and security assessment results.

## Customization

- You can customize the script by adding more CMS patterns to the `cms_patterns dictionary`.

- To perform additional security checks, modify the `check_security_issues` function as needed.

- For scraping CMS version information, customize the `scrape_cms_version` function based on how the CMS version is indicated in the HTML of the websites you are assessing.
