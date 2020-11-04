import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from credentials.credentails import PATH, facebook_url


class FaceBookBot:
    def __init__(self, email, password):
        self.email = email
        self.password = password

        option = Options()
        # option.add_argument("--disable-infobars")
        # option.add_argument("start-maximized")
        # option.add_argument("--disable-extensions")
        option.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })
        self.bot = webdriver.Chrome(
            chrome_options=option, executable_path=PATH)
        self.friendList = [
            "web", "developer", "full stack", "Machine Learning", "ml", "iot", "software", "devops", "aws",
            "javascript", "react", "angular", "database", "java", "python", "c#", "cloud", "sqa", "frontend",
            "backend", "wordpress", "php", "laravel", ".net core", "vue", "freelance", "freelancer"
        ]

    def nameInput(self):
        name = input("Please the enter the Name: ")
        return name

    def openFacebook(self):
        self.bot.get(facebook_url)

    def logIn(self):
        try:
            emailField = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.ID, "email"))
            )
            emailField.clear()
            emailField.send_keys(self.email)

            passwordField = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.ID, "pass"))
            )
            passwordField.clear()
            passwordField.send_keys(self.password)

            try:
                button = WebDriverWait(self.bot, 10).until(
                    EC.presence_of_element_located((By.NAME, "login"))
                )
                button.send_keys(Keys.RETURN)
            except:
                logIn = WebDriverWait(self.bot, 10).until(
                    EC.presence_of_element_located((By.ID, "loginbutton"))
                )
                logIn.send_keys(Keys.RETURN)
        except:
            print("Facebook Login Failed.")

    def search(self, name):
        searchField = WebDriverWait(self.bot, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        searchField.clear()
        searchField.send_keys(name)
        time.sleep(2)
        searchField.send_keys(Keys.RETURN)

        people = WebDriverWait(self.bot, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "People"))
        )
        people.send_keys(Keys.RETURN)

    def sendingRequest(self):
        time.sleep(3)
        last_height = self.bot.execute_script(
            "return document.body.scrollHeight;")
        i = 0
        print("PROGRESS")
        while True:

            self.bot.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

            mainDiv = WebDriverWait(self.bot, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "_4p2o"))
            )

            for item in mainDiv:
                work = item.find_element_by_class_name("_glm").text
                for tag in self.friendList:
                    if tag.lower() in work.lower():
                        try:
                            addFreind = item.find_element_by_class_name(
                                "FriendRequestAdd")
                            addFreind.send_keys(Keys.RETURN)
                            i += 1
                            print(f'{i}\r', end="")
                            try:
                                confirm = WebDriverWait(self.bot, 10).until(
                                    EC.presence_of_element_located(
                                        (By.CLASS_NAME, "layerConfirm"))
                                )
                                confirm.send_keys(Keys.RETURN)
                            except:
                                pass
                            break
                        except:
                            break
                try:
                    close = WebDriverWait(self.bot, 1).until(
                        EC.presence_of_all_elements_located(
                            (By.CLASS_NAME, "layerCancel"))
                    )
                    for item in close:
                        if item.text == "Close":
                            item.send_keys(Keys.RETURN)
                            i -= 1
                            print(f'{i}\r', end="")
                except:
                    pass

            new_height = self.bot.execute_script(
                "return document.body.scrollHeight")
            if new_height == last_height:
                print("Break due to height.")
                break
            if i == 100:
                print("Break due to limit exceed.")
                break
            last_height = new_height

    def quit(self):
        self.bot.quit()
        self.bot.close()
