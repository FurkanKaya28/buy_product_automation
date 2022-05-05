import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class BuyProduct(object):
    BaseURL = "https://www.apple.com/tr/"

    def __setup(self):
        self.__driver = webdriver.Chrome()
        self.__driver.maximize_window()
        self.__driver.get(self.BaseURL)

    def __quit(self):
        self.__driver.close()
        self.__driver.quit()

    def __click_element(self, locator):
        self.__driver.find_element(By.XPATH, locator).click()
        time.sleep(2)

    def __check_price(self, count, total_price):
        item_count = self.__driver.find_element(By.XPATH,
                                                "/html/body/div[2]/div[4]/div[2]/div[1]/ol/li/div/div[2]/div[1]/div[2]/div/div/div/select[1]")
        Select(item_count).select_by_value(str(count))
        time.sleep(2)
        assert total_price in self.__driver.find_element(By.XPATH,
                                                         '//*[@id="bag-content"]/ol/li/div/div[2]/div[1]/div[3]/div[1]/p').text

    def buy_ipad(self):
        self.__setup()

        self.__click_element("/html/body/nav[1]/div/ul[2]/li[4]/a")
        self.__click_element("/html/body/main/section[2]/div/div/div[1]/div/a")
        assert "iPad Air" in self.__driver.title

        self.__click_element(
            '/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/fieldset/div/div[1]/label')
        self.__click_element(
            '/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div/div/fieldset/div[2]/div[1]/label')
        self.__click_element(
            '/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div/div/div/fieldset/div[2]/div[1]/label')
        self.__click_element(
            '/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/div[2]/div[3]/div/div/div/div[1]/div/fieldset/div/div[3]/label')
        self.__click_element(
            '/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/div[2]/div[5]/div/div/div/div/div/div[2]/div/button')
        self.__click_element(
            '/html/body/div[2]/div[5]/div[3]/div[2]/div[2]/div[2]/div[7]/div[1]/div/div[5]/div/form/div/span/button/span')
        self.__click_element('/html/body/div[2]/div[4]/div[2]/div[2]/div/div/div[2]/div/form/button')

        assert "Çanta" in self.__driver.title
        self.__check_price(1, "10.699,00 TL")
        self.__check_price(2, "21.398,00 TL")
        self.__check_price(3, "32.097,00 TL")
        self.__check_price(4, "42.796,00 TL")
        self.__check_price(5, "53.495,00 TL")
        self.__check_price(6, "64.194,00 TL")

        print("The iPad product can be purchased successfully.")
        self.__quit()

    def buy_iphone(self):
        self.__setup()

        self.__click_element("/html/body/nav/div/ul[2]/li[5]/a")
        self.__click_element("/html/body/main/section[2]/div[2]/div[1]/div/div[1]/ul/li[1]/a")
        assert "iPhone 13 Pro" in self.__driver.title

        self.__click_element(
            '/html/body/div[2]/div[5]/div[4]/div[2]/div[2]/div[2]/div[2]/div[1]/fieldset/div/div[1]/label')
        self.__click_element(
            '/html/body/div[2]/div[5]/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/fieldset/div/div[1]/label')
        self.__click_element(
            '/html/body/div[2]/div[5]/div[4]/div[2]/div[2]/div[2]/div[2]/div[3]/fieldset/div/div[1]/label')
        self.__click_element('//*[@id="root"]/div[2]/div[2]/div[2]/div[4]/div[1]/div/div[3]/div/form/div/span/button')
        self.__click_element('//*[@id="root"]/div[2]/div/div/div[2]/div/form/button')

        assert "Çanta" in self.__driver.title
        self.__check_price(1, "24.999,00 TL")
        self.__check_price(2, "49.998,00 TL")
        self.__check_price(3, "74.997,00 TL")
        self.__check_price(4, "99.996,00 TL")
        self.__check_price(5, "124.995,00 TL")
        self.__check_price(6, "149.994,00 TL")

        print("The iPhone product can be purchased successfully.")
        self.__quit()


buy_product = BuyProduct()
buy_product.buy_ipad()
buy_product.buy_iphone()
