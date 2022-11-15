import telebot
import os.path

class send_files:
    def __init__(self, token, message_chat_id):
        self.bot = telebot.TeleBot(token)
        self.message_chat_id = message_chat_id

    def file_exist_check(self, file_name):
        if os.path.exists(file_name):
            return True
        else:
            return False
           
    def send_document(self, file_name):
        if self.file_exist_check:
            self.file_name = open(file_name, "rb")
            try:
                self.bot.send_document(self.message_chat_id, self.file_name)
                self.file_name.close()
            except Exception as error:
                print(error)
        else:
            raise Exception("File not exist!")