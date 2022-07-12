import json
from telegram import Bot, ReplyKeyboardRemove

from django.http import JsonResponse
from django.views import View
from phoneasker.settings.base import BOT_TOKEN

from .handlers import post_contact
from .models import Contact
from .utils import KEYBOARD

bot = Bot(token=BOT_TOKEN)


class BotView(View):
    def post(self, request, *args, **kwargs):
        t_data = json.loads(request.body)
        t_message = t_data["message"]
        t_chat = t_message["chat"]
        chat_id = int(t_chat["id"])

        # если пришла кооманда /start
        if "text" in t_message and t_message["text"] == "/start":

            # проверяем или создаем Контакт
            contact, created = Contact.objects.get_or_create(pk=chat_id)

            # если новый, то отправляем кнопку
            if created:
                bot.send_message(
                    chat_id,
                    "Привет, а дай номер",
                    reply_markup=KEYBOARD
                )

        # если пришел контакт
        elif "contact" in t_message:
            contact = Contact.objects.filter(pk=chat_id).first()

            # если id уже внесен, а номер еще нет, то добавляем
            if contact and contact.phone is None:
                phone = t_message["contact"]["phone_number"]
                login = t_chat["username"]

                # сохраняем контакт
                contact.phone = phone
                contact.login = login
                contact.save()

                # прощаемся и убираем кнопку контакта
                bot.send_message(
                    chat_id,
                    "Спасибо",
                    reply_markup=ReplyKeyboardRemove()
                )

                # отправляем контак
                post_contact({
                    "phone": phone,
                    "login": login,
                })

        return JsonResponse({"ok": "POST request processed"})
