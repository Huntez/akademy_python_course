import telebot
import connections
import login_registration

bot = telebot.TeleBot(connections.token)
db_name = "Vegetables"

@bot.message_handler(commands=['start'])
def start(message):
    authorization_check = login_registration.check_authorization(message.chat.id,
    db_name)
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    if not authorization_check.authorization_check():
        button_login = telebot.types.KeyboardButton(text="login")
        button_reg = telebot.types.KeyboardButton(text="registration")
        keyboard.add(button_login, button_reg)
        bot.send_message(message.chat.id, "Menu : ", reply_markup=keyboard)
    else:
        button_logout = telebot.types.KeyboardButton(text="logout")
        keyboard.add(button_logout)
        bot.send_message(message.chat.id, "Menu : ", reply_markup=keyboard)                              

@bot.message_handler(content_types=['text'])
def command_checker(message):
    authorization_check = login_registration.check_authorization(message.chat.id,
    db_name)
    if message.text == "login":
        if not authorization_check.authorization_check():
            bot.send_message(message.chat.id, "user, password : ")
            bot.register_next_step_handler(message, login_to_db)
        else:
            bot.send_message(message.chat.id, "You already authorized!")
            start(message)
    elif message.text == "registration":
        if not authorization_check.authorization_check():
            bot.send_message(message.chat.id, "user, password : ")
            bot.register_next_step_handler(message, registration)
        else:
            bot.send_message(message.chat.id, "You already authorized!")
            start(message)
    elif authorization_check.authorization_check():
        if message.text == "logout":
            logout(message)
    else:
        bot.send_message(message.chat.id, "Log in first!")
        start(message)

def registration(message):
    try:
        user_and_password = message.text.replace(" ", "").split(",")
        auth = login_registration.authorization(user_and_password[0], 
        user_and_password[1], db_name)
    except IndexError:
        bot.send_message(message.chat.id, "Wrong format!")
    else:
        if auth.registration_to_db():
            bot.send_message(message.chat.id, "Account created!")
        else:
            bot.send_message(message.chat.id, "User already exist!")

def logout(message):
    try:
        authorization_check = login_registration.check_authorization(message.chat.id, 
        db_name)
        authorization_check.authorization_update(False)
    except Exception as error:
        print(error)
    else:
        start(message)

def login_to_db(message):
    try:
        user_and_password = message.text.replace(" ", "").split(",")
        auth = login_registration.authorization(user_and_password[0], 
        user_and_password[1], db_name)
    except IndexError:
        bot.send_message(message.chat.id, "Wrong format!")
    else:
        if auth.login_to_db():
            authorization_check = login_registration.check_authorization(message.chat.id,
            db_name)
            authorization_check.authorization_update(True)          
            bot.send_message(message.chat.id, "Login success!")
            start(message)
        else:
            bot.send_message(message.chat.id, "Login failure!")

def show_vegetables():
    pass

def show_vegetables_with_filters():
    pass
            
bot.infinity_polling()