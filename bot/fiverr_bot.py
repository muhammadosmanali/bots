import time
import keyboard

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from credentials.credentails import PATH


class FiverrBot:
    def __init__(self):
        self.bot = webdriver.Chrome(PATH)
        self.suggested_tags_list = []

    def openFiverr(self):
        self.bot.get("https://www.fiverr.com/?force_buying_nav")
        print("Press Any Key After Solving Captcha: ")
        if keyboard.is_pressed('q'):
            pass
        else:
            pass

    def search(self):
        search = input("Enter the Word To Search: ")

        search_header = WebDriverWait(self.bot, 10).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "search-bar-package"))
        )
        search_input = search_header[1].find_element_by_tag_name("input")
        search_input.send_keys(search)

        search_button = search_header[1].find_element_by_tag_name("button")
        search_button.send_keys(Keys.RETURN)

    def suggestedTags(self):
        suggested_tags = WebDriverWait(self.bot, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "related-search"))
        )
        suggested_tags_links = suggested_tags.find_elements_by_tag_name("a")
        for tags in suggested_tags_links:
            self.suggested_tags_list.append(tags.text)
        print(self.suggested_tags_list)

    def openGigs(self):
        gigs_list = WebDriverWait(self.bot, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "gig-card-layout"))
        )

        for gigs in gigs_list:
            gig_link = gigs.find_elements_by_tag_name("a")
            gig_link[0].send_keys(Keys.RETURN)
            time.sleep(3)
            self.bot.switch_to_window(self.bot.window_handles([1]))

            