import os
import requests
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

# see docker compose
POCKETBASE_URL: str = "pocketbase-server:8090"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="PixiBot à votre service !")

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    txt = update.message.text.lower()
    if "album" in txt:
        response = requests.get("http://" + POCKETBASE_URL + "/get_random_response").json()["texte"]
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Veuillez reformuler votre demande afin de contenir le mot-clé album")
    
if __name__ == '__main__':
    load_dotenv()  # take environment variables from .env.

    telegram_token: str = os.getenv("TELEGRAM_TOKEN")
    
    msg_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), message_handler)
    application = ApplicationBuilder().token(telegram_token).build()
    
    start_handler = CommandHandler('start', start)
    
    application.add_handler(start_handler)
    application.add_handler(msg_handler)

    application.run_polling()
