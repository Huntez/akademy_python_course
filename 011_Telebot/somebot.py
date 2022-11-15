import telebot
import os.path
import connections
import login_registration
import sending

authorization_check = False
bot = telebot.TeleBot(connections.token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    if not authorization_check:
        button_login = telebot.types.KeyboardButton(text="login")
        button_reg = telebot.types.KeyboardButton(text="registration")
        keyboard.add(button_login, button_reg)
        bot.send_message(message.chat.id, "Menu : ", reply_markup=keyboard)
    else:
        button_calc = telebot.types.KeyboardButton(text="calc")
        button_hticket = telebot.types.KeyboardButton(text="happy ticket")
        button_cwords = telebot.types.KeyboardButton(text="count words")
        button_stats = telebot.types.KeyboardButton(text="text statistics")
        keyboard.add(button_calc, button_hticket, button_cwords, button_stats)
        bot.send_message(message.chat.id, "Menu : ", reply_markup=keyboard)                              

@bot.message_handler(content_types=['text'])
def command_checker(message):
    if message.text == "login":
        if not authorization_check:
            bot.send_message(message.chat.id, "user, password : ")
            bot.register_next_step_handler(message, login_to_db)
        else:
            bot.send_message(message.chat.id, "You already authorized!")
    elif message.text == "registration":
        if not authorization_check:
            bot.send_message(message.chat.id, "user, password : ")
            bot.register_next_step_handler(message, registration)
        else:
            bot.send_message(message.chat.id, "You already authorized!")
    elif authorization_check:
        if message.text == "calc":
            bot.send_message(message.chat.id, "Enter a action : ")
            bot.register_next_step_handler(message, calc)
        if message.text == "happy ticket":
            somevar = bot.send_message(message.chat.id, "Enter a ticket : ")
            bot.register_next_step_handler(somevar, happy_ticket)
        if message.text == "count words":
            somevar = bot.send_message(message.chat.id, "Enter a text : ")
            bot.register_next_step_handler(somevar, count_words)
        if message.text == "text statistics":
            somevar = bot.send_message(message.chat.id, "Enter a text : ")
            bot.register_next_step_handler(somevar, send_statistics)
    else:
        bot.send_message(message.chat.id, "Log in first!")
        start(message)

def registration(message):
    try:
        user_and_password = message.text.replace(" ", "").split(",")
        auth = login_registration.authorization(user_and_password[0], 
        user_and_password[1])
    except IndexError:
        bot.send_message(message.chat.id, "Wrong format!")
    else:
        if auth.registration_to_db():
            bot.send_message(message.chat.id, "Account created!")
        else:
            bot.send_message(message.chat.id, "User already exist!")

def login_to_db(message):
    try:
        user_and_password = message.text.replace(" ", "").split(",")
        auth = login_registration.authorization(user_and_password[0], 
        user_and_password[1])
    except IndexError:
        bot.send_message(message.chat.id, "Wrong format!")
    else:
        if auth.login_to_db():
            global authorization_check
            authorization_check = True
            bot.send_message(message.chat.id, "Login success!")
            start(message)
        else:
            bot.send_message(message.chat.id, "Login failure!")        

def send_statistics(message):
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

    # need rework
    send_file = sending.send_files(token=connections.token, 
    message_chat_id=message.chat.id)
    send_file.send_document("stats.txt")

def count_words(message):
    bot.send_message(message.chat.id, "word count : " + str(len(message.text.split(" "))))    

def happy_ticket(message):
    try:
        ticket = message.text
        first = [int(i) for i in ticket[:len(ticket)//2]]
        second = [int(i) for i in ticket[(len(ticket)//2):]]
    except ValueError:
        bot.send_message(message.chat.id, "Wrong value!")
    else:
        if sum(first) == sum(second):
            bot.send_message(message.chat.id, "Ticket - " + ticket + " is happy!")
        else:
            bot.send_message(message.chat.id, "Ticket - " + ticket + " is unhappy..")

def calc(message):
    try:
        alist = ["+", "-", "*", "/"]
        svar = [i for i in message.text if i in alist]
        ab = [i for i in message.text.replace(" ", "").split(svar[0])]
        a, b = int(ab[0]), int(ab[1])
    except IndexError:
        bot.send_message(message.chat.id, "Wrong format!")
    else:
        if svar[0] == "+":
            bot.send_message(message.chat.id, str(a)+" + "+str(b)+" = "+str(a + b))
        elif svar[0] == "-":
            bot.send_message(message.chat.id, str(a)+" - "+str(b)+" = "+str(a - b))
        elif svar[0] == "*":
            bot.send_message(message.chat.id, str(a)+" * "+str(b)+" = "+str(a * b))
        elif svar[0] == "/":
            bot.send_message(message.chat.id, str(a)+" / "+str(b)+" = "+str(a / b))

bot.infinity_polling()