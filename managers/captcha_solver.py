import time
from selenium.webdriver.common.by import By
import nopecha  # Official NopeCHA Python SDK

class CaptchaSolver:
    def __init__(self, api_key):
        self.api_key = api_key
        nopecha.api_key = self.api_key  # Set API key globally for the SDK

    def solve_if_present(self, driver):
        try:
            # Look for a reCAPTCHA iframe
            captcha_frame = driver.find_element(By.XPATH, '//iframe[contains(@src, "recaptcha")]')
            driver.switch_to.frame(captcha_frame)

            # Extract sitekey
            sitekey = driver.find_element(By.CLASS_NAME, "g-recaptcha").get_attribute("data-sitekey")
            driver.switch_to.default_content()

            print("[INFO] CAPTCHA detected, solving with NopeCHA API...")

            # Solve using the official NopeCHA solve method
            token = nopecha.Recognition.solve(
                type="recaptcha2",
                sitekey=sitekey,
                url=driver.current_url
            )

            # Inject the solution token into the page
            driver.execute_script(
                'document.getElementById("g-recaptcha-response").innerHTML = arguments[0];',
                token
            )

            time.sleep(1)  # Small delay to let the token register
            return True

        except Exception as e:
            print(f"[INFO] No CAPTCHA detected or error occurred: {e}")
            return False
