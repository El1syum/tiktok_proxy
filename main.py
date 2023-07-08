import time

from dotenv import dotenv_values
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from seleniumwire.webdriver import Chrome


def main():
    options = {
        'proxy': {
            'http': dotenv_values().get('PROXY'),
            'https': dotenv_values().get('PROXY'),
            'no_proxy': 'localhost,127.0.0.1'
        }
    }
    driver = Chrome(seleniumwire_options=options)

    try:
        driver.get('https://www.tiktok.com/')
        driver.find_element(by=By.XPATH, value='//*[@id="loginContainer"]/div/div/a[2]').click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="loginContainer"]/div[2]/form/a'))
        ).click()

        driver.find_element(by=By.XPATH, value='//*[@id="loginContainer"]/div[2]/form/div[2]/div/div[1]').click()
        driver.find_element(by=By.XPATH, value='//*[@id="login-phone-search"]').send_keys('russia')
        driver.find_element(by=By.XPATH, value='//*[@id="area-number-pick-ul"]/li[18]').click()

        driver.find_element(by=By.XPATH, value='//*[@id="loginContainer"]/div[2]/form/div[2]/div/div[2]/input'). \
            send_keys(dotenv_values().get('NUMBER'))
        driver.find_element(by=By.XPATH, value='//*[@id="loginContainer"]/div[2]/form/div[3]/div/input'). \
            send_keys(dotenv_values().get('PASSWORD'))
        driver.find_element(by=By.XPATH, value='//*[@id="loginContainer"]/div[2]/form/button').click()

        time.sleep(10e1000)
    finally:
        driver.quit()


if __name__ == '__main__':
    main()
