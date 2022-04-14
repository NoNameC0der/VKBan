import requests
import vk_api
import os
import time
from colorama import Fore, Back, Style 
def vkban():
    os.system("clear")
    intro = '''
\033[32m\033[01m
╔╗╔╗╔╗╔══╗╔══╗─╔══╗╔╗─╔╗
║║║║║║║╔═╝║╔╗║─║╔╗║║╚═╝║
║║║║║╚╝║──║╚╝╚╗║╚╝║║╔╗─║
║╚╝║║╔╗║──║╔═╗║║╔╗║║║╚╗║
╚╗╔╝║║║╚═╗║╚═╝║║║║║║║─║║
─╚╝─╚╝╚══╝╚═══╝╚╝╚╝╚╝─╚╝
\033[0m
      .:EvenSpon Studio:.
'''
    print(Fore.RED + "\033[1m" + intro)
    print(Fore.WHITE + """                                  
[1] WALL-POST-BAN                        
[2] DEVOLOPERS                          
[3] EXIT                                 


    """)
    a = input("[Enter number] -> ")
    if a == "1":
        try:
            tok = input("[ACCESS-TOKEN] -> ") 
            token = vk_api.VkApi(token = tok) 
            vk = token.get_api()
            for var in range(5):
                time.sleep(3)
                vk.wall.post(message='#СинийКит #ЯСова')             
                print(Fore.BLACK + Back.GREEN + "[log] Сообщение отправленно. Ожидайте бана!")
            print(Back.BLACK + Fore.WHITE)
            os.system("clear")
            vkban()
        except Exception as er:
            print('Невалидный токен или страница в бане')
            vkban()
    if a == "2":
        print("""                                  
 DEVOLOPERS                               
 TELEGRAM: @evensponstudio                              
 Для выхода в главное меню нажмите Enter   

        """)
        c = input("-> : ")
        if c == "1":
            os.system("clear")
            vkban()
        else:
            os.system("clear")
            vkban()
    if a == "3":
        os.system("exit")
    else:
        vkban()
vkban()
