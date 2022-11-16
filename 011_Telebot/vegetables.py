import telebot
import connections
import login_registration
import work_with_vg_db

db_name = "Vegetables"
bot = telebot.TeleBot(connections.token)
vg_db = work_with_vg_db.work_with_vegetables_db(db_name)

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
        button_sh_vg = telebot.types.KeyboardButton(text="show vegetables")
        button_sh_by_filter = telebot.types.KeyboardButton(text="show by filter")
        button_add_to_vg = telebot.types.KeyboardButton(text="add vegetable")
        button_del_from_db = telebot.types.KeyboardButton(text="del by id")
        button_logout = telebot.types.KeyboardButton(text="logout")
        keyboard.add(button_sh_vg, button_sh_by_filter, button_add_to_vg, 
        button_del_from_db, button_logout)
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
        if message.text == "show vegetables":
            show_vegetables(message)
        if message.text == "show by filter":
            bot.send_message(message.chat.id, "filter : ")
            bot.register_next_step_handler(message, show_vegetables_with_filters)
        if message.text == "add vegetable":
            bot.send_message(message.chat.id, "name, cost : ")
            bot.register_next_step_handler(message, add_to_db)
        if message.text == "del by id":
            bot.send_message(message.chat.id, "id: ")
            bot.register_next_step_handler(message, del_from_db)
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

def show_vegetables(message):
    try:
        bot.send_message(message.chat.id, vg_db.select_without_filters())
    except:
        bot.send_message(message.chat.id, "Database empty, add something!")

def show_vegetables_with_filters(message):
    try:
        bot.send_message(message.chat.id, vg_db.select_with_filter(message.text))
    except:
        bot.send_message(message.chat.id, "Database empty, add something!")

def del_from_db(message):
    try:
        bot.send_message(message.chat.id, "Okay!")
    except Exception as error:
        bot.send_message(message.chat.id, error)

def add_to_db(message):
    try:
        add_list = message.text.replace(" ", "").split(",")
        if vg_db.add_to_db(add_list[0], add_list[1]):
            bot.send_message(message.chat.id, "Okay!")
        else:
            bot.send_message(message.chat.id, "Already in db!")
    except IndexError:
        bot.send_message(message.chat.id, "Wrong format!")
            
bot.infinity_polling()