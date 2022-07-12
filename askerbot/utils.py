from telegram import KeyboardButton, ReplyKeyboardMarkup


KEYBOARD = ReplyKeyboardMarkup(
            keyboard=[[
                KeyboardButton(
                    text="Отправить контакт",
                    request_contact=True,
                )
            ]]
        )
