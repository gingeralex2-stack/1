import telebot
from telebot import types
from telebot.apihelper import ApiTelegramException
bot = telebot.TeleBot('8508596696:AAG0xMcCi6A-VYMGC9wwOmDcifekhoUlBTI')
CHANNEL_ID = '@olmath_hare'  # ✅ Правильно!
PDF_FILE = 'gift.pdf'

def is_subscribed(user_id):
    try:
        print(f"Check {user_id} for {CHANNEL_ID}")
        chat_member = bot.get_chat_member(CHANNEL_ID, user_id)
        print(f"Status: {chat_member.status}")
        return chat_member.status in ['member', 'administrator', 'creator']
    except Exception as e:
        print(f"Error: {e}")
        return False

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_gift = types.KeyboardButton('Get Gift!')
    markup.add(btn_gift)
    bot.send_message(message.chat.id, 'Подпишись @olmath_hare!', reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'Get Gift!')
def gift(message):
    user_id = message.from_user.id
    print(f"Gift request from {user_id}")
    if is_subscribed(user_id):
        print("✅ Sending PDF")
        with open(PDF_FILE, 'rb') as pdf:
            bot.send_document(message.chat.id, pdf, caption='🎁 Подарок!')
    else:
        print("❌ Not subscribed")
        markup = types.InlineKeyboardMarkup()
        btn_channel = types.InlineKeyboardButton('Подписаться', url='https://t.me/olmath_hare')
        markup.add(btn_channel)
        bot.send_message(message.chat.id, 'Сначала подпишись @olmath_hare!', reply_markup=markup)

print("🚀 Bot started!")
bot.polling(none_stop=True)
