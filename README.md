# 🛡️ Web Security Testing Framework

A modular **Python-based Web Security Testing Framework** developed as part of my **Offensive Security Internship at ITSOLERA Pvt Ltd**. The framework performs automated web security assessments by analyzing HTTP security headers, authentication mechanisms, forms, information disclosure, and generating professional HTML reports.

> **Disclaimer:** This tool is intended for educational purposes and authorized security assessments only. Use it only on systems you own or have explicit permission to test.

---

# 🚀 Features

- 🔐 Security Headers Analysis
- 🔑 Authentication Assessment
- 💉 SQL Injection Assessment
- ⚡ XSS Assessment
- 📄 Information Disclosure Scanner
- 📊 HTML Report Generation
- 📝 Logging System
- 💻 Command Line Interface (CLI)

---

# 📂 Project Structure

```text
WebSecurityFramework/
│
├── framework.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── modules/
│   ├── headers.py
│   ├── auth.py
│   ├── xss.py
│   ├── sqli.py
│   └── disclosure.py
│
├── utils/
│   ├── logger.py
│   └── report.py
│
├── reports/
├── logs/
└── venv/
```

---

# ⚙️ Requirements

- Python 3.10+
- requests
- beautifulsoup4
- colorama
- lxml
- tqdm

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/WebSecurityFramework.git
```

Move into the project directory

```bash
cd WebSecurityFramework
```

Create Virtual Environment

### Linux / Kali

```bash
python3 -m venv venv

source venv/bin/activate
```

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Usage

## Security Headers

```bash
python framework.py --target https://example.com --module headers
```

---

## Authentication Assessment

```bash
python framework.py --target https://example.com --module auth
```

---

## XSS Assessment

```bash
python framework.py --target https://example.com --module xss
```

---

## SQL Injection Assessment

```bash
python framework.py --target "http://testphp.vulnweb.com/listproducts.php?cat=1" --module sqli
```

---

## Information Disclosure

```bash
python framework.py --target https://example.com --module disclosure
```

---

## Run All Modules

```bash
python framework.py --target https://example.com --module all
```

---

## Help Menu

```bash
python framework.py --help
```

---

# 📄 HTML Report

The framework automatically generates an HTML report inside the **reports/** directory after execution.

Example:

```
reports/report_2026-07-24_14-30-15.html
```

The report includes:

- Target Information
- Executed Modules
- Scan Status
- Date & Time

---

# 📝 Logging

Execution logs are stored inside the **logs/** directory.

Example:

```
logs/framework.log
```

---

# 🛠 Technologies Used

- Python
- Requests
- BeautifulSoup
- HTML
- Logging
- Argparse
- Git
- GitHub

---

# 🎯 Learning Outcomes

This project helped me gain hands-on experience in:

- Web Security Testing
- HTTP Security Headers
- Authentication Analysis
- Information Disclosure Assessment
- Secure Coding Practices
- Python Automation
- HTML Report Generation
- Logging and CLI Development

---

# 📸 Sample Output

Recommended screenshots for GitHub:

- VS Code Project Structure
- CLI Execution
- HTML Report
- GitHub Repository

---

# 👨‍💻 Author

**Ali Nasir**

BS Computer Science Graduate

Offensive Security Intern

ITSOLERA Pvt Ltd

---

# 📜 License

This project is intended for educational purposes and authorized security testing only.

Do not use this framework against systems without explicit permission.
