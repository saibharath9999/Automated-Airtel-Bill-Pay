from selenium import webdriver
import time
import sys

class airtel:

    def __init__(self,mobile,amnt):
        self.mobile = mobile
        self.amnt = amnt

    def __del__(self):
        dr.quit()

    @staticmethod
    def webPage():
        global dr
        cd="/Users/marellasaibharath/Downloads/chromedriver"
        dr = webdriver.Chrome(cd)
        dr.get("https://www.airtel.in/postpaid-bill-pay/")
    def details(self):
        Num=dr.find_element_by_name('phone_number_field')
        Num.send_keys(self.mobile)
        time.sleep(1)
        Amnt=dr.find_element_by_id('amount_input')
        time.sleep(2)
        Amnt.send_keys(self.amnt)
        dr.find_element_by_xpath('//*[@id="scroll"]/div/section/div[2]/button').click()
        time.sleep(3)
    # Debit/Credit Card Payment
    @staticmethod
    def paySelect(name,card_num,mnth,year,cvv):
        dr.find_element_by_xpath('//*[@id="payments_tab"]/payment-options/div/div/div/ul/li[2]/a').click()
        cardname=dr.find_element_by_id('card_holder_name')
        cardname.send_keys(name)
        cardnum=dr.find_element_by_id('card_number')
        cardnum.send_keys(card_num)
        mnth=dr.find_element_by_id('expiry_month')
        mnth.send_keys(mnth)
        year=dr.find_element_by_name('expiry_year')
        year.send_keys(year)
        cvv=dr.find_element_by_id('cvv')
        cvv.send_keys(cvv)
        # Uncomment the following line during payment.
        #dr.find_element_by_xpath('//*[@id="payments_tab"]/payment-options/div/div/div/div/div[2]/cards-tab/div/page-buttons/div/div/div/div/div/button[1]').click()

bill = airtel(sys.argv[1],sys.argv[2])
bill.webPage()
bill.details()
bill.paySelect("name","card_num","mnth","year","cvv")
