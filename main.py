import telebot
import random
import os
from telebot import types
from flask import Flask
from threading import Thread


# === UptimeRobot Keep-Alive ===
app = Flask('')


@app.route('/')
def home():
    return "Bot läuft!"


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()


keep_alive()

import json

# === Inhalte aus ausgelagerter JSON laden ===
with open('inhalte.json', 'r', encoding='utf-8') as f:
    inhalte = json.load(f)

motivation_nachrichten = inhalte['motivation']['nachrichten']
motivation_bilder = inhalte['motivation']['bilder']

impulsstopp_nachrichten = inhalte['impulsstopp']['nachrichten']
impulsstopp_bilder = inhalte['impulsstopp']['bilder']

ruhe_nachrichten = inhalte['ruhe']['nachrichten']
ruhe_bilder = inhalte['ruhe']['bilder']

laune_nachrichten = inhalte['laune']['nachrichten']
laune_bilder = inhalte['laune']['bilder']

# Token einfügen
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

# === Trigger: Impulsstop ===
@bot.message_handler(commands=['impulsstopp'])
def sende_impulsstopp(message):
    name = message.from_user.first_name if message.from_user.first_name else "Du"
    text = random.choice(impulsstopp_nachrichten).replace("{name}", name)
    bild = random.choice(impulsstopp_bilder)
    bot.send_message(message.chat.id, text, parse_mode='Markdown')
    bot.send_photo(message.chat.id, bild)

# === Trigger: Motivation ===
@bot.message_handler(commands=['motivation'])
def sende_motivation(message):
    name = message.from_user.first_name if message.from_user.first_name else "Du"
    text = random.choice(motivation_nachrichten).replace("{name}", name)
    bild = random.choice(motivation_bilder)
    bot.send_message(message.chat.id, text, parse_mode='Markdown')
    bot.send_photo(message.chat.id, bild)


# === Trigger: RUHE ===

@bot.message_handler(commands=['ruhe'])
def sende_ruhe(message):
    text = random.choice(ruhe_nachrichten)
    bild = random.choice(ruhe_bilder)
    bot.send_message(message.chat.id, text, parse_mode='Markdown')
    bot.send_photo(message.chat.id, bild)


# === Trigger: LAUNE ===

@bot.message_handler(commands=['laune'])
def sende_laune(message):
    text = random.choice(laune_nachrichten)
    bild = random.choice(laune_bilder)
    bot.send_message(message.chat.id, text, parse_mode='Markdown')
    bot.send_photo(message.chat.id, bild)


# === START ===
@bot.message_handler(commands=['start'])
def sende_start(message):
    welcome_text = ("👋 Willkommen beim DopaminBot!\n\n"
                    "Wähle eine Option:")

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🔥 Impulsstopp")
    btn2 = types.KeyboardButton("🧘 Ruhe")
    btn3 = types.KeyboardButton("🚀 Motivation")
    btn4 = types.KeyboardButton("😄 Laune")
    markup.add(btn1, btn2, btn3, btn4)

    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)


# === Button Handlers ===
@bot.message_handler(func=lambda message: message.text == "🔥 Impulsstopp")
def impulsstopp_button_handler(message):
    sende_impulsstopp(message)


@bot.message_handler(func=lambda message: message.text == "🧘 Ruhe")
def ruhe_button_handler(message):
    sende_ruhe(message)


@bot.message_handler(func=lambda message: message.text == "🚀 Motivation")
def motivation_button_handler(message):
    sende_motivation(message)


@bot.message_handler(func=lambda message: message.text == "😄 Laune")
def laune_button_handler(message):
    sende_laune(message)


# === Starte den Bot ===
print("Bot läuft...")
bot.infinity_polling()
