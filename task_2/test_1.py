from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pathlib import Path
import os

output_dir = f"{Path(__file__).resolve().parent}/output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 120, poll_frequency=1)


def test_unauthorized_user():
    driver.get("https://www.avito.ru/avito-care/eco-impact")

    COUNTERS = (
        "xpath",
        "//*[@class='desktop-value-Nd1tR']/ancestor::*[contains(@class, 'desktop-impact-item-eeQO3')]",
    )
    wait.until(ec.visibility_of_all_elements_located(COUNTERS))
    driver.execute_script("window.scrollTo({top: window.scrollY + 700});")
    counters = driver.find_elements(*COUNTERS)

    for i in range(len(counters)):
        counters[i].screenshot(f"/{output_dir}/testcase_1_{i}.png")
