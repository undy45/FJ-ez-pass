from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

import config


class EasyPass:
    def __init__(self):
        self.driver = webdriver.Chrome(config.path_to_driver)
        self.login()
        list_of_tests_url = self.get_list_of_test_url()
        links = self.get_tests_links(list_of_tests_url)
        self.solve_tests(links)

    def solve_tests(self, links):
        for link in links:
            self.driver.get(link)
            self.find(By.XPATH, "//button[contains(text(), 'Spustit nový odpovědník')]").click()
            self.find(By.XPATH, "//button[contains(text(), 'Odevzdat')]").click()
            self.find(By.LINK_TEXT, "Prohlídka").click()
            answers = self.driver.find_elements_by_xpath("//span[@class='ok']")
            answers = [answer.text[1:-1].split(',')[0].strip() for answer in answers]
            self.find(By.XPATH, "//a[contains(text(), 'Zpět')]").click()
            self.find(By.XPATH, "//div[@class='shrink column']/a[contains(text(), 'Znovu odpovídat')]").click()
            cells = self.driver.find_elements_by_xpath("//input[@type='text']")
            for i, cell in enumerate(cells):
                cell.send_keys(answers[i])
            self.find(By.XPATH, "//button[contains(text(), 'Odevzdat')]").click()
            sleep(1)

    def get_tests_links(self, list_of_tests_url):
        self.driver.get(list_of_tests_url)
        elements = self.driver.find_elements_by_xpath(f"//tr/td/a[starts-with(text(), '{config.lecture_index}. ')]")
        links = [element.get_attribute('href') for element in elements]
        return links

    def login(self):
        self.driver.get(config.login_url)

        elem = self.driver.find_element_by_name("credential_0")
        elem.send_keys(config.UCO)

        elem = self.driver.find_element_by_name("credential_1")
        elem.send_keys(config.primary_password)
        elem.send_keys(Keys.RETURN)

    def get_list_of_test_url(self):
        self.find(By.XPATH, "//div/a[contains(text(), 'Student')]").click()
        self.find(By.XPATH, "//a[span/strong[contains(text(), 'FJ1028')]]").click()
        self.find(By.XPATH, ".//div[@class='row student_row_b']/div/a")
        link = self.driver.find_elements_by_xpath(".//div[@class='row student_row_b']/div/a")[-2].get_attribute("href")
        return link

    def find(self, by_method, pattern, wait_time=10):
        try:
            element = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((by_method, pattern))
            )
            return element
        except:
            self.driver.quit()


a = EasyPass()
sleep(5)
