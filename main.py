import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot("5303408159:AAFv_MiQO052ShZeUT8mQkr6OIzatv-QMN0")

conn = sqlite3.connect('C:/Users/User/Documents/GitHub/telegrambot1/learn.db', check_same_thread=False)
cursor = conn.cursor()


def db_table_val(user_id, name, phone, username, course):
    cursor.execute('INSERT INTO Student (user_id, name, phone, username, course) VALUES (?, ?, ?, ?, ?)',
                   (user_id, name, phone, username, course))
    conn.commit()


def db_table_update_phone(user_id, phone):
    cursor.execute(f'UPDATE Student SET phone=(?) WHERE user_id=(?)',(phone, user_id))
    conn.commit()


def db_table_update_course(user_id, course):
    cursor.execute(f'UPDATE Student SET course=(?) WHERE user_id=(?)', (course, user_id))
    conn.commit()


def ism_yoz(message):
    user_id = message.from_user.id
    name = message.text
    phone = "000"
    course = 'unbyb'
    username = message.from_user.username

    db_table_val(user_id, name=name, phone=phone, username=username, course=course)
    text = "Raxmat, Endi siz bilan bog'lanishimiz uchun raqamingizni kiriting:"
    text += "\nNamuma: <b>99 123 45 67</b>"

    bot.send_message(message.chat.id, text, parse_mode="html")
    bot.register_next_step_handler(message, raqam_yoz)


def raqam_yoz(message):
    raqam = message.text
    user_id = message.from_user.id
    db_table_update_phone(user_id, raqam)
    markup2 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    itembtn1 = types.KeyboardButton("Kompyuter Savodxonligi")
    itembtn2 = types.KeyboardButton("Frontend Development")
    itembtn3 = types.KeyboardButton("Python Backend")
    itembtn4 = types.KeyboardButton("IT english")
    itembtn5 = types.KeyboardButton("🔙 Go Back")
    markup2.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)
    text = "Ajoyib, Endi quyidagi kurslarimizdan birini tanlang:"
    bot.send_message(message.chat.id, text, reply_markup=markup2)
    bot.register_next_step_handler(message, kurs_yoz)


def kurs_yoz(message):
    course = message.text
    user_id = message.from_user.id
    db_table_update_course(user_id, course)

    text = "Ro'yxatdan o'tish yakunlandi.Biz sizga tez orada aloqaga chiqamiz."

    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    itembtn1 = types.KeyboardButton("🔹 Kurslarimiz haqida")
    itembtn2 = types.KeyboardButton("📝 Kursga Yozilish")
    itembtn3 = types.KeyboardButton("☎️ Aloqa va Manzil")
    itembtn4 = types.KeyboardButton("🌐 Ijtimoy tarmoqlarimiz")
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    text = "Assalomu Alaykum <b>\"Mike Academy\"</b> o'quv markazining ro'yxatdan o'tish, Rasmiy Telegram botiga xush kelibsiz"
    bot.send_message(message.chat.id, text, parse_mode="html", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text == "🔹 Kurslarimiz haqida":
        text = '''🖥 Bizning kurslarimiz:

<b>— Kompyuter savodxonligi,
— Python Backend,
— Frontend Development,
— IT-english,</b>
✅ Kurslarimiz haqida batafsil ma'lumotni quyida menu orqali bilib olasiz!'''
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtn1 = types.KeyboardButton("🔰Kompyuter Savodxonligi")
        itembtn2 = types.KeyboardButton("🔰Frontend Development")
        itembtn3 = types.KeyboardButton("🔰Python Backend")
        itembtn4 = types.KeyboardButton("🔰IT english")
        itembtn5 = types.KeyboardButton("🔙 Go Back")
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)
        bot.send_message(message.chat.id, text, parse_mode="html", reply_markup=markup)
    elif message.text == "📝 Kursga Yozilish":
        str1 = '''📩 Bu yerda siz bizning kurslarimizga ariza yozib qoldirishingiz mumkun:
Quyidagi so'ralgan formani aniq qilib to'ldiring va sizga admin tez orada aloqaga chiqadi:'''
        bot.send_message(message.chat.id, str1)
        bot.send_message(message.chat.id, "❓Ism va familyangiz:")
        bot.register_next_step_handler(message, ism_yoz)
    elif message.text == "🔰Kompyuter Savodxonligi":
        txt1 = '''Kompyuter savodxonligi.

📚 Kompyuter bilan umumiy tanishuv, Ofis dasturlari (Word, Excel), internet bilan ishlash kabi bilimlar o'rgatiladi.

📆 Kurs davomiyligi: 1 oy,
🗓 1 haftada 3 kun dars,
🕒 1 kunda 1 soat.

💰 Kurs narxi: 400 ming so'm,
💳 To'lov usuli: Naxt/ PayMe/ Bank.'''
        bot.send_message(message.chat.id, txt1)
    elif message.text == "🔰Frontend Development":
        txt2 = '''🌐 Frontend Development kursi.

📚 Frontend (HTML, CSS, JavaScript), React JS, Bootstrap kabi bilimlar o'rgatiladi.

📆 Kurs davomiyligi: 3 oy dan 6 oygacha
🗓 1 haftada: 3 kun dars,
🕒 1 kunda: 2 soat.

💰 Kurs narxi: 700 ming so'm/oyiga,
💳 To'lov usuli: Naxt/ PayMe/ Bank.'''
        bot.send_message(message.chat.id, txt2)
    elif message.text == "🔰Python Backend":
        txt3 = '''🌐 Backend kursi.

📚 Backend kursida PHP, Python, NodeJS kabi bilimlar o'rgatiladi.

📆 Kurs davomiyligi: 3 oy dan 9 oygacha,
🗓 1 haftada 3 kun dars,
🕒 1 kunda 2 soat.

💰 Kurs narxi: 800 ming so'm/oyiga,
💳 To'lov usuli: Naxt/ PayMe/ Bank.'''
        bot.send_message(message.chat.id, txt3)
    elif message.text == "🔰IT english":
        txt4 = '''🇬🇧 IT English.

📚 IT English kirish, IT sohasida Ingliz tili o'rni, IT sohasida ingliz tilidan foydalanish va natijaga erishish, xalqaro materiallar bilan ishlash, (Speaking va Grammar chuqurlashtirilgan holda) kabi bilimlar o'rgatiladi.

📆 Kurs davomiyligi: 3 oy,
🗓 1 haftada 3 kun dars,
🕒 1 kunda 2 soat.
💰 Kurs narxi: 300 ming so'm/oyiga,
💳 To'lov usuli: PayMe/Bank.'''
        bot.send_message(message.chat.id, txt4)
    elif message.text == "🔙 Go Back":
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtn1 = types.KeyboardButton("🔹 Kurslarimiz haqida")
        itembtn2 = types.KeyboardButton("📝 Kursga Yozilish")
        itembtn3 = types.KeyboardButton("☎️ Aloqa va Manzil")
        itembtn4 = types.KeyboardButton("🌐 Ijtimoy tarmoqlarimiz")
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
        text = "<b>Bosh Menu</b>"
        bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=markup)
    elif message.text == "☎️ Aloqa va Manzil":
        str2 = '''🔺 Mike ACADEMY
⏰ Ish vaxti: 09:00 dan 20:00 gacha
👤 Masul hodim: Muhammadsaid
🔹 Manzil: Amity Universiteti yotoqxonasi, Тошкент, Узбекистан
📱 Telefon: +998 91 001 65 77
📍 Locatsiya: https://www.google.com/maps/place/Amity+University+Tashkent/@41.3324611,69.2622475,17z/data=!3m1!4b1!4m5!3m4!1s0x38ae8b6cbd7e49a1:0xf23c3817c486d743!8m2!3d41.3324611!4d69.2644362'''
        bot.send_message(message.chat.id, str2)
    elif message.text == "🌐 Ijtimoy tarmoqlarimiz":
        str3 = '''🌐 Bizning ijtimoiy tarmoqlardagi manzillarimiz:

✔️ Telegram:  https://t.me/MikeSaid2000
✔️ Instagram:  instagram.com/Muhammadsid__shox'''
        bot.send_message(message.chat.id, str3)



bot.infinity_polling()

