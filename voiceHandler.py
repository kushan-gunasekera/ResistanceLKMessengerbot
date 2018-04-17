# -*- coding: utf-8 -*-
import configuration
import common

groupID = configuration.adminGroup
admin = configuration.admin
botID = configuration.botID

def privateVoice(bot, message):
    if (common.chechStatus(message.from_user.id) == False):
        try:
            bot.forward_message(chat_id=groupID, from_chat_id=message.chat.id, message_id=message.message_id)
            bot.send_message(chat_id=message.chat.id,
                             text='<b>Your Submission has Successfully Submitted</b> ' + str(
                                 common.getName(message.from_user)),
                             parse_mode='HTML')
        except:
            bot.send_message(chat_id=admin, text='Private Voice Forward Failed from agent ' + str(common.getName(message.from_user)), parse_mode='HTML')

def replyToUser(bot, message):
    if(message.reply_to_message.from_user.id == botID):
        for chatAdmin in bot.get_chat_administrators(chat_id=groupID):
            if(message.from_user.id==chatAdmin.user.id and chatAdmin.user.is_bot==False):
                try:
                    bot.send_voice(chat_id=message.reply_to_message.forward_from.id, data=message.voice.file_id, caption=message.caption)
                except:
                    try:
                        bot.send_message(chat_id=admin, text='Reply Voice Send Failed to agent ' + str(common.getName(message.reply_to_message.forward_from)), parse_mode='HTML')
                    except:
                        bot.send_message(chat_id=admin, text='Trying to reply as a Voice to the BOT message by ' + str(common.getName(message.from_user)))