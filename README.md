# RaspyBot
A Telegram Bot that runs in a raspberry-pi and displays the messages that recive in a LCD display. Uses libs Adafuit for LCD and pyTelegramBotAPI by eternoir for Telegram

1) Install telebot lib for python https://github.com/eternnoir/pyTelegramBotAPI

2) Edit the line 56 in Adafuit_CharLCD.py   

def __init__(self, pin_rs=?, pin_e=?, pins_db=[?, ?, ?, ?], GPIO=None):  

replace "?" for your GPIO numbers.
where pins_db = Datapins

3) Put the <TOKEN> of your bot in raspybot.py (line 9) 

4) Launch raspybot.py :)
