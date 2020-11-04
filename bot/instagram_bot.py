import time
from sys import exit

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from credentials.credentails import PATH, instagram_url, instagram_email, instagram_password


class InstagramBot:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.bot = webdriver.Chrome(executable_path=PATH)
        self.notFollow = [".com", ".pk", "official", ".ai", ".sac",
                          "_sultan_e_meme_", "foryou", "pk", ".sk",
                          "designer", "uet", "text", "creative", ".girl",
                          "gre", "run", "erotic", "eroticbutts", "online", "art", "sexy"]
        self.followers = []

    def openInstagram(self):
        self.bot.get(instagram_url)

    def logIn(self):
        try:
            emailField = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )

            emailField.clear()
            emailField.send_keys(self.email)

            passwordField = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            passwordField.clear()
            passwordField.send_keys(self.password)

            button = WebDriverWait(self.bot, 10).until(
                EC.presence_of_all_elements_located(
                    (By.TAG_NAME, "button"))
            )
            for btn in button:
                if btn.text == "Log In":
                    btn.send_keys(Keys.RETURN)
        except:
            print("Instagram Login Failed.")

    def turnOffNotification(self):
        time.sleep(3)
        turnOff = WebDriverWait(self.bot, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
        for item in turnOff:
            if item.text == "Not Now":
                item.send_keys(Keys.RETURN)


class FollowSuggestions(InstagramBot):
    def seeAllSuggestions(self):
        seeAll = WebDriverWait(self.bot, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "See All"))
        )
        seeAll.send_keys(Keys.RETURN)

    def FollowUsers(self):
        last_height = self.bot.execute_script(
            "return document.body.scrollHeight")
        while True:
            self.bot.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            user = WebDriverWait(self.bot, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "XfCBB")))
            for item in user:
                isCheck = False
                name = item.find_element_by_class_name("notranslate").text
                for check in self.notFollow:
                    if check.lower() in name.lower():
                        isCheck = True
                        break
                if isCheck == False:
                    follow = item.find_element_by_tag_name("button")
                    if follow.text == "Follow":
                        follow.send_keys(Keys.RETURN)
                        time.sleep(2)
                        if follow.text == "Follow":
                            self.bot.quit()

            new_height = self.bot.execute_script(
                "return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height


class UnFollowUsers(InstagramBot):
    def openProfile(self):
        try:
            username = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "gmFkV"))
            )
            self.bot.get(f'https://www.instagram.com/{username.text}')
        except:
            self.bot.get("https://www.instagram.com/usmanali_456")

    def openSpecificLink(self, link_name):
        links = WebDriverWait(self.bot, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "-nal3 "))
        )
        for item in links:
            if link_name in item.text:
                item.send_keys(Keys.RETURN)

    def getFollowers(self):
        self.openSpecificLink("followers")

        time.sleep(3)
        last_height = self.bot.execute_script(
            "return document.getElementsByClassName('isgrP')[0].scrollHeight")
        while True:
            self.bot.execute_script(
                "document.getElementsByClassName('isgrP')[0].scrollTo(0, document.getElementsByClassName('isgrP')[0].scrollHeight);")
            time.sleep(2)
            names = WebDriverWait(self.bot, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "MqpiF"))
            )

            for item in names:
                if item.text not in self.followers:
                    self.followers.append(item.text)

            new_height = self.bot.execute_script(
                "return document.getElementsByClassName('isgrP')[0].scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        
    def unfollowUsers(self):
        if len(self.followers) > 0:
            self.openSpecificLink("following")
            time.sleep(2)
            last_height = self.bot.execute_script(
                "return document.getElementsByClassName('isgrP')[0].scrollHeight")
            while True:
                self.bot.execute_script(
                    "document.getElementsByClassName('isgrP')[0].scrollTo(0, document.getElementsByClassName('isgrP')[0].scrollHeight);")
                time.sleep(2)
                
                li = WebDriverWait(self.bot, 10).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, "wo9IH"))
                )
                for item in li:
                    name = item.find_element_by_class_name("MqpiF")
                    if name.text not in self.followers:
                        button = item.find_element_by_tag_name("button")
                        if button.text == "Following":
                            button.send_keys(Keys.RETURN)
                            confirm = WebDriverWait(self.bot, 10).until(
                                EC.presence_of_element_located((By.CLASS_NAME, "-Cab_"))
                            )
                            confirm.send_keys(Keys.RETURN)
                            time.sleep(10)

                new_height = self.bot.execute_script(
                    "return document.getElementsByClassName('isgrP')[0].scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height

