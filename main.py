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
    "🪞 *Zoom raus:* Stell dir vor, du siehst dich selbst von außen – wie du gerade kämpfst. Sag dir: „Krass, wie stark du gerade bist, dass du innehältst.“",
    "🎬 *Filmtrick:* Stell dir vor, dein Impuls ist nur eine Filmszene – du kannst sie stoppen, zurückspulen oder überspringen. *Du hast die Fernbedienung.*",
    "🕐 *Zeitreise:* Frag dich: Was wird mein zukünftiges Ich in 2 Stunden stolz erzählen, was ich *nicht* getan habe?",
    "🧃 *Dopamin-Ersatz:* Trink ein kaltes Glas Wasser in 3 Schlucken – bewusst. *Mini-Belohnung, echter Reset.*",
    "🚪 *Raumwechsel:* Geh 10 Schritte in einen anderen Raum oder an ein Fenster. *Neuer Reiz, neues Gefühl.*",
    "🔢 *5-4-3-2-1 Trick:* Zähle innerlich: 5 Dinge sehen, 4 hören, 3 fühlen, 2 riechen, 1 schmecken – du bist sofort im Jetzt.",
    "🍬 *Marshmallow-Trick (Stanford-Studie):*\nStell dir vor, du bekommst dein Lieblingsessen – aber *doppelt so gut*, wenn du 10 Minuten wartest. *Belohnung verschieben = Stärke gewinnen.*"
]

impulsstopp_bilder = [
    "https://images.unsplash.com/photo-1523978591478-c753949ff840?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1611223460067-715a6e5a65df?auto=format&fit=crop&w=800&q=80"
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
    "🪩 *Dopamin-Disco:*\nTanz 60 Sekunden zu deinem Lieblingslied – ja, jetzt! Bewegung + Musik + Überraschung = *Neustart für dein Belohnungssystem*.",
    "🎉 *Feier dich kurz:* Denk an das letzte Mal, wo du durchgezogen hast – fühl diesen Stolz. Sag dir laut: *„Ich kann das wieder.“*",
    "🎯 *Heute kein Bock?* Perfekt! Jetzt zählt’s am meisten. Motivation ist nicht Voraussetzung, sondern *Ergebnis von Aktion*.",
    "🧠 *Mindset Shift:* Statt „Ich muss“ sag „Ich darf“ – das verändert dein Gefühl sofort.",
    "📦 *Belohnung verschieben:* Schreib dir eine Belohnung auf, die du heute Abend bekommst – *wenn du 1 Sache jetzt durchziehst*.",
    "🃏 *Random Action:* Schließe die Augen, atme tief ein und zähle von 10 rückwärts. Öffne die Augen und mache dann das, was dir zuerst einfällt.",
    "🧊 *1-Minute-Kaltstart:* Wasch dein Gesicht mit kaltem Wasser, zieh dir die Schuhe an, geh raus – jetzt zählt nur: *einmal loslegen*.",
    "🎧 *Sound-Kick*\n\nHöre jetzt für 60 Sekunden einen Beat mit 120–140 bpm – idealerweise mit Kopfhörern. Währenddessen grinsen oder tanzen. Musik + Bewegung + Lächeln = *Dopamin-Kombo für Motivation*.",
]

motivation_bilder = [
    "https://images.unsplash.com/photo-1605296867304-46d5465a13f1?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1584466977773-e625c37cdd87?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1504198266285-165a8b34f0a1?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1588702547923-7093a6c3ba33?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1526403223033-3be62b7b7234?auto=format&fit=crop&w=800&q=80"
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
    "🌊 *Gedanken wie Wellen:* Lass sie kommen, lass sie gehen. *Du bist nicht deine Gedanken – du bist der Beobachter.*",
    "🪶 *1 Minute Leichtigkeit:* Leg deine Hand aufs Herz. Spür den Schlag. Sag dir: „Ich bin sicher. Ich bin da.“",
    "🌬️ *Längeres Ausatmen:* Atme 4 Sekunden ein, 6 Sekunden aus. Wiederhole 4x. *Ausatmen = Entspannen.*",
    "📦 *Gedanken-Parkplatz:* Stell dir eine Box vor. Pack all deine Gedanken rein – du kannst sie später abholen.",
    "☕ *Langsames Schlürfen:* Nimm einen bewussten Schluck Tee, Wasser oder Kaffee. Schließe die Augen. *Spür die Ruhe im Detail.*",
    "🔇 *Augen zu, 15 Sekunden atmen. Muskeln entspannen.*",
]

ruhe_bilder = [
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
    "https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0",
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1558981403-c5f9891de7b1?auto=format&fit=crop&w=800&q=80"
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
    "🎁 *Mini-Überraschung:* Schenk dir selbst jetzt was Kleines: ein Lächeln, ein Lied, eine Pause. *Ja, du darfst das.*",
    "📸 *Selfie mit Grimasse:* Mach jetzt ein dummes Gesicht und lach drüber. Humor ist Dopamin mit Kick.",
    "🦶 *Körper trickst Kopf:* Stell dich aufrecht hin, breite die Arme aus und lächle. 20 Sekunden. *Dein Gehirn folgt dem Körper.*",
    "👃 *Geruchs-Booster:* Riech an etwas Angenehmem: Kaffee, Parfüm, Kräuter. *Ein Duft kann alles drehen.*",
    "👂 *Stimme hören:* Sag laut: „Ich schaff das. Ich bin gut drauf.“ Laut. Jetzt. Dein Gehirn merkt's sich.",
    "🚶 *Micro-Movement Shift:*\nSteh auf und geh 60 Sekunden im Raum umher, Blick nach vorne, Schultern locker, Arme schwingen. Bewegung + offene Haltung = *Laune-Push*.",
]

laune_bilder = [
    "https://images.unsplash.com/photo-1511988617509-a57c8a288659?auto=format&fit=crop&w=800&q=80",  # lächelnde Frau
    "https://images.unsplash.com/photo-1543269865-cbf427effbad?auto=format&fit=crop&w=800&q=80",  # Musik & Freude
    "https://images.unsplash.com/photo-1504198453319-5ce911bafcde?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1518837695005-2083093ee35b?auto=format&fit=crop&w=800&q=80"
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
