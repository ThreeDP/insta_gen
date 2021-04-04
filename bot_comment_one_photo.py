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
        #self.get_friends('threedp.png')
        self.tag_photos('CKNo0eSBsDwRCrP79x7eQHsgp9wv1yPOER_zzU0')

    @staticmethod
    def person(phrase, loc):
        for word in phrase:
            loc.send_keys(word)
            time.sleep(random.randint(1,5)/30)
    
    def get_friends(self, username_insta):
        driver = self.driver
        driver.get("https://www.instagram.com/"+ username_insta +"/")

        try:
            following_bt = driver.find_element_by_xpath("//li[3]/a [@href='/threedp.png/following/']")
            following_bt.click()
            time.sleep(2)

            ####### ISSUE #####
            # Necessario scrollar para baixo para visualizar todos os seguidores.
            ###################

            hrefs = driver.find_elements_by_tag_name("a")
            list_friends = [elem.get_attribute("title") for elem in hrefs]
            #[name_friend for name_friend in list_friends if username_insta in name_friend]
            print(username_insta + 'fotos ' + str(len(list_friends)))
            print(list_friends)
        except Exception as e:
            print(e)
            time.sleep(5)           


    def tag_photos(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/p/"+ hashtag +"/")

        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        
        friends = ["dam", "oh shit", "boss", "king", "oh my god", "jesus"]
        for friend in range(230):
            try:  
                driver.find_element_by_class_name('Ypffh').click()
                input_comment = driver.find_element_by_class_name('Ypffh')
                time.sleep(random.randint(3, 5))
                
                self.person(random.choice(friends), input_comment)
                time.sleep(random.randint(4, 5))
                driver.find_element_by_xpath('//button[contains(text(),"Publicar")]').click()
                time.sleep(5)
            except Exception as e:
                print(e)
                time.sleep(5)

#insta_user = input("Enter a User...:  ")
#insta_pass = input("Enter a pass...:  ")

ganharSorteio = InstagramBot('dalmatica_', 'Estivemega$10')
#ganharSorteio = InstagramBot('threedp.png', 'xErife10')
ganharSorteio.login()