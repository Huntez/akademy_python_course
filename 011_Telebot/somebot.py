import telebot
import os.path
import connections

bot = telebot.TeleBot(connections.token)
@bot.message_handler(commands=['calc', 'happy_ticket', 'count_words', 'statistics'])

def get_text(message):
    if message.text == "/calc":
        somevar = bot.send_message(message.chat.id, "Enter a action : ")
        bot.register_next_step_handler(somevar, calc)
    elif message.text == "/happy_ticket":
        somevar = bot.send_message(message.chat.id, "Enter a ticket : ")
        bot.register_next_step_handler(somevar, happy_ticket)
    elif message.text == "/count_words":
        somevar = bot.send_message(message.chat.id, "Enter a text : ")
        bot.register_next_step_handler(somevar, count_words)
    elif message.text == "/statistics":
        somevar = bot.send_message(message.chat.id, "Enter a text : ")
        bot.register_next_step_handler(somevar, statistics)

def statistics(message):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    consonants = ['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 
    'n', 'p', 'q', 's', 't', 'v', 'x', 'z', 'h','r', 'w', 'y']
    prlist = [',', '!', '?', ':', '-', '"', "'"]
    chcount, nchcount, gcount, ngcount, pcount = 0, 0, 0, 0, 0
    
    wcount = len([i for i in message.text.split(" ")])
    for i in message.text.replace(" ", "").lower():
        if i in vowels:
            gcount += 1
        elif i in consonants:
            ngcount +=1
        elif i in prlist:
            pcount +=1
        elif i.isdigit():
            if int(i) % 2 == 0:
                chcount += 1
            else:
                nchcount += 1

    file = open("stats.txt", "w")
    file.write("Symbol counter : " + str(len(message.text)) + "\n")
    file.write("Word counter : " + str(wcount) + "\n")
    file.write("Vowels counter : " + str(gcount) + "\n")
    file.write("Consonants counter : " + str(ngcount) + "\n")
    file.write("Punctuation symbol counter : " + str(pcount) + "\n")
    file.write("Even counter : " + str(chcount) + "\n")
    file.write("Odd counter : " + str(nchcount))
    file.close()

    file = open("stats.txt", "rb")
    bot.send_document(message.chat.id, file)
    file.close()

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