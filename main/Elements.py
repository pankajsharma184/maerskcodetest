import os

class Elements:

    # chrome_driver = "chromedriver.exe"
    # driver_path = os.path.join(chrome_driver)
    Url = "https://e.ggtimer.com/"
    Text_Box = 'EggTimer-start-time-input-text'
    start_button = "/html//div[@id='root']/div[@class='EggTimer']//button[.='Start']"
    first_wait_element = "/html//div[@id='root']/div[@class='EggTimer']/main[@class='EggTimer-timer']//span[.='20 seconds ']"
    second_wait_element = "/html//div[@id='root']/div[@class='EggTimer']/main[@class='EggTimer-timer']//span[.='5 seconds ']"
