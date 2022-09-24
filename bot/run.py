from pickle import TRUE
from booking.booking import Booking


with Booking() as bot:
    bot.land_first_page()
    bot.change_idiom(idiom='es')
    bot.select_place_to_go(input("Where you want to go?"))
    bot.select_dates(check_in_date='2022-03-24',check_out_date='2022-03-30')
    bot.select_adults(1)
    bot.click_search()
    bot.report_results()
