import logging
import time
import cx_Oracle
from telegram import Update
from telegram.ext import CommandHandler, Updater
from textwrap import wrap


logging.basicConfig(
    filename='kabo_telegram.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def start(update: Update, context):

    update.message.reply_text('Ola, Eu sou o KaBô e vou ajudar no tempo de resposta do tratamento de Tickets')

def sla(update: Update, context):

    while True:

        conn = cx_Oracle.connect(user="user", password="pass", dsn="host",encoding="UTF-8")

        query = """
SELECT
*
FROM table
WHERE status = 'xpto'
        
        """
        cursor = conn.cursor()

        time.sleep(3600)

        cursor.execute(query)

        result = cursor.fetchall()

        if result == None:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text='Otimo trabalho, sem tickets com a SLA a estourar.'
            )
        else:
            x = str(result)
            for line in wrap(x, width=90):
                context.bot.send_message(
                    chat_id=update.effective_chat.id, text=line.replace(',','')
                )

def main():
    updater = Updater(token='TELEGRAM_TOKEN')

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("sla", start))

    updater.start_polling()

if __name__ == '__main__':
    main()
