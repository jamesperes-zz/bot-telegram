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
    userid = update.message.from_user.id
    date = str(update.message.date)
    ide = str(update.message.chat_id)
    print('{0} {1}:{2} {3}  .... {4}'.format(date, user, text, ide, userid))


unknown_handler = MessageHandler(Filters.text, chat_listener)
updater.dispatcher.add_handler(unknown_handler)
updater.start_polling()
updater.idle()
