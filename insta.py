from instabot import Bot
import os 
import glob
from datetime import datetime
import time
from os import remove

#openpyxl can be used here to optimize this

captn = ['zero'
,'I believe in God, only I spell it Nature. —Frank Lloyd Wright'
,'Forget not that the earth delights to feel your bare feet and the winds long to play with your hair. —Khalil Gibran'
,'Look deep into nature, and then you will understand everything better. —Albert Einstein'
,'Heaven is under our feet as well as over our heads. —Henry David Thoreau'
,'To me a lush carpet of pine needles or spongy grass is more welcome than the most luxurious Persian rug. —Helen Keller'
,'We don’t inherit the earth from our ancestors, we borrow it from our children. —Native American proverb'
,'In nature, nothing is perfect and everything is perfect. Trees can be contorted, bent in weird ways, and they’re still beautiful. –Alice Walker'
,'Choose only one master—nature. —Rembrandt'
,'Nature does not hurry, yet everything is accomplished. —Lao Tzu'
,'If you truly love nature, you will find beauty everywhere. —Laura Ingalls Wilder'
,'There is something infinitely healing in the repeated refrains of nature—the assurance that dawn comes after night, and spring after winter. —Rachel Carson'
,'Leave the road, take the trails. —Pythagoras'
,'Live in each season as it passes; breathe the air, drink the drink, taste the fruit, and resign yourself to the influence of the earth. —Henry David Thoreau'
,' I go to nature to be soothed and healed, and to have my senses put in order. —John Burroughs'
,'There’s a whole world out there, right outside your window. You’d be a fool to miss it. —Charlotte Eriksson'
,'To forget how to dig the earth and to tend the soil is to forget ourselves. —Mahatma Gandhi'
]

today = datetime.today()
i = today.day

def upload_photo():
    bot = Bot()
    #cookie_del = glob.glob("config/*cookie.json")
    #os.remove(cookie_del[0])
    remove('C:\R A J A S\Learn\InstaBot\config\jungli_engineer_uuid_and_cookie.json')
    time.sleep(2)

    bot.login(username = "id", password = "password")
    time.sleep(5)
    bot.upload_photo(str(i)+'.jpg',caption= captn[i])
    

#if i%2 != 0:  alternate days
while True:
    upload_photo()
    


