from telegram.ext import Updater, MessageHandler,Filters

from Adafruit_IO import Client
import os

aio = Client('nostalgicboy22',os.getenv('nostalgicboy22'))
             
def demo1(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://image.shutterstock.com/image-vector/ok-hand-lettering-handmade-calligraphy-260nw-669965602.jpg'
  bot.message.reply_text('I am fine')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def demo2(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://ak.picdn.net/shutterstock/videos/1036409747/thumb/1.jpg'
  bot.message.reply_text('LIGHT is turned ON')
  aio.send('light', 1)
  data1 = aio.receive('light')
  print(f'Received value: {data1.value}')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def demo3(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://ak.picdn.net/shutterstock/videos/16051507/thumb/1.jpg'
  bot.message.reply_text('LIGHT is turned OFF')
  aio.send('light', 0)
  data1 = aio.receive('light')
  print(f'Received value: {data1.value}')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def demo4(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://cdn.imgbin.com/4/14/11/imgbin-fan-cartoon-green-simple-fan-decoration-pattern-wb2X4GAMBapYZ5w3Te8g1bknd.jpg'
  bot.message.reply_text('FAN is turned ON')
  aio.send('fan', 1)
  data2 = aio.receive('fan')
  print(f'Received value: {data2.value}')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def demo5(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://previews.123rf.com/images/tawesit/tawesit1601/tawesit160100054/50820091-house-item-electric-fan-cartoon.jpg'
  bot.message.reply_text('FAN is turned OFF')
  aio.send('fan', 0)
  data2 = aio.receive('fan')
  print(f'Received value: {data2.value}')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def main(bot,update):
  a = bot.message.text.lower()
  print(a)

  if a == "how are you?":
    demo1(bot,update)
  elif a =="light on" or a=="turn on light":
    demo2(bot,update)
  elif a =="light off" or a=="turn off light":
    demo3(bot,update)
  elif a =="switch on the fan" or a=="turn on fan":
    demo4(bot,update)
  elif a =="switch of the fan" or a=="turn off fan":
    demo5(bot,update)
  else:
    bot.message.reply_text('Invalid Text')
BOT_TOKEN = os.getenv('BOT_TOKEN')
u = Updater(BOT_TOKEN,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
