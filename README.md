# 500 Login-Logout Test from Different IPs Using Selenium + NopeCHA

## 📌 Overview
This project performs automated **login/logout cycles** on a target website using:
- **Selenium WebDriver** for browser automation
- **Proxy rotation** for simulating different IPs/networks
- **NopeCHA API** for solving CAPTCHAs (only when present)
- **Environment variables** for secure configuration
- **CSV-based credentials & proxies** for scalability

**⚠ LEGAL DISCLAIMER:**  
This tool is intended **only** for websites where you have **explicit written permission** from the owner to perform automated testing.  
Unauthorized automated access may violate laws such as the Computer Fraud and Abuse Act (CFAA), GDPR, and others.  
CAPTCHA bypass should only be tested in controlled or staging environments.

---

## 📂 Project Structure
├── managers/
│ ├── init.py
│ ├── browser_manager.py
│ ├── captcha_solver.py
│ ├── credential_manager.py
│ └── proxy_manager.py
├── tests/
│ ├── init.py
│ └── login_logout_test.py
├── credentials.csv
├── proxies.csv
├── .env
├── .gitignore
├── README.md
└── selenium_nopecha_runner.py


---

## 🔧 Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/selenium-login-test.git
cd selenium-login-test
```
---

### 2️⃣ Install dependencies
```
pip install -r requirements.txt
```
---
### 3️⃣ Set environment variables
Edit .env with your target URLs and NopeCHA API key.

Example:
```LOGIN_URL=https://example.com/login
LOGOUT_URL=https://example.com/logout
NOPECHA_KEY=your-nopecha-api-key
HEADLESS=true
```
### #️⃣ Add credentials and proxies
Edit credentials.csv with test usernames & passwords

Edit proxies.csv with IPs, ports, and optional authentication

### 5️⃣ Run the test
```
python selenium_nopecha_runner.py
```

## How It Works
-Loads environment variables from .env

-Reads credentials & proxies from CSV files

-Creates a browser instance with a new proxy each run

-Logs into the site, solving CAPTCHA only if detected

-Logs out

-Repeats the cycle (default: 5 times, configurable)

## Legal & Ethical Use
DO

-Use with permission from the site owner

-Test in staging or QA environments when possible

DON’T 

-Run against production without explicit written approval

-Attempt to bypass security controls without authorization

## License
This code is for educational and authorized testing purposes only.
The author assumes no liability for misuse.