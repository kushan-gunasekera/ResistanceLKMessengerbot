# -*- coding: utf-8 -*-
import sys
sys.path.append('/mnt/c/Users/hp/AppData/Local/Programs/Python/Python36-32/Lib/site-packages')
import telebot
import configuration
import textHandler
import photoHandler
import audioHandler
import videoHandler
import documentHandler
import voiceHandler
import locationHandler
import contactHandler
import stickerHandler
import commandHandler

bot = telebot.TeleBot(configuration.botToken)

@bot.message_handler(commands=['blockuser'])
def handle_command_botversion(message):
    commandHandler.blockUser(bot, message)

@bot.message_handler(commands=['unblockuser'])
def handle_command_botversion(message):
    commandHandler.unblockUser(bot, message)

@bot.message_handler(commands=['blocklist'])
def handle_command_botversion(message):
    commandHandler.blockList(bot, message)

@bot.message_handler(commands=['start'])
def handle_command_botversion(message):
    commandHandler.start(bot, message)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if (message.chat.type == 'private'):
        textHandler.privateText(bot, message)
        return
    if(message.reply_to_message != None):
        textHandler.replyToUser(bot, message)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    if (message.chat.type == 'private'):
        photoHandler.privatePhoto(bot, message)
        return
    if (message.reply_to_message != None):
        photoHandler.replyToUser(bot, message)

@bot.message_handler(content_types=['audio'])
def handle_audio(message):
    if (message.chat.type == 'private'):
        audioHandler.privateAudio(bot, message)
        return
    if (message.reply_to_message != None):
        audioHandler.replyToUser(bot, message)

@bot.message_handler(content_types=['video'])
def handle_video(message):
    if (message.chat.type == 'private'):
        videoHandler.privateVideo(bot, message)
        return
    if (message.reply_to_message != None):
        videoHandler.replyToUser(bot, message)

@bot.message_handler(content_types=['document'])
def handle_document(message):
    if (message.chat.type == 'private'):
        documentHandler.privateDocument(bot, message)
        return
    if (message.reply_to_message != None):
        documentHandler.replyToUser(bot, message)

@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    if (message.chat.type == 'private'):
        voiceHandler.privateVoice(bot, message)
        return
    if (message.reply_to_message != None):
        voiceHandler.replyToUser(bot, message)

@bot.message_handler(content_types=['location'])
def handle_location(message):
    if (message.chat.type == 'private'):
        locationHandler.privateLocation(bot, message)
        return
    if (message.reply_to_message != None):
        locationHandler.replyToUser(bot, message)

@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    if (message.chat.type == 'private'):
        contactHandler.privateContact(bot, message)
        return
    if (message.reply_to_message != None):
        contactHandler.replyToUser(bot, message)

@bot.message_handler(content_types=['sticker'])
def handle_stickers(message):
    # if (message.chat.type == 'private'):
    #     stickerHandler.privateSticker(bot, message)
    #     return
    if (message.reply_to_message != None):
        stickerHandler.replyToUser(bot, message)

bot.polling(none_stop=True, interval=0, timeout=0)