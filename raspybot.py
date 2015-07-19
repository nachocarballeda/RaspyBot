#!/usr/bin/python 

import urllib3
import unicodedata
import telebot
import os
import time
import token
from Adafruit_CharLCD import Adafruit_CharLCD

TOKEN = token.TOKEN

def ascii_ignore(text):
	return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')
	

def listener(messages):
	for m in messages:
		#tb.reply_to(m, "queee?") #responde quoteando
		chatid = m.chat.id
		if m.content_type == 'text':
			text = ascii_ignore(m.text)
			with open("/home/pi/bots/message.log","a") as log:
				log.write("Username: " + m.chat.username + " At {0}:{1}:{2} , day {3}/{4}/{5}".format(time.localtime()[3],time.localtime()[4],time.localtime()[5],time.localtime()[2],time.localtime()[1],time.localtime()[0]) + "\n" + text[:50] + "\n\n")
			text_to_lcd = text + '\n'  + m.chat.username
			text_to_user = "El mensaje: " + text[:16] + '\n' + "fue enviado con exito !"
			text_to_user2 = "El mensaje: " + text[:16] + '\n' + "se trunco a 16 caracteres  pero fue enviado :)"
			if text == '/temperature':
				tb.send_message(chatid,"La temperatura en la pi es de "+ get_temperature() + " grados centigrados." ) 
			elif text == '/photo':
				take_and_send_photo(chatid)
			elif text == '/log':
				with  open("/home/pi/bots/message.log","rb") as log:
					tb.send_document(chatid,log)
			elif text == '/getcode':
				with  open("/home/pi/bots/raspybot.py","rb") as code:
					tb.send_document(chatid,code)
			else:
				
				with open("/home/pi/bots/lastmessage.log","w") as log:
					log.write(text[:16] + "\n"+ m.chat.username )
				if len(text)>16:
					tb.send_message(chatid,text_to_user2)
				else:
					tb.send_message(chatid,text_to_user)
				to_lcd(text_to_lcd)

def get_temperature():
	with open("/sys/class/thermal/thermal_zone0/temp") as f:
		temp = str(int(f.read())/1000)
	return temp

def take_and_send_photo(chat_id):
	os.system('fswebcam -r 360x296 --jpeg 85 -D 1 /home/pi/bots/photo.jpg')
	with open('/home/pi/bots/photo.jpg', 'rb') as photo:
		tb.send_photo(chat_id, photo)

def to_lcd(text):
	lcd.clear()
	lcd.message(text)
	

if __name__=='__main__':
	lcd=Adafruit_CharLCD()
	lcd.clear()
	with open("/home/pi/bots/lastmessage.log","r") as log:
		lcd.message(log.read())
	tb = telebot.TeleBot(TOKEN)
	tb.set_update_listener(listener) 
	tb.polling()

	while True:
		time.sleep(0.5)
