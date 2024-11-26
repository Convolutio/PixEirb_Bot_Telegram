import os
import requests
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

# see docker compose
POCKETBASE_INTERN_URL: str = "http://pocketbase-server:8090"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="PixiBot à votre service !")

def get_message_handler(pocketbase_url: str):
    async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
        txt = update.message.text.lower()
        if "album" in txt:
            response = requests.get(pocketbase_url + "/get_random_response").json()["texte"]
            await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Veuillez reformuler votre demande afin de contenir le mot-clé album")
    return message_handler
    
if __name__ == '__main__':
    load_dotenv()  # take environment variables from .env.

    def load_or_raise(token: str):
        val = os.getenv(token)
        if (val is None):
            raise ValueError(f"No value with the {token} key in your .env")
        return val

    telegram_token: str = load_or_raise("TELEGRAM_TOKEN")
    pocketbase_url = os.getenv("POCKETBASE_URL", POCKETBASE_INTERN_URL)
    
    msg_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), get_message_handler(pocketbase_url))
    application = ApplicationBuilder().token(telegram_token).build()
    
    start_handler = CommandHandler('start', start)
    
    application.add_handler(start_handler)
    application.add_handler(msg_handler)

    application.run_polling()
