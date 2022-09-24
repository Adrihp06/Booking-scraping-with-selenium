from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def apply_star_rating(self, star_value):
        #NO LO CONSIGO
        star_filtration_box = self.driver.find_element_by_css_selector('input[name="class=5"]')
        star_filtration_box.click()
        star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR, '*')
        #print(len(star_child_elements))

        #for star_element in star_child_elements:
            #if str(star_element == f'{star_value} estrellas':
                #star_element.click()