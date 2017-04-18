from telegram.ext import Updater, MessageHandler, Filters


updater = Updater('228843118:AAGk6hkBpjIW_DazSEv843WwD_SMCuOFS0M')


def chat_listener(bot, update):
    """
    A função chat_listener recebe uma mensagem de um usuário em privado ou em grupo
    e exibe no terminal a data,o primeiro nome do usuário(from_user.first_name) e
    o corpo da mensagem (update.message.text)
    """
    text = update.message.text
    user = update.message.from_user.first_name
    date = str(update.message.date)
    print('{0} {1}:{2}'.format(date, user, text))

unknown_handler = MessageHandler(Filters.text, chat_listener)
updater.dispatcher.add_handler(unknown_handler)
updater.start_polling()
updater.idle()
