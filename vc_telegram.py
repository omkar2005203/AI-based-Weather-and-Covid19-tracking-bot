#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple Bot to reply to Telegram messages.
This is built on the API wrapper, see echobot2.py to see the same example built
on the telegram.ext bot framework.
This program is dedicated to the public domain under the CC0 license.
"""

## Telegram Imports
#import telegram
import json
from telegram.error import NetworkError, Unauthorized
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
#======================================================================
# Python Imports
import logging
import re 
import sys, os, subprocess
#import secrets
from datetime import datetime
from time import sleep
#import sqlite3 as sql3	
import pandas as pd
import tensorflow as tf
import numpy as np
import requests
import json
json_nan = json.dumps(float('nan'))
import logging
#import socket
import telegram
import config
from telegram.ext import CommandHandler, Updater
json.loads(json_nan)

import regulexp as t
import test 
import logging
logging.getLogger('tensorflow').disabled = True
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf

# Rasa imports
from rasa.nlu.training_data import load_data
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.model import Trainer
from rasa.nlu.model import Metadata, Interpreter
from rasa.nlu import config
from rasa.nlu.training_data import load_data
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.model import Trainer
from rasa.nlu.model import Metadata, Interpreter
from rasa.nlu import config
import warnings
warnings.filterwarnings('ignore')
#==================================================================================#

import covid19test as d
import config  as f
#print(invlist)
# to remove None values in list 

if os.name == "nt":
	subprocess.run("chcp 65001", shell=True)
	
#======================================================================
# Wit Imports
from wit import Wit
#======================================================================
# In-Project Imports

import globalConfigs as c
import warnings
warnings.filterwarnings('ignore')
#======================================================================

## For WeatherOpen Api
import pyowm
owm = pyowm.OWM(c.api)

##---------------------------------------------------------------------
## Initialization 
update_id = None
degree_sign = u'\N{DEGREE SIGN}'
## Functions

def TelegramMain():
	"""Run the bot."""
	global update_id
	# Telegram Bot Authorization Token
	bot = telegram.Bot(c.botToken)

	# get the first pending update_id, this is so we can skip over it in case
	# we get an "Unauthorized" exception.
	try:
		update_id = bot.get_updates()[0].update_id
	except IndexError:
		update_id = None

	logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

	while True:
		try:
			response(bot)
		except NetworkError:
			sleep(1)
		except Unauthorized:
			# The user has removed or blocked the bot.
			update_id += 1
		
def log(message):
	print(str(message) + "\n")
	sys.stdout.flush()

def response(bot):
	"""
	Main Bot response function, that binds all the codes and functions written above. 
	Uses the Telegram bot API to access the chats as updates and prepares a curated response for all these chats
	"""
	global update_id
	global chatID 
	

	for update in bot.get_updates(offset=update_id, timeout=10):

			
			#print(update)
			
			update_id = update.update_id + 1

			#print(update_id)

			#print(update['callback_query'])

		

			if update.message:
				chatID = update.message.chat.id
				#print(update)
				#print(chatID)
				try:
					phone = update.message.contact.phone_number

					# if update.message.chat.id in f.CHATIDLIST:
					# 	ip_list = socket.gethostbyname_ex(socket.gethostname())
					# 	bot.send_message(chat_id=update.message.chat.id, text=f'Hostname: {ip_list[0]}')
					# 	for number,ip in enumerate(ip_list[2]):
					# 		msg = f'IP #{number + 1} - {ip}'
					# 		print(msg)
					# 		bot.send_message(chat_id=update.message.chat.id, text=msg)
					#print('Mobile Number is:',phone)
				# 	response = UpdateUser(chatID, phone)
				# 	if response:
				# 		bot.send_message(chat_id=chatID, text = "Welcome")
				# 	else:
				# 		bot.send_message(chat_id=chatID, text = "Welcome")
					
				except AttributeError:
					pass
				# 	if not checkUser(chatID):
				# 		contact_keyboard = telegram.KeyboardButton(text="I Agree", request_contact=True)
				# 		custom_keyboard = [[contact_keyboard]]
				# 		reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard, one_time_keyboard=True)
				# 		# bot.send_message(chat_id = chatID, text="Accept disclaimer")
				# 		bot.send_message(chat_id=chatID, text = "Accept disclaimer", reply_markup = reply_markup)
				# 	else:
				# 		with open("AdminData.json", "r") as r:
				# 			AdminData = json.load(r)
				# 			phone = AdminData["chatid-user"][str(chatID)]
				# 			vcode = AdminData["phone-user"][phone]

						#bot.send_message(chat_id=chatID, text = "Your Vendor Code is " + vcode)
				query = update.message.text
						# var = test.run_nlu(query,'project/models/nlu')
						# print (var) # prints entities and intent part
					
				interpreter = Interpreter.load('trained/models/nlu')
				var=interpreter.parse(query)
										
				intent1=var['intent']['name']

						# exception handling incase if there no invoices
				try:
					entity1=var['entities'][0]['value']
					#print("Entities:",entity1)

				except IndexError as e:
							print("No entity found")
							print(e)

				first_name=update.message.chat.first_name

				chatID = update.message.chat.id

                         # getting intents
				#print("Intent:",intent1)


				if intent1 == 'greet':
					bot.send_message(chat_id=chatID, text = "hello"+"\t"+first_name+"\t"+"!")
					# res = requests.get('https://ipinfo.io/')
					# data = res.json()
					# print(data)
				elif update.message.text == '/start':
					bot.send_message(chat_id=chatID, text = "Welcome to WeatherBot ! - Crafted by Omkar Rane")

				elif intent1 == 'endchat':
					bot.send_message(chat_id=chatID, text = "Bye ! Have a nice day."+"!")

				elif intent1 == 'location':
					try:
						try:
							txt = update.message.text
							print(txt)
							observation = owm.weather_at_place(txt)
							weather = observation.get_weather()
							wind = weather.get_wind()['speed']
							humidity= weather.get_humidity()
							temperature = weather.get_temperature('celsius')['temp']
							status = weather.get_detailed_status()
							bot.send_message(chat_id=chatID, text = "Weather details of"+" "+ txt +" "+"is as follows:")
							bot.send_message(chat_id=chatID, text = "Temperature:"+" "+str(temperature)+degree_sign)
							bot.send_message(chat_id=chatID, text = "Wind:"+" "+str(wind)+"Km/hr")
							bot.send_message(chat_id=chatID, text = "humidity:"+" "+str(humidity)+"%")
							bot.send_message(chat_id=chatID, text = "sky:"+" "+str(status))
								 
						except pyowm.exceptions.api_response_error.NotFoundError:
							 bot.send_message(chat_id=chatID, text = "location not found !")

					except pyowm.exceptions.api_call_error.APICallTimeoutError:
						bot.send_message(chat_id=chatID, text = "Dont mess with bot !")
						bot.send_message(chat_id=chatID, text = "Enter your appropriate location !")
					
				elif intent1 == 'ask_weather':
					try:
						try:
							try:
									observation = owm.weather_at_place(entity1)
									weather = observation.get_weather()
									wind = weather.get_wind()['speed']
									humidity= weather.get_humidity()
									temperature = weather.get_temperature('celsius')['temp']
									status = weather.get_detailed_status()
									bot.send_message(chat_id=chatID, text = "Weather details of"+" "+ entity1 +" "+"is as follows:")
									bot.send_message(chat_id=chatID, text = "Temperature:"+" "+str(temperature)+degree_sign)
									bot.send_message(chat_id=chatID, text = "Wind:"+" "+str(wind)+"Km/hr")
									bot.send_message(chat_id=chatID, text = "humidity:"+" "+str(humidity)+"%")
									bot.send_message(chat_id=chatID, text = "sky:"+" "+str(status))
									
							except UnboundLocalError as e:
								print(e)
								#print("I don't care @ ask_weather")
								 
						except pyowm.exceptions.api_response_error.NotFoundError:
							 bot.send_message(chat_id=chatID, text = "location not found !")

					except pyowm.exceptions.api_call_error.APICallTimeoutError:
						bot.send_message(chat_id=chatID, text = "Dont mess with bot !")
						bot.send_message(chat_id=chatID, text = "Enter your appropriate location !")
						

				elif intent1 == 'loc_not_mentioned':
					bot.send_message(chat_id=chatID, text = "Enter your appropriate location ! Hey,Bot does not track you location.We care for user privacy")


				elif intent1 == 'covid19_ind_data':
					y=d.covidshow()
					tot=d.infectsum()
					bot.send_message(chat_id=chatID, text = "COVID-19 infected people data in India is as follows:")
					bot.send_message(chat_id=chatID, text = y)
					bot.send_message(chat_id=chatID, text = "Total Infected people in India:"+str(tot))


				else:
					bot.send_message(chat_id=chatID, text="Sorry,I cannot help you.Contact Developer for support !")

if __name__ == '__main__':
	TelegramMain()
