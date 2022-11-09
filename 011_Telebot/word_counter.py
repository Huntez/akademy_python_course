import telebot
import connections

bot = telebot.TeleBot(connections.token)

@bot.message_handler(content_types=['text'])
def count_words(message):
    count = 0
    for i in message.text.split(" "):
        count += 1
    bot.send_message(message.chat.id, "word count : " + str(count))    

bot.infinity_polling()