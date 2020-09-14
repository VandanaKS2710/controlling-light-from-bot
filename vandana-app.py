!pip3 install adafruit.io

from Adafruit_IO import RequestError, Client, Feed
from Adafruit_IO import Data
username = 'Vandana_K_S'
code = 'aio_FbID65D3UrGqzg88XGMMaPph9GbQ'
aio = Client(username,code)

!pip install python-telegram-bot

from telegram.ext import Updater,CommandHandler
import requests

def get_url():
  contents = requests.get('https://random.dog/woof.json').json()
  url = contents['url']
  return url

def on(bot2,update):
  url = get_url()
  chat_id = update.message.chat_id
  txt = 'light is turning on'
  pic = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Green_sphere.svg/1024px-Green_sphere.svg.png'
  bot2.send_message(chat_id,txt)
  bot2.send_photo(chat_id,pic)
  value = Data(value=1)
  vale_send = aio.create_data('lit',value)

def off(bot2,update):
  url = get_url()
  chat_id = update.message.chat_id
  txt = 'light is turning off'
  pic = 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Red_sphere_shaded_lightsource_top_right.svg/1024px-Red_sphere_shaded_lightsource_top_right.svg.png'
  bot2.send_message(chat_id,txt)
  bot2.send_photo(chat_id,pic)
  value = Data(value=0)
  value_send = aio.create_data('lit',value)

u = Updater('1389706076:AAEAfeA88tdA0ja8gumBWLERUnCf1siu6lg')
dp = u.dispatcher
dp.add_handler(CommandHandler('on',on))
dp.add_handler(CommandHandler('off',off))
u.start_polling()
u.idle()
