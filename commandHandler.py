# -*- coding: utf-8 -*-
import configuration
import common
import dbFunction
import re

groupID = configuration.adminGroup
admin = configuration.admin
botID = configuration.botID
botUsername = configuration.botUsername

def start(bot, message):
    if (dbFunction.addToAllUser(message.from_user) == 'failed'):
        if (dbFunction.updateToAllUser(message.from_user) == 'failed'):
            try:
                bot.send_message(chat_id=message.from_user.id, text='Cannot update your details ' + str(common.getName(message.from_user)))
            except:
                print('User update failed')
                bot.send_message(chat_id=admin, text='Cannot update details for ' + str(common.getName(message.from_user)))
        else:
            try:
                bot.send_message(chat_id=message.from_user.id, text='You Already STARTed me ' + common.getName(message.from_user) + ' and updated your personal details')
            except:
                print('User update failed')
    else:
        try:
            bot.send_message(chat_id=groupID, text='Bot started for ' + str(common.getName(message.from_user)))
            bot.send_message(chat_id=message.from_user.id, text='Hello ' + str(common.getName(message.from_user)) + '!\nYou can contact ResLK Messenger service using this BOT.')
        except:
            print('User start failed')

def blockUser(bot, message):
    if(message.chat.id == groupID):
        if(message.reply_to_message.from_user.id == botID and message.reply_to_message.forward_from != None):
            for chatAdmin in bot.get_chat_administrators(chat_id=groupID):
                if(message.from_user.id==chatAdmin.user.id and chatAdmin.user.is_bot==False):
                    if(dbFunction.blockUser(message.reply_to_message.forward_from)):
                        bot.send_message(chat_id=groupID, text='Successfully blocked and messages will not be received from ' + common.getName(message.reply_to_message.forward_from))
                    else:
                        bot.send_message(chat_id=groupID, text='Already blocked ' + common.getName(message.reply_to_message.forward_from))

def unblockUser(bot, message):
    if(message.chat.id == groupID):
        unblockuser = re.split('\W+', message.text, re.U)
        if(len(unblockuser)==3):
            if(unblockuser[2]=='' or unblockuser[2]==botUsername):
                try:
                    bot.send_message(chat_id=groupID, text='Please add a valid User ID to unblock users')
                except:
                    print('Please add a User ID to unblock users')
            elif(isinstance(int(unblockuser[2]),int)):
                if(common.chechStatus(unblockuser[2])):
                    if (dbFunction.unblockUser(unblockuser[2]) == 'success'):
                        try:
                            bot.send_message(chat_id=groupID, text='Successfully unblocked user <b>' + str(unblockuser[2]) + '</b>', parse_mode='HTML')
                        except:
                            print('Successfully unblocked user ' + str(unblockuser[2]))
                    else:
                        try:
                            bot.send_message(chat_id=groupID, text='Failed to unblock user <b>' + str(unblockuser[2]) + '</b>', parse_mode='HTML')
                        except:
                            print('Failed to unblock user ' + str(unblockuser[2]))
                else:
                    try:
                        bot.send_message(chat_id=groupID, text='<b>' + str(unblockuser[2]) + '</b> User ID not available', parse_mode='HTML')
                    except:
                        print(str(unblockuser[2]) + ' User ID not available')
            else:
                try:
                    bot.send_message(chat_id=groupID, text='User ID should be an <b>Integer</b> value', parse_mode='HTML')
                except:
                    print('User ID should be an Integer value')
        elif(len(unblockuser)==2):
            try:
                bot.send_message(chat_id=groupID, text='Please add a User ID to unblock users')
            except:
                print('Please add a user id to unblock users')
        else:
            try:
                bot.send_message(chat_id=groupID, text='Cannot unblock more than one User IDs same time')
            except:
                print('Cannot unblock more than one User IDs same time')

def blockList(bot, message):
    if(message.chat.id == groupID):
        text = '<b>Blocked Users</b>\n\n'
        count = 0
        blockList = dbFunction.getAllBlockedUsers()
        for users in blockList:
            count = count + 1
            text = text + '<b>' + users[0] + '</b>\nfname : ' + users[1] + '\nlname : ' + users[2] + '\nuname : ' + users[3]
            if(count != len(blockList)):
                text = text + '\n\n'

        if(len(text)>22):
            try:
                bot.send_message(chat_id=groupID, text=text, parse_mode='HTML')
            except:
                bot.send_message(chat_id=admin, text='Block list sending failed', parse_mode='HTML')
        else:
            try:
                bot.send_message(chat_id=groupID, text='Block list is empty', parse_mode='HTML')
            except:
                bot.send_message(chat_id=admin, text='Empty Block list sending failed', parse_mode='HTML')