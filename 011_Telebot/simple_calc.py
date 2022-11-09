import telebot
import connections

bot = telebot.TeleBot(connections.token)
@bot.message_handler(content_types=['text'])

def get_text(message):
    alist = ["+", "-", "*", "/"]
    svar = [i for i in message.text if i in alist]
    message.text = [i for i in message.text.replace(" ", "").split(svar[0])]
    a, b = int(message.text[0]), int(message.text[1])
    if svar[0] == "+":
        bot.send_message(message.chat.id, str(a)+" + "+str(b)+" = "+str(a + b))
    elif svar[0] == "-":
        bot.send_message(message.chat.id, str(a)+" - "+str(b)+" = "+str(a - b))
    elif svar[0] == "*":
        bot.send_message(message.chat.id, str(a)+" * "+str(b)+" = "+str(a * b))
    elif svar[0] == "/":
        bot.send_message(message.chat.id, str(a)+" / "+str(b)+" = "+str(a / b))

bot.polling(none_stop=True, interval=0)