from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r"E:\ESTUDOS\CURSOS\PYTHON\livroexe\bot_coment\geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(5)
        
        # Go to login
        #bottom_lg = driver.find_element_by_xpath('//a [@href="/accounts/login/?source=auth_switcher"]')
        #bottom_lg.click()
        # Enter Username
        input_user = driver.find_element_by_xpath('//input [@name="username"]')
        input_user.click()
        input_user.clear()
        input_user.send_keys(self.username)

        # Enter Password
        input_pass = driver.find_element_by_xpath('//input [@name="password"]')
        input_pass.click()
        input_pass.clear()
        input_pass.send_keys(self.password)
        # Enter
        input_pass.send_keys(Keys.RETURN)
        
        time.sleep(5)
        self.tag_photos('money')

    @staticmethod
    def person(phrase, loc):
        for word in phrase:
            loc.send_keys(word)
            time.sleep(random.randint(1,5)/30) # tempo para digitar cada letra.

    def tag_photos(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/"+ hashtag +"/")
        
        for i in range(1,3):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(5)

        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href]
        print(hashtag + 'fotos ' + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            try:
                comments_list = ["dam", "oh shit"]
                
                driver.find_element_by_class_name('Ypffh').click()
                input_comment = driver.find_element_by_class_name('Ypffh')
                time.sleep(random.randint(3, 5))
                
                self.person(random.choice(comments_list), input_comment)
                time.sleep(random.randint(5, 10)) #tempo até publicar comentario.
                driver.find_element_by_xpath('//button[contains(text(),"Publicar")]').click()
                time.sleep(5)
            except Exception as e:
                print(e)
                time.sleep(5)

insta_user = "dalmatica_" #input("Enter a User...:  ")
insta_pass = 'Estivemega$10' #input("Enter a pass...:  ")

ganharSorteio = InstagramBot(insta_user, insta_pass)
ganharSorteio.login()