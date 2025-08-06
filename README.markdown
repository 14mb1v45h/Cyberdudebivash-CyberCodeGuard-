# CyberCodeGuard

CyberCodeGuard is an AI-powered code vulnerability scanner designed to help developers identify security issues in their codebases. It uses machine learning to detect common vulnerabilities like hardcoded credentials, unsafe functions, and more, with a focus on reducing false positives. The tool integrates with GitHub to scan repositories and provides a clear report of findings.

## Features
- **AI-Driven Analysis**: Leverages a machine learning model to classify code snippets as safe or vulnerable.
- **GitHub Integration**: Scans Python files in GitHub repositories using the GitHub API.
- **Customizable Detection**: Identifies specific vulnerabilities like hardcoded credentials, unsafe `eval()`, and risky system commands.
- **Extensible**: Easily adaptable to support additional programming languages or vulnerability patterns.

## Prerequisites
- Python 3.8 or higher
- GitHub Personal Access Token (with `repo` scope)
- Required Python libraries: `requests`, `scikit-learn`, `pandas`, `numpy`

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/14mb1v45h/Cyberdudebivash-CyberCodeGuard-.git
   cd YOUR_REPO_NAME
   ```
2. **Install Dependencies**:
   ```bash
   pip install requests scikit-learn pandas numpy
   ```
3. **Set Up GitHub Token**:
   - Generate a Personal Access Token from [GitHub Settings](https://github.com/settings/tokens).
   - Update the `GITHUB_TOKEN`, `REPO_OWNER`, and `REPO_NAME` variables in `cybercodeguard.py` with your details.

## Usage
1. **Run the Scanner**:
   ```bash
   python cybercodeguard.py
   ```
2. **View the Report**:
   - The script will scan all `.py` files in the specified GitHub repository.
   - A vulnerability report will be printed to the console, listing files and detected issues (e.g., "Line 5: Hardcoded credentials detected").

## Example Output
```
Vulnerability Report:
File: example.py
  - Line 3: Hardcoded credentials detected
  - Line 10: Unsafe use of eval() detected
File: utils.py
  - Line 7: Unsafe system command detected
```

## Extending the Tool
- **Add More Patterns**: Update the `analyze_code` function to detect additional vulnerabilities (e.g., SQL injection, XSS).
- **Support Other Languages**: Modify the file filtering logic to include `.js`, `.java`, or other file types.
- **Enhance the Model**: Replace the simple Logistic Regression model with a more advanced one (e.g., BERT for code analysis).
- **Add a Web Interface**: Integrate a frontend (e.g., Flask or React) for a user-friendly dashboard.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m "Add your feature"`).
4. Push to your branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

Please ensure your code follows PEP 8 standards and includes tests for new features.

## License
This project is licensed under the MIT License. 

## Contact
For questions or suggestions, reach out to [Cyberdudebivash](https://github.com/14mb1v45h/Cyberdudebivash-CyberCodeGuard-.git) or open an issue in the repository.
contact iambivash.bn@proton.me for any issues or support .

## Copyright

Copyright @cyberdudebivash 2025 
Powered by cyberdudebivash
