from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pickle
import os

output_dir = f"{os.getcwd()}/output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

cookies_exist = False
cookies = "cookies.pkl"
if os.path.exists(f"{os.getcwd()}/{cookies}"):
    cookies_exist = True

options = Options()
options.add_argument("--window-size=1920,1080")
if cookies_exist:
    options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 120, poll_frequency=1)


def login():
    LOGIN_BUTTON = (
        "xpath",
        "//*[contains(@class, 'index-module-login-K8jzD')]",
    )
    wait.until(ec.visibility_of_element_located(LOGIN_BUTTON)).click()

    PROFILE_MENU = (
        "xpath",
        "//*[contains(@class, 'index-module-username-bFXLV')]",
    )
    wait.until(ec.visibility_of_element_located(PROFILE_MENU))


def test_authorized_user():
    driver.get("https://www.avito.ru/avito-care/eco-impact")

    if cookies_exist:
        for cookie in pickle.load(open(f"{os.getcwd()}/{cookies}", "rb")):
            driver.add_cookie(cookie)
        driver.refresh()
    else:
        login()
        pickle.dump(driver.get_cookies(), open(f"{os.getcwd()}/{cookies}", "wb"))

    COUNTERS = (
        "xpath",
        "//*[@class='desktop-value-Nd1tR']/ancestor::*[contains(@class, 'desktop-impact-item-eeQO3')]",
    )
    wait.until(ec.visibility_of_all_elements_located(COUNTERS))
    driver.execute_script("window.scrollTo({top: window.scrollY + 700});")
    counters = driver.find_elements(*COUNTERS)

    for i in range(len(counters)):
        counters[i].screenshot(f"/{output_dir}/testcase_2_{i}.png")
