import time
from sys import exit
import html
import datetime
from dateutil.relativedelta import relativedelta
import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from credentials.credentails import PATH, linkedIn_url, linked_email, linked_password


class LinkedInBot:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.bot = webdriver.Chrome(executable_path=PATH)
        self.connectTo = [
            "web", "developer", "full stack", "Machine Learning", "ml", "iot", "software", "devops", "aws",
            "javascript", "react", "angular", "database", "java", "python", "c#", "cloud", "sqa", "frontend",
            "backend", "wordpress", "php", "laravel", ".net core", "vue", "mean stack", "mern", "sql", "flask"
        ]
        self.pagination = []

    def openLinkedIn(self):
        self.bot.get(linkedIn_url)

    def logIn(self):
        try:
            emailField = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            emailField.clear()
            emailField.send_keys(self.email)

            passwordField = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.ID, "password"))
            )
            passwordField.clear()
            passwordField.send_keys(self.password)

            button = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "mercado-button--primary"))
            )
            button.send_keys(Keys.RETURN)
        except:
            print("LinkedIn Login Failed.")

    def openNetwork(self):
        network = WebDriverWait(self.bot, 10).until(
            EC.presence_of_element_located((By.ID, "ember23"))
        )
        network.send_keys(Keys.RETURN)


class LinkedInConnect(LinkedInBot):

    def makeConnections(self):
        last_height = self.bot.execute_script(
            "return document.body.scrollHeight")

        isCheck = False

        while True:
            if isCheck == True:
                break

            self.bot.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

            li = WebDriverWait(self.bot, 10).until(
                EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, "discover-entity-card"))
            )
            for item in li:
                try:
                    gotIt = self.bot.find_element_by_class_name(
                        "ip-fuse-limit-alert__primary-action")
                    if gotIt.text.lower() == "got it":
                        print(
                            "You can't make connections right now, try after some time")
                        isCheck = True
                        self.bot.close()
                        break
                except:
                    buttons = item.find_elements_by_tag_name("button")
                    if len(buttons) == 3:
                        if buttons[2].text == "Connect":
                            occupation = item.find_element_by_class_name(
                                "discover-person-card__occupation").text
                            for tag in self.connectTo:
                                if tag.lower() in occupation.lower():
                                    buttons[2].send_keys(Keys.RETURN)
                                    time.sleep(1)
                                    break

            new_height = self.bot.execute_script(
                "return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height


class WithDrawConnection(LinkedInBot):
    def __init__(self, *arg):
        super(WithDrawConnection, self).__init__(*arg)
        self.connection_date = datetime.date.today()
        while True:
            self.how_old = input(
                "How old connections you wanr to withdraw (e.g 1d, 1w, 1m, 1y): ")
            if re.match("^[1-9][d|w|m|y]", self.how_old):
                break
            else:
                continue

    def openManage(self):
        manage = WebDriverWait(self.bot, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Manage"))
        )
        manage.send_keys(Keys.RETURN)

    def openSent(self):
        sent = WebDriverWait(self.bot, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "artdeco-tablist--no-wrap"))
        )
        button = sent.find_elements_by_tag_name("button")
        button[1].send_keys(Keys.RETURN)

    def findNumbers(self):
        numbers = WebDriverWait(self.bot, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "artdeco-pagination__pages"))
        )
        button = numbers.find_elements_by_tag_name("button")
        return button

    def getPaginationNumbers(self):
        try:
            temp = []
            button = self.findNumbers()
            for btn in button:
                try:
                    integer = int(btn.text)
                    temp.append(integer)
                except:
                    pass
            for number in range(max(temp)):
                self.pagination.append(number+1)
            print(self.pagination)

        except:
            print("There is no Pagination there.")

    def getPrevDate(self, prev_date):
        connection_date = datetime.date.today()
        number = int(prev_date[0])
        if prev_date[1] == 'd':        
            connection_date = connection_date - relativedelta(days=number)
        elif prev_date[1] == 'w':
            connection_date = connection_date - relativedelta(weeks=number)
        elif prev_date[1] == 'm':
            connection_date = connection_date - relativedelta(months=number)
        elif prev_date[1] == 'y':
            connection_date = connection_date - relativedelta(years=number)
        return connection_date

    def openLastPage(self):
        if len(self.pagination) > 0:
            length = len(self.pagination)
            date_by_user = self.getPrevDate(self.how_old)

            for x in range(1, length):
                time.sleep(2)
                button = self.findNumbers()
                page = self.pagination[length - x]

                for btn in button:
                    try:
                        if int(btn.text) == page:
                            btn.send_keys(Keys.RETURN)
                            user_arr = []
                            last_height = self.bot.execute_script(
                                "return document.body.scrollHeight")
                            while True:
                                self.bot.execute_script(
                                    "window.scrollTo(0, document.body.scrollHeight);")
                                time.sleep(2)
                                lst = WebDriverWait(self.bot, 10).until(
                                    EC.presence_of_all_elements_located(
                                        (By.CLASS_NAME, "artdeco-list__item"))
                                )
                                for item in lst:
                                    name = item.find_element_by_class_name(
                                        "invitation-card__title").text
                                    if name not in user_arr:
                                        user_arr.append(name)

                                        duration = item.find_element_by_class_name(
                                            "time-badge").text
                                        html.unescape(duration)
                                        duration_arr = duration.split(" ")
                                        total_dur = duration_arr[0]
                                        if duration_arr[1] == "year" or duration_arr[1] == "years":
                                            total_dur = total_dur + "y"
                                        elif duration_arr[1] == "month" or duration_arr[1] == "months":
                                            total_dur = total_dur + "m"
                                        elif duration_arr[1] == "week" or duration_arr[1] == "weeks":
                                            total_dur = total_dur + "w"
                                        elif duration_arr[1] == "day" or duration_arr[1] == "days":
                                            total_dur = total_dur + "d"
                                        
                                        date_of_user = self.getPrevDate(total_dur)
                                        if date_of_user <= date_by_user:
                                            withdraw = item.find_element_by_class_name("invitation-card__action-container")
                                            print(name, withdraw.text)
                                            withdraw.send_keys(keys.RETURN)
                                            # confirm = WebDriverWait(self.bot, 10).until(
                                            #     EC.presence_of_all_elements_located((By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn"))
                                            # )
                                            # confirm[1].send_keys(Keys.RETURN)
                                        time.sleep(2)
                                new_height = self.bot.execute_script(
                                    "return document.body.scrollHeight")
                                if new_height == last_height:
                                    break
                                last_height = new_height

                            time.sleep(3)
                            break
                    except:
                        pass