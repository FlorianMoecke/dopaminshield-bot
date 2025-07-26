import telebot
import random
import os
from datetime import datetime
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
from telebot import types
from flask import Flask, request
from threading import Thread

import json

# JSON-Datei für User-Daten
USER_DATA_FILE = "user_data.json"

# Lade Userdaten oder erstelle neue Datei
try:
    with open(USER_DATA_FILE, "r") as f:
        user_data = json.load(f)
except FileNotFoundError:
    user_data = {}

def save_user_data():
    with open(USER_DATA_FILE, "w") as f:
        json.dump(user_data, f, indent=2)

def update_user(user_id, key, value):
    uid = str(user_id)
    if uid not in user_data:
        user_data[uid] = {}
    user_data[uid][key] = value
    save_user_data()

def get_user_value(user_id, key, default=None):
    return user_data.get(str(user_id), {}).get(key, default)

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

# === ToolboxE ===

@bot.message_handler(commands=['toolbox'])
def toolbox_menu(message):
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("🔥 Impulsstopp", callback_data='tool_impulsstopp'),
        types.InlineKeyboardButton("🚀 Motivation", callback_data='tool_motivation')
    )
    markup.row(
        types.InlineKeyboardButton("😄 Laune", callback_data='tool_laune'),
        types.InlineKeyboardButton("🧘 Ruhe", callback_data='tool_ruhe')
    )
    bot.send_message(message.chat.id, "🧰 *Wähle eine Toolbox-Kategorie:*", reply_markup=markup, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: call.data.startswith('tool_'))
def sende_toolbox_inhalt(call):
    key = call.data.split('_')[1]  # ergibt jetzt z. B. 'impulsstopp'
    name = call.from_user.first_name or "Du"

    if key in inhalte:
        text = random.choice(inhalte[key]['nachrichten']).replace("{name}", name)
        bild = random.choice(inhalte[key]['bilder'])
        bot.send_message(call.message.chat.id, f"🧰 *{key.capitalize()}*\n\n{text}", parse_mode='Markdown')
        bot.send_photo(call.message.chat.id, bild)
    else:
        bot.send_message(call.message.chat.id, "⚠️ Kategorie nicht gefunden.")
        
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
    btn5 = types.KeyboardButton("🧰 Toolbox")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    

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

@bot.message_handler(func=lambda message: message.text == "🧰 Toolbox")
def toolbox_button_handler(message):
    toolbox_menu(message)

@bot.message_handler(func=lambda message: message.text.lower() in ['hi', 'hallo', 'start', 'hey', 'servus'])
def handle_greeting(message):
    sende_start(message)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_freetext(message):
try:
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Du bist ein motivierender Telegram-Coach."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300
    )
    antwort = response.choices[0].message.content

except openai.RateLimitError:
    antwort = "⚠️ KI ist gerade überlastet. Bitte später nochmal versuchen."

except openai.AuthenticationError:
    antwort = "⚠️ API-Key ist ungültig oder fehlt. Bitte prüfen."

except Exception as e:
    antwort = "⚠️ KI nicht erreichbar"
        
# === Starte den Bot über Webhook ===
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '', 200

bot.remove_webhook()
bot.set_webhook(url=f'https://dopaminshield.onrender.com/{TOKEN}')
print("Bot läuft... (Webhook-Modus)")
