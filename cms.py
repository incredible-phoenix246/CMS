import requests
from bs4 import BeautifulSoup

# Define common CMS-related patterns
cms_patterns = {
    "WordPress": [
        "/wp-content/",
        "/wp-includes/",
        "/wp-admin/",
        "/xmlrpc.php",
        "/readme.html",
    ],
    "Joomla": [
        "/administrator/",
        "/components/",
        "/templates/",
        "/media/",
        "/libraries/",
    ],
    "Drupal": [
        "/sites/default/",
        "/core/",
        "/includes/",
        "/misc/",
    ],
    "Magento": [
        "/skin/frontend/",
        "/app/etc/",
        "/js/",
        "/media/",
    ],
    # Add more patterns for other CMSs as needed
}

# Function to identify CMS based on patterns
def identify_cms(url):
    detected_patterns = []
    for cms, patterns in cms_patterns.items():
        for pattern in patterns:
            response = requests.get(url + pattern)
            if response.status_code == 200:
                detected_patterns.append(pattern)
                return cms, detected_patterns
    return "Unknown", detected_patterns

# Function to scrape CMS version information from HTML
def scrape_cms_version(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Customize this part based on how the CMS version is indicated in HTML
        version_element = soup.find("meta", {"name": "generator"})
        
        if version_element:
            return version_element.get("content")
        else:
            return "Version not found"
    except Exception as e:
        return "Unable to scrape version"

# Function to check for common security issues
def check_security_issues(url):
    try:
        response = requests.get(url)
        
        # Check for security issues
        security_issues = []
        
        # Check for weak passwords
        if "password" in response.text.lower():
            security_issues.append("Weak password usage detected.")
        
        # Check for exposed sensitive files
        sensitive_files = ["config.php", "settings.php", "web.config"]
        for file in sensitive_files:
            if file in response.text:
                security_issues.append(f"Exposed sensitive file: {file}")
        
        # Add more security checks as needed
        
        if security_issues:
            return "\n".join(security_issues)
        else:
            return "No security issues found"
    except Exception as e:
        return "Unable to perform security checks"

# Get the target URL from the user
target_url = input("Enter the target URL (e.g., https://example.com): ")

# Identify the CMS based on the input URL
cms_detected, detected_patterns = identify_cms(target_url)

if cms_detected != "Unknown":
    print(f"The CMS detected on {target_url} is: {cms_detected}")
    if detected_patterns:
        print(f"Detected patterns: {', '.join(detected_patterns)}")

    # Scrape CMS version information
    cms_version = scrape_cms_version(target_url)
    print(f"CMS Version: {cms_version}")

    # Check for common security issues
    security_issues = check_security_issues(target_url)
    print(security_issues)
else:
    print(f"No CMS was detected on {target_url}")
