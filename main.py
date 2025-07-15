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

# Token einfügen
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

# === Trigger: IMPULSSTOPP ===
impulsstopp_nachrichten = [
    "😌 *Psychological Sigh:*\n2x durch die Nase einatmen, 1x lang ausatmen durch den Mund. 3x wiederholen – wirkt sofort gegen Stress und Impulse.",
    "🧊 *Musterunterbrechung:*\nStell dir dein Lieblingsessen eiskalt & geschmacklos vor. Oder: Geh Zähne putzen – dein Gehirn bekommt ein neues Signal: *„Ich bin fertig.“*",
    "🎁 *Mini-Reframing:*\n„Das, was du jetzt widerstehst, macht dich stärker als alles, was du essen könntest.“\n*Kurzfristiger Verzicht – langfristiger Stolz.*",
    "🎲 *Sofort-Ablenkungsspiel:*\nDenk an 3 Dinge, die du auch gern magst, die aber gesund sind (z. B. Kefir, Nüsse, Tee). Nimm das erste. Der Impuls wird umlenkt.",
    "🧠 *WOOP gegen Heißhunger:*\nWish: Klar bleiben\nOutcome: Leicht fühlen\nObstacle: Süßhunger\nPlan: 3x tief durchatmen, 1 Glas Wasser, 5 Min warten – oft reicht das schon.",
    "🗣️ *Selbstgespräch stoppen (nach Ethan Kross):*\n„Stopp, {name}, das brauchst du gerade nicht wirklich.“\nSprich mit dir in der dritten Person – das schafft Abstand zum Impuls.",
    "🎯 *Fantasie-Ort aktivieren:*\nSchließ die Augen. Stell dir vor, du sitzt auf einem Berggipfel, Wind im Gesicht, Ruhe pur. Halte dieses Bild 15 Sekunden.",
    "🎲 *Würfelspiel-Ablenkung:*\nDenk dir 3 kleine Aufgaben:\n1️⃣ Hampelmann\n2️⃣ Lied summen\n3️⃣ Wasser holen\nLass den Zufall entscheiden – und tu’s einfach!",
    "🍬 *Marshmallow-Trick (Stanford-Studie):*\nStell dir vor, du bekommst dein Lieblingsessen – aber *doppelt so gut*, wenn du 10 Minuten wartest. *Belohnung verschieben = Stärke gewinnen.*"
]

impulsstopp_bilder = [
    "https://images.unsplash.com/photo-1523978591478-c753949ff840?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80"
]



@bot.message_handler(commands=['impulsstopp'])
def sende_impulsstopp(message):
    name = message.from_user.first_name if message.from_user.first_name else "Du"
    text = random.choice(impulsstopp_nachrichten).replace("{name}", name)
    bild = random.choice(impulsstopp_bilder)
    bot.send_message(message.chat.id, text, parse_mode='Markdown')
    bot.send_photo(message.chat.id, bild)


# === Trigger: MOTIVATION ===
motivation_nachrichten = [
    "🏃 *Bewegung kickt Motivation*\n\nStarte mit 30 Sekunden Bewegung – jetzt sofort: z. B. 10 Kniebeugen, Hampelmänner oder schnelles Treppensteigen. Bewegung aktiviert dein dopaminerges System – dein Gehirn wechselt vom Denken ins Handeln. *Motivation folgt der Bewegung, nicht umgekehrt.*",
    "🧠 *Sprich mit dir wie mit einem Freund* (nach Ethan Kross)\n\nStell dir vor, du sprichst mit deinem besten Freund – oder dir selbst in der dritten Person:\n„{name}, du schaffst das. Du weißt, warum du das machst. Du bist schon oft gestartet.“\nSo bekommst du sofort mehr Klarheit und Kontrolle.",
    "🥅 *Mach einen 10-Sekunden-WOOP*\n\n**Wunsch:** Was willst du gerade erreichen?\n**Ergebnis:** Was wäre das Beste daran?\n**Hindernis:** Was steht dir im Weg?\n**Plan:** Was tust du, wenn es auftaucht?\n\nSag es dir leise oder laut – du aktivierst damit dein Zielnetzwerk im Gehirn.",
    "💥 *Tiny Win erzeugt Momentum*\n\nErledige jetzt eine Mini-Aufgabe (z. B. 1 E-Mail, 10 Liegestütze, Wasser holen). Der *erste Schritt* erzeugt Schwung – Motivation kommt nicht vor der Handlung, sondern *aus* der Handlung.",
    "🧩 *Reframe: Du bist der Typ, der loslegt* (nach Carol Dweck)\n\nSag dir: „Ich bin jemand, der startet – auch wenn es schwer ist.“\nDas aktiviert dein Selbstbild und ein Growth Mindset – du brauchst kein Ziel, du brauchst *Identität*.",
    "🎧 *Sound-Kick*\n\nHöre jetzt für 60 Sekunden einen Beat mit 120–140 bpm – idealerweise mit Kopfhörern. Währenddessen grinsen oder tanzen. Musik + Bewegung + Lächeln = *Dopamin-Kombo für Motivation*.",
]

motivation_bilder = [
    "https://images.unsplash.com/photo-1605296867304-46d5465a13f1?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1584466977773-e625c37cdd87?auto=format&fit=crop&w=800&q=80"
]


@bot.message_handler(commands=['motivation'])
def sende_motivation(message):
    name = message.from_user.first_name if message.from_user.first_name else "Du"
    text = random.choice(motivation_nachrichten).replace("{name}", name)
    bild = random.choice(motivation_bilder)
    bot.send_message(message.chat.id, text, parse_mode='Markdown')
    bot.send_photo(message.chat.id, bild)


# === Trigger: RUHE ===
ruhe_nachrichten = [
    "🧘 *Atme ein… und aus…Lass los*",
    "🌿 *Nur da sein – kein Druck.Lass los.*",
    "☁️ *Schau 10 Sekunden in den Himmel.Muskeln entspannen.*",
    "🔇 *Augen zu, 15 Sekunden atmen. Muskeln entspannen.*",
]

ruhe_bilder = [
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
    "https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0",
]


@bot.message_handler(commands=['ruhe'])
def sende_ruhe(message):
    text = random.choice(ruhe_nachrichten)
    bild = random.choice(ruhe_bilder)
    bot.send_message(message.chat.id, text, parse_mode='Markdown')
    bot.send_photo(message.chat.id, bild)


# === Trigger: LAUNE ===
laune_nachrichten = [
    "🎧 *Musik-Shift:*\nHöre 60 Sekunden deinen Lieblingssong mit positiven Erinnerungen – *am besten tanzend oder singend*. Musik mit Bedeutung aktiviert dein Belohnungszentrum doppelt.",
    "🖼️ *Dankbarkeits-Zoom:*\nDenk an 3 kleine Dinge, für die du gerade dankbar bist. *Nicht groß – sondern konkret!* (z. B. weiches Bett, leckerer Kaffee, freundlicher Blick heute).",
    "📞 *Social Ping:*\nSchick jemandem eine kurze Nachricht mit einem ehrlichen Kompliment. Du erzeugst *sofort positive Resonanz* – auch in deinem Gehirn.",
    "🚶 *Micro-Movement Shift:*\nSteh auf und geh 60 Sekunden im Raum umher, Blick nach vorne, Schultern locker, Arme schwingen. Bewegung + offene Haltung = *Laune-Push*.",
]

laune_bilder = [
    "https://images.unsplash.com/photo-1511988617509-a57c8a288659?auto=format&fit=crop&w=800&q=80",  # lächelnde Frau
    "https://images.unsplash.com/photo-1543269865-cbf427effbad?auto=format&fit=crop&w=800&q=80",  # Musik & Freude
]


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
