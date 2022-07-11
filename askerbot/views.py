import json

from django.http import JsonResponse
from django.views import View
from phoneasker.settings.base import BOT_TOKEN
from .models import Contact

from telegram import Bot, KeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup


bot = Bot(token=BOT_TOKEN)


class BotView(View):
    def post(self, request, *args, **kwargs):
        t_data = json.loads(request.body)
        t_message = t_data["message"]
        t_chat = t_message["chat"]
        chat_id = int(t_chat["id"])

        keyboard = ReplyKeyboardMarkup(
            keyboard=[[
                KeyboardButton(
                    text="Отправить контакт",
                    request_contact=True,
                )
            ]]
        )
        
        # если пришла кооманда /start
        if "text" in t_message and t_message["text"] == "/start":
            
            # проверяем или создаем Контакт
            contact, created = Contact.objects.get_or_create(pk=chat_id)
            
            # если новый, то отправляем кнопку
            if created:
                bot.send_message(
                    chat_id,
                    "Привет, а дай номер",
                    reply_markup=keyboard
                )
                
        # если пришел контакт
        elif "contact" in t_message:
            contact = Contact.objects.get(pk=chat_id)
            
            # если контакта еще не было, то добавить
            if contact.phone is None:
                contact.phone = t_message["contact"]["phone_number"]
                contact.save()
                
                # прощаемся и убираем кнопку контакта
                bot.send_message(
                    chat_id,
                    "Спасибо",
                    reply_markup=ReplyKeyboardRemove()
                )

        return JsonResponse({"ok": "POST request processed"})
