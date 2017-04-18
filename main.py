from telegram.ext import Updater, CommandHandler
from datetime import datetime
now = datetime.now()


def start(bot, update):
    update.message.reply_text('Hello World!!')


def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


def hora(bot, update):
    update.message.reply_text(now.hour)
    update.message.reply_text(now.minute)

updater = Updater('228843118:AAGk6hkBpjIW_DazSEv843WwD_SMCuOFS0M')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('hora', hora))

updater.start_polling()
updater.idle()
