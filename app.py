from sys import exit
import os
import time

from bot.facebook_bot import FaceBookBot
from bot.linkedIn_bot import LinkedInConnect, WithDrawConnection
from bot.instagram_bot import FollowSuggestions, UnFollowUsers
from bot.fiverr_bot import FiverrBot

from credentials.credentails import PATH, facebook_email, facebook_password, linked_email, linked_password, instagram_email, instagram_password


if __name__ == "__main__":
    os.system('color f0')
    print("-------------------------------------------------------------")
    print("                 WELCOME TO SOCIAL BOTS                      ")
    print("-------------------------------------------------------------")
    print("Please Select from the following Social Media Platforms".upper())
    print("1. Facebook")
    print("2. LinkedIn")
    print("3. Instagram")
    print("4. Fiverr")
    print("5. Quit Program")
    print("Note: Make sure screen size of browser is full.")
    print("\n")

    while True:
        social_input = input("Please enter the number (1 to 4): ")

        try:
            number = int(social_input)
        except:
            os.system('color 4f')
            print("Please Enter a valid input b/w 1 to 4!!")
            time.sleep(1)
            os.system('color f0')
            continue

        if int(social_input) == 1:
            print("-------------------------------------------------------------")
            print("Please Select the option.".upper())
            print("1. Sending Friend Requests")
            print("\n")

            facebook_input = input("Please enter the number: ")

            if int(facebook_input) == 1:
                facebook_bot = FaceBookBot(facebook_email, facebook_password)
                facebook_bot.openFacebook()
                name = facebook_bot.nameInput()
                facebook_bot.logIn()
                time.sleep(5)
                facebook_bot.search(name)
                facebook_bot.sendingRequest()

            else:
                os.system('color 4f')
                print(
                    "Selected Option is invalid. Again Select from Facebook, Instagram and LinkedIn Option.\n")
                time.sleep(1)
                os.system('color f0')
                continue

        if int(social_input) == 2:
            print("-------------------------------------------------------------")
            print("Please Select the option.".upper())
            print("1. Make Connections of your Field.")
            print("2. WithDrawn the old sended connections.")
            print("\n")
            linkedin_input = input("Please enter the number: ")

            if int(linkedin_input) == 1:
                linkedin_connect = LinkedInConnect(
                    linked_email, linked_password)
                linkedin_connect.openLinkedIn()
                linkedin_connect.logIn()
                linkedin_connect.openNetwork()
                linkedin_connect.makeConnections()

            if int(linkedin_input) == 2:
                linkedin_withdrawn = WithDrawConnection(
                    linked_email, linked_password)
                linkedin_withdrawn.openLinkedIn()
                linkedin_withdrawn.logIn()
                linkedin_withdrawn.openNetwork()
                linkedin_withdrawn.openManage()
                linkedin_withdrawn.openSent()
                linkedin_withdrawn.getPaginationNumbers()
                linkedin_withdrawn.openLastPage()

            else:
                os.system('color 4f')
                print(
                    "Selected Option is invalid. Again Select from Facebook, Instagram and LinkedIn Option.\n")
                time.sleep(1)
                os.system('color f0')
                continue

        if int(social_input) == 3:
            print("-------------------------------------------------------------")
            print("Please Select the option.".upper())
            print("1. Follow the Users")
            print("2. UnFollow those Users WHo did not follow you.")
            print("\n")
            instagram_input = input("Please enter the number: ")

            if int(instagram_input) == 1:
                instagram_bot = FollowSuggestions(
                    instagram_email, instagram_password)
                instagram_bot.openInstagram()
                instagram_bot.logIn()
                instagram_bot.turnOffNotification()
                instagram_bot.seeAllSuggestions()
                instagram_bot.FollowUsers()

            if int(instagram_input) == 2:
                unfollow_user = UnFollowUsers(
                    instagram_email, instagram_password)
                unfollow_user.openInstagram()
                unfollow_user.logIn()
                unfollow_user.turnOffNotification()
                unfollow_user.openProfile()
                unfollow_user.getFollowers()
                unfollow_user.unfollowUsers()
            else:
                os.system('color 4f')
                print(
                    "Selected Option is invalid. Again Select from Facebook, Instagram and LinkedIn Option.\n")
                time.sleep(1)
                os.system('color f0')
                continue

        if int(social_input) == 4:
            fiverr_bot = FiverrBot()
            fiverr_bot.openFiverr()
            fiverr_bot.search()
            fiverr_bot.suggestedTags()
            fiverr_bot.openGigs()

        if int(social_input) == 5:
            os.system('color 07')
            exit(0)

        elif int(social_input) > 4 or int(social_input) < 0:
            os.system('color 4f')
            print("Please Enter a valid input b/w 1 to 4!!")
            time.sleep(1)
            os.system('color f0')
