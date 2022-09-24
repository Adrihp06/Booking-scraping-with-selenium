import booking.constants as const
import os
from selenium import webdriver
from booking.booking_filtration import BookingFiltration
from booking.booking_reporty import BookingReport
from prettytable import PrettyTable




#Esto es un objeto necesario para generalizar el proceso de iniciar selenium y abrir la pagina web
class Booking(webdriver.Chrome):
    def __init__(self,driver_path=r"C:\Users\Usuario\Documents\SeleniumDrivers\chromedriver", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()


    def __exit__(self, *args) -> None:
        #al añadir la variable teardown al __init__ si la indicamos como TRUE en run.py cerrara el navegador automaticamente
        if self.teardown:
            return super().__exit__(*args)
       


#Aqui es donde lanzamos la pagina web almacenada en constants        
    def land_first_page(self):
        self.get(const.BASE_URL)



#Con esta funcion cambiamos el idioma de la pagina para ponerlo en espa
    def change_idiom(self, idiom=None):
        idiom_element = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your language"]'
        )
        idiom_element.click()
        selected_idiom_element = self.find_element_by_css_selector(
        #la f al principio es necesaria para introducir el valor de idiom
            f'a[data-lang="{idiom}"]'
        )
        selected_idiom_element.click()




    def select_place_to_go(self, place_to_go):
        search_field = self.find_element_by_id('ss')
        #borramos el texto existente
        search_field.clear()
        search_field.send_keys(place_to_go)
        first_result = self.find_element_by_css_selector(
            'li[data-i="0"]'
        )
        first_result.click()
    



    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element_by_css_selector(
            f'td[data-date="{check_in_date}"'
        )
        check_in_element.click()

        check_out_element = self.find_element_by_css_selector(
            f'td[data-date="{check_out_date}"'
        )
        check_out_element.click()



    def select_adults(self, count=1):
        selection_element = self.find_element_by_id('xp__guests__toggle')
        selection_element.click()

        #Vamos a seleccionar el numero de adultos en uno 
        while True:
            #con esto bajamos en uno el contador de adultos
            decrease_adults_element = self.find_element_by_css_selector(
                'button[aria-label="Reduce el número de Adultos"]'
            )
            decrease_adults_element.click()
            #identificamos el valor del contador de adultos
            adults_value_element = self.find_element_by_id('group_adults')
            #devuelve el contador de adultos
            adults_value = adults_value_element.get_attribute('value')

            if int(adults_value) == 1:
                break

        increase_button_element = self.find_element_by_css_selector(
            'button[aria-label="Aumenta el número de Adultos"]'
        )

        for _ in range(count - 1):
            increase_button_element.click()




    def click_search(self):
        search_button = self.find_element_by_css_selector(
            'button[type="submit"]'
        )
        search_button.click()

    def report_results(self):
        hotel_boxes = self.find_element_by_id('search_results_table')
        
        report = BookingReport(hotel_boxes)
        table = PrettyTable(
            ["Hotel Name","Hotel Price(euros)", "Hotel Score"]
        )

        table.add_rows(report.pull_titles())
        print (table)