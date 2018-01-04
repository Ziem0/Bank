import getpass
import os, sys

class UI:
    
    menu = ['Bank', 'Director', 'Employee', 'Customer', 'Exit']
    title1 = '\nWelcome! Log as: \n\n'

    @staticmethod
    def print(it):
        print(it)
    
    @staticmethod
    def clear():
        os.system('clear')
    
    @staticmethod
    def pause():
        input('Press ENTER..')

    @staticmethod
    def create_menu(title, menu):
        for n,option in enumerate(menu,1):
            title += '{}.{}\n'.format(n, option)
        return title

    @staticmethod
    def user_choice(menu):
        user = 0
        while user < 1 or user > len(menu):
            try:
                user = int(input('choose option: '))
            except ValueError:
                print('Choose number!')
        return user

    @staticmethod
    def login_inputs():
        name = input('Type your name: ')
        password = getpass.getpass('Please enter your password: ')
        return name, password