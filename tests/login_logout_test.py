from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from managers.browser_manager import BrowserManager

class LoginLogoutTest:
    COMMON_USER_FIELDS = ["username", "user", "email"]
    COMMON_PASS_FIELDS = ["password", "pass"]

    def __init__(self, login_url, logout_url, credential_manager, proxy_manager, solver, headless=True):
        self.login_url = login_url
        self.logout_url = logout_url
        self.credential_manager = credential_manager
        self.proxy_manager = proxy_manager
        self.solver = solver
        self.headless = headless

    def find_field(self, driver, possible_names, timeout=15):
        """
        Try multiple common field names and return the first one found
        """
        for name in possible_names:
            try:
                field = WebDriverWait(driver, timeout).until(
                    EC.presence_of_element_located((By.NAME, name))
                )
                return field
            except TimeoutException:
                continue
        raise NoSuchElementException(f"None of the field names {possible_names} were found")

    def run(self, cycles=10):
        for i in range(cycles):
            print(f"\n[RUN] Cycle {i+1}/{cycles}")
            proxy = self.proxy_manager.get_next_proxy()
            cred = self.credential_manager.get_next_credential()

            browser = BrowserManager(proxy, self.headless)
            driver = browser.driver

            try:
                driver.get(self.login_url)

                # Handle iframe if present (optional)
                iframes = driver.find_elements(By.TAG_NAME, "iframe")
                if iframes:
                    driver.switch_to.frame(iframes[0])

                # Find username and password fields
                username_field = self.find_field(driver, self.COMMON_USER_FIELDS)
                password_field = self.find_field(driver, self.COMMON_PASS_FIELDS)

                # Fill credentials
                username_field.clear()
                username_field.send_keys(cred["username"])
                password_field.clear()
                password_field.send_keys(cred["password"])

                # Solve CAPTCHA if present
                self.solver.solve_if_present(driver)

                # Submit login
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
                )
                submit_button.click()

                # Wait until the URL changes (login successful)
                WebDriverWait(driver, 10).until(lambda d: d.current_url != self.login_url)

                # Logout
                driver.get(self.logout_url)
                WebDriverWait(driver, 5).until(lambda d: d.current_url != self.logout_url)

                print(f"[SUCCESS] Logged in as {cred['username']} via {proxy['ip']}")

            except TimeoutException as te:
                print(f"[ERROR] Timeout while waiting for elements: {te}")
            except Exception as e:
                print(f"[ERROR] {e}")
            finally:
                browser.quit()
