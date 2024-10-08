import os
from supabase import create_client, Client
import telebot

url: str = os.environ.get("SUPABASE_URL")
users_email: str = os.environ.get("USER_EMAIL")
users_password: str = os.environ.get("USER_PASSWORD")
table_name: str = os.environ.get("TABLE_NAME")
telegram_token: str = os.environ.get("TELEGRAM_TOKEN")
service_key : str = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")

supabase: Client = create_client(url, service_key)

bot = telebot.TeleBot(telegram_token, parse_mode=None)

@bot.message_handler()
def NewMessage(message):
    txt = message.text.lower()
    if message.text == "/start":
        bot.reply_to(message, "PixiBot à votre service")
    elif "album" in txt:
        response = supabase.rpc("get_random_data").execute()
        bot.reply_to(message, response.data)
    else:
        bot.reply_to(
            message,
            'Veuillez reformuler votre demande afin de contenir le mot-clé album',
        )

bot.infinity_polling()
