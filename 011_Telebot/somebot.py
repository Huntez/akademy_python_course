import telebot
import os.path
import connections
import login_registration

authorization_check = False

bot = telebot.TeleBot(connections.token)
@bot.message_handler(commands=['calc', 'happy_ticket', 
                            'count_words', 'statistics', 
                            'login', 'registration'])

def command_checker(message):
    if message.text == "/login":
        if not authorization_check:
            bot.send_message(message.chat.id, "user, password : ")
            bot.register_next_step_handler(message, login_to_db)
        else:
            bot.send_message(message.chat.id, "You already authorized!")
    elif message.text == "/registration":
        if not authorization_check:
            bot.send_message(message.chat.id, "user, password : ")
            bot.register_next_step_handler(message, registration)
        else:
            bot.send_message(message.chat.id, "You already authorized!")
    elif authorization_check:
        if message.text == "/calc":
            bot.send_message(message.chat.id, "Enter a action : ")
            bot.register_next_step_handler(message, calc)
        elif message.text == "/happy_ticket":
            somevar = bot.send_message(message.chat.id, "Enter a ticket : ")
            bot.register_next_step_handler(somevar, happy_ticket)
        elif message.text == "/count_words":
            somevar = bot.send_message(message.chat.id, "Enter a text : ")
            bot.register_next_step_handler(somevar, count_words)
        elif message.text == "/statistics":
            somevar = bot.send_message(message.chat.id, "Enter a text : ")
            bot.register_next_step_handler(somevar, show_statistics)
    else:
        bot.send_message(message.chat.id, "Log in first!")

def registration(message):
    user_and_password = message.text.replace(" ", "").split(",")
    auth = login_registration.authorization(user_and_password[0], 
    user_and_password[1])
    if auth.registration_to_db():
        bot.send_message(message.chat.id, "Account created!")
    else:
        bot.send_message(message.chat.id, "User already exist!")

def login_to_db(message):
    user_and_password = message.text.replace(" ", "").split(",")
    auth = login_registration.authorization(user_and_password[0], 
    user_and_password[1])
    if auth.login_to_db():
        global authorization_check
        authorization_check = True
        bot.send_message(message.chat.id, "Login success!")
    else:
        bot.send_message(message.chat.id, "Login failure!")        

def show_statistics(message):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    consonants = ['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 
    'n', 'p', 'q', 's', 't', 'v', 'x', 'z', 'h','r', 'w', 'y']
    prlist = [',', '!', '?', ':', '-', '"', "'"]
    even_count, odd_count, vowels_count, conso_count, prcount = 0, 0, 0, 0, 0
    
    word_count = len([i for i in message.text.split(" ")])
    for i in message.text.replace(" ", "").lower():
        if i in vowels:
            vowels_count += 1
        elif i in consonants:
            conso_count +=1
        elif i in prlist:
            prcount +=1
        elif i.isdigit():
            if int(i) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    file = open("stats.txt", "w")
    file.write("Symbol counter : " + str(len(message.text)) + "\n")
    file.write("Word counter : " + str(word_count) + "\n")
    file.write("Vowels counter : " + str(vowels_count) + "\n")
    file.write("Consonants counter : " + str(conso_count) + "\n")
    file.write("Punctuation symbol counter : " + str(prcount) + "\n")
    file.write("Even counter : " + str(even_count) + "\n")
    file.write("Odd counter : " + str(odd_count))
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