from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class BookingReport:
    def __init__(self, boxes_section_element:WebElement):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements(By.CSS_SELECTOR,'div[data-testid="property-card"]')
    def pull_titles(self):
        collection = []
        for deal_box in self.deal_boxes:
            hotel_name = deal_box.find_element(By.CLASS_NAME,'fde444d7ef').get_attribute('innerHTML').strip()
            hotel_price = deal_box.find_element(By.CLASS_NAME,'_e885fdc12').get_attribute('innerHTML').strip()
            hotel_score = deal_box.find_elements(By.CSS_SELECTOR, 'span[aria-hidden="true"]')
            collection.append([hotel_name, hotel_price[7:], len(hotel_score)])
        return collection