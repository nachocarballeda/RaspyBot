#!/usr/bin/python

import telebot 
import os
import time
from Adafruit_CharLCD import Adafruit_CharLCD


TOKEN = '<TOKEN_STRING_HERE>' 

def listener(messages):
	for m in messages:
		chatid = m.chat.id
		if m.content_type == 'text':
			text = m.text
			text_to_lcd = text + '\n' + m.chat.username
			text_to_user = "El mensaje: " + text + '\n' + "fue enviado con exito !"
			if len(text)>16:
				tb.send_message(chatid,"Lo siento el mensaje es muy largo, por ahora solo 16 chars ;)")
			else:
				tb.send_message(chatid,text_to_user) 
				to_lcd(text_to_lcd)

def to_lcd(text):
	lcd.clear()
	lcd.message(text)
	

if __name__=='__main__':
	lcd=Adafruit_CharLCD()
	lcd.clear()
	tb = telebot.TeleBot(TOKEN)
	tb.set_update_listener(listener) 
	tb.polling()

	while True:
		time.sleep(0.5)
		pass
