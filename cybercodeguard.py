import requests
import re
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import base64

# GitHub API setup
GITHUB_TOKEN = "YOUR_GITHUB_TOKEN"  # Replace with your GitHub Personal Access Token
REPO_OWNER = "YOUR_GITHUB_USERNAME"  # Replace with repository owner
REPO_NAME = "YOUR_REPO_NAME"  # Replace with repository name
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

# Simulated training data for ML model (in practice, use a larger dataset)
TRAINING_DATA = [
    ("print('hello')", 0),  # Safe
    ("password = 'hardcoded'", 1),  # Vulnerable: Hardcoded credentials
    ("os.system('rm -rf /')", 1),  # Vulnerable: Unsafe command
    ("def safe_function(): pass", 0),  # Safe
    ("eval(input())", 1),  # Vulnerable: Unsafe eval
]

# Train a simple ML model to classify code snippets
def train_model():
    texts, labels = zip(*TRAINING_DATA)
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)
    model = LogisticRegression()
    model.fit(X, labels)
    return model, vectorizer

# Fetch files from GitHub repository
def fetch_repo_files():
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print(f"Error fetching repo: {response.json().get('message')}")
        return []
    return response.json()

# Analyze a single code file for vulnerabilities
def analyze_code(content, model, vectorizer):
    findings = []
    lines = content.split("\n")
    X = vectorizer.transform(lines)
    predictions = model.predict(X)
    
    for i, (line, pred) in enumerate(zip(lines, predictions)):
        if pred == 1:
            # Check for specific patterns
            if re.search(r"password\s*=\s*['\"]", line, re.IGNORECASE):
                findings.append(f"Line {i+1}: Hardcoded credentials detected")
            elif re.search(r"eval\s*\(", line, re.IGNORECASE):
                findings.append(f"Line {i+1}: Unsafe use of eval() detected")
            elif re.search(r"os\.system\s*\(", line, re.IGNORECASE):
                findings.append(f"Line {i+1}: Unsafe system command detected")
    return findings

# Main function to scan repository
def scan_repository():
    model, vectorizer = train_model()
    files = fetch_repo_files()
    report = []
    
    for file in files:
        if file['name'].endswith('.py'):  # Only scan Python files
            file_url = file['download_url']
            response = requests.get(file_url)
            if response.status_code == 200:
                content = response.text
                findings = analyze_code(content, model, vectorizer)
                if findings:
                    report.append({"file": file['name'], "findings": findings})
    
    # Generate report
    if report:
        print("Vulnerability Report:")
        for entry in report:
            print(f"\nFile: {entry['file']}")
            for finding in entry['findings']:
                print(f"  - {finding}")
    else:
        print("No vulnerabilities found.")

if __name__ == "__main__":
    scan_repository()