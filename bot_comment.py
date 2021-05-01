from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

func_actions = {'like_photo': '//section/span [@class="fr66n"]', 'public_comment': '//button[contains(text(),"Publicar")]', 'go_login': '//a [@href="/accounts/login/?source=auth_switcher"]', 'input_username': '//input [@name="username"]', 'input_password': '//input [@name="password"]', 'scrolling_page': 'window.scrollTo(0, document.body.scrollHeight);', 'scrolling_modal': 'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight' }

waiting_time = {'pg_loading': 3, 'scroll_time': 4, 'action_start': 30, 'action_end': 40}

class InstagramBot:
    # Função para receber usuario e senha.
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r"E:\ESTUDOS\CURSOS\PYTHON\livroexe\bot_coment\geckodriver.exe")
    
    @staticmethod # Para digitar como uma pessoa
    def like_person(phrase, loc):
        for word in phrase:
            loc.send_keys(word)
            time.sleep(random.randint(1,5)/30) # tempo para digitar cada letra.
    
    # Função encontrar o elemento input (clicar, inserir a informação e retuonar a posição).
    def input_inserty(self, name_element, input_text, driver):
        input_data = driver.find_element_by_xpath(func_actions[name_element])
        input_data.click()
        input_data.clear()
        input_data.send_keys(input_text)
        return input_data

    def ref_list(self, tag_named, elem_get):
        driver = self.driver
        elem_push = driver.find_elements_by_tag_name(tag_named)
        elem_list = [elem.get_attribute(elem_get) for elem in elem_push]
        print(elem_list)
        return elem_list

    def scrolling_body(self, start, end, driver, parameter):
        for i in range(start, end):
            driver.execute_script(parameter)
            time.sleep(waiting_time['scroll_time'])

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(waiting_time['pg_loading'])
        
        while True:
            try:
                press_enter = self.input_inserty('input_username', self.username, driver)
                press_enter = self.input_inserty('input_password', self.password, driver)
                break
            except Exception as e:
                print(e)
                # Go to login pagein
                bottom_lg = driver.find_element_by_xpath(func_actions['go_login'])
                bottom_lg.click()
                time.sleep(waiting_time['pg_loading'])
                continue
        press_enter.send_keys(Keys.RETURN)
        time.sleep(waiting_time['pg_loading'])
        
        # Componentes de starts
        #self.get_friends()
        #self.tag_photos('cakes')
    
    def get_friends(self):
        driver = self.driver
        driver.get("https://www.instagram.com/"+ self.username +"/")

        try:
            name_text = "//li[3]/a [@href='/"+ self.username +"/following/']"
            following_bt = driver.find_element_by_xpath(name_text)
            following_bt.click()
            time.sleep(2)

            opened_window = driver.find_element_by_xpath('//div [@class="isgrP"]')
            while True:
                driver.execute_script(func_actions['scrolling_modal'], opened_window)
                break
            
            list_friends = self.ref_list('a', 'title')
            list_friends.sort(reverse=True)
            print(list_friends)

        except Exception as e:
            print(e)
            time.sleep(5)

    def tag_photos(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/"+ hashtag +"/")
        
        self.scrolling_body(1, 5, driver, func_actions['scrolling_page'])
        pic_hrefs = self.ref_list('a', 'href')

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script(func_actions['scrolling_page'])
            
            try:
                comments_list = ["Que capricho! amei", "Que capricho", "Você arrasa!", "Que obra de arte!", "Um mimo!", "Que trabalho delicado uma obra de arte.", "Maravilhoso!", "Dá pra sentir o gosto só de ver!", "Arrasou como sempre!", "Uauuu, tá mega maravilhoso." ]
                
                time.sleep(random.randint(3, 5))
                like_bt = driver.find_element_by_xpath(func_actions['like_photo'])
                like_bt.click()
                time.sleep(random.randint(waiting_time['action_start'], waiting_time['action_end']))
                
                driver.find_element_by_class_name('Ypffh').click()
                input_comment = driver.find_element_by_class_name('Ypffh')
                
                self.like_person(random.choice(comments_list), input_comment)
                time.sleep(random.randint(waiting_time['action_start'], waiting_time['action_end']))
                
                driver.find_element_by_xpath(func_actions['public_comment']).click()
                time.sleep(waiting_time['pg_loading'])

            except Exception as e:
                print(e)
                time.sleep(waiting_time['pg_loading'])

if __name__ == "__main__":

    insta_user = 'marddocuras' #input("Enter a User...:  ")
    insta_pass = 'Estivemega$10' #input("Enter a pass...:  ")

    ganharSorteio = InstagramBot(insta_user, insta_pass)
    ganharSorteio.login()