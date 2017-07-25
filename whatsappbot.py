
from selenium import webdriver

class Bot:

    def __init__(self, wurl = "https://web.whatsapp.com/"):
        self.wurl = wurl
        self.driver = webdriver.Firefox()
        self.driver.get(wurl)
    
    def start(self):
        try:
            self.qrcode = self.driver.find_element_by_class_name('qrcode')
            return False
        except:
            return True


    def getchat(self, chatid):
        try:
            self.chat = self.driver.find_element_by_xpath('//*[@title="' + chatid  + '"]').find_element_by_xpath('../../../../../..')
            self.chat.click()
            return True
        except:
            return False

    def sendmessage(self, message):
        try:
            self.input = self.driver.find_element_by_class_name('input')
            self.input.send_keys(message)
            self.sendbtn = self.driver.find_element_by_class_name('compose-btn-send')
            self.sendbtn.click()
            return True
        except:
            return False
