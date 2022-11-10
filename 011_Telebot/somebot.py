import telebot
import connections

bot = telebot.TeleBot(connections.token)
@bot.message_handler(commands=['calc', 'happy_ticket', 'start'])

def get_text(message):
    if message.text == "/calc":
        somevar = bot.send_message(message.chat.id, "Enter a action : ")
        bot.register_next_step_handler(somevar, calc)
    elif message.text == "/happy_ticket":
        somevar = bot.send_message(message.chat.id, "Enter a ticket : ")
        bot.register_next_step_handler(somevar, happy_ticket)

def count_words(message):
    count = 0
    for i in message.text.split(" "):
        count += 1
    bot.send_message(message.chat.id, "word count : " + str(count))    

def happy_ticket(message):
    ticket = message.text
    first = [int(i) for i in ticket[:len(ticket)//2]]
    second = [int(i) for i in ticket[(len(ticket)//2):]]
    if sum(first) == sum(second):
        bot.send_message(message.chat.id, "Ticket - " + ticket + " is happy!")
    else:
        bot.send_message(message.chat.id, "Ticket - " + ticket + " is unhappy..")

def calc(message):
    alist = ["+", "-", "*", "/"]
    svar = [i for i in message.text if i in alist]
    ab = [i for i in message.text.replace(" ", "").split(svar[0])]
    a, b = int(ab[0]), int(ab[1])
    if svar[0] == "+":
        bot.send_message(message.chat.id, str(a)+" + "+str(b)+" = "+str(a + b))
    elif svar[0] == "-":
        bot.send_message(message.chat.id, str(a)+" - "+str(b)+" = "+str(a - b))
    elif svar[0] == "*":
        bot.send_message(message.chat.id, str(a)+" * "+str(b)+" = "+str(a * b))
    elif svar[0] == "/":
        bot.send_message(message.chat.id, str(a)+" / "+str(b)+" = "+str(a / b))

bot.infinity_polling()