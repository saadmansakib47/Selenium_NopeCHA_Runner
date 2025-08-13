import os
from dotenv import load_dotenv
from managers.proxy_manager import ProxyManager
from managers.credential_manager import CredentialManager
from managers.captcha_solver import CaptchaSolver
from tests.login_logout_test import LoginLogoutTest

class SeleniumNopechaRunner:
    def __init__(self, cycles=5):
        # Load environment variables
        load_dotenv()

        self.cycles = cycles
        self.config = {
            "login_url": os.getenv("LOGIN_URL"),
            "logout_url": os.getenv("LOGOUT_URL"),
            "credentials_file": os.getenv("CREDENTIALS_FILE", "credentials.csv"),
            "proxies_file": os.getenv("PROXIES_FILE", "proxies.csv"),
            "nopecha_key": os.getenv("NOPECHA_KEY"),
            "headless": os.getenv("HEADLESS", "true").lower() == "true"
        }

        # Validate required environment variables
        required_vars = ["login_url", "logout_url", "nopecha_key"]
        missing_vars = [var for var in required_vars if not self.config[var]]
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars).upper()}")

    def run(self):
        proxy_manager = ProxyManager(self.config["proxies_file"])
        credential_manager = CredentialManager(self.config["credentials_file"])
        captcha_solver = CaptchaSolver(api_key=self.config["nopecha_key"])

        tester = LoginLogoutTest(
            login_url=self.config["login_url"],
            logout_url=self.config["logout_url"],
            credential_manager=credential_manager,
            proxy_manager=proxy_manager,
            solver=captcha_solver,
            headless=self.config["headless"]
        )

        # Run the login/logout test cycles
        tester.run(cycles=self.cycles)


if __name__ == "__main__":
    # Set number of cycles here, e.g., 5 or 500 depending on your test
    runner = SeleniumNopechaRunner(cycles=5)
    runner.run()
