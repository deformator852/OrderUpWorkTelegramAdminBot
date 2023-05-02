from aiogram.types import CallbackQuery
from create_bot import dp,bot,ID_ADMIN
from aiogram import types
from keyboards.keyboards import *

#message_handler
async def command_start(message: types.Message):
    if message.from_user.id == ID_ADMIN:
        await bot.send_message(ID_ADMIN,"Welcome Admin",reply_markup=kb_admin)

async def command_Statistics(message: types.Message):
    if message.from_user.id == ID_ADMIN:
        await bot.send_message(ID_ADMIN,"""
📊 Till Statistics:
! User: 
Total: 
Blocked: 
No ads: 
!Languages: 
🇬🇧EN: 
🇷🇺RU: 
🇹🇷TU: 
🇪🇸SP: 
🇮🇳HI: 
🇵🇰UR: 
🇲🇨IN: 
🇵🇭PH: 
!Downloads: 
Total: 
  • TikTok: 
  • Doyuin: 
  • Twitter: 
  • YouTube: 
  • Pinterest: 
  • Instagram: 
  • Facebook: 
        """,reply_markup=kb_back)
async def Back(message: types.Message):
    if message.from_user.id == ID_ADMIN:
      await bot.send_message(ID_ADMIN,"You exit from statistics",reply_markup=kb_admin)
async def command_Send_Ads(message: types.Message):
    if message.from_user.id == ID_ADMIN:
        await bot.send_message(ID_ADMIN,"Admin Ads revies\nPlease select a adss to review:",reply_markup=kb_ads_review)
async def command_Manage_UserAds(message: types.Message):
    if message.from_user.id == ID_ADMIN:
        await bot.send_message(ID_ADMIN,"Mailind ags 10516\nAd # 10516 can be viewed by clickin read more",reply_markup=kb_Manage_User_Ads)
#more callback_query_handler
async def Inline_Back(callback: CallbackQuery):
    message = callback.message.chat.id
    if ID_ADMIN == message:
        print("all right")
async def command_SendAds_Back(callback: CallbackQuery):
      message = callback.message.chat.id
      if ID_ADMIN == message:
        print("it's all right")

async def command_Read_More(callback: CallbackQuery):
    message = callback.message.chat.id
    if ID_ADMIN == message:
      await bot.send_photo(ID_ADMIN,photo=types.InputFile("images/tree1.jpg"),caption="Let user upwork so that everything can go smoothly, if after working I am s"
                                                                                      "atisfield we can edn the contract and I will play you in crypto.",reply_markup=kb_read_more)
      await bot.send_message(ID_ADMIN,"Admin can approve,reject above ads or press back to leave the process.",reply_markup=kb_redm)

async def command_Manage_Ads_Back(callback: CallbackQuery):
    message = callback.message.chat.id
    if ID_ADMIN == message:
        print("it's all right")

async def command_Approve(callback: CallbackQuery):
    message = callback.message.chat.id
    if ID_ADMIN == message:
        await bot.send_message(ID_ADMIN,"Do you want to approve?",reply_markup=kb_approve)

async def send_approve_user(callback: CallbackQuery):
    await bot.send_message(ID_ADMIN, text="Ad has been approved by admin")

async def send_reject_user(callback: CallbackQuery):
    await bot.send_message("id user", text="Ad has been rejected and deleted by admin")
async def command_Reject(callback: CallbackQuery):
    message = callback.message.chat.id
    if ID_ADMIN == message:
        await bot.send_message("id_user","Do you want to reject?",reply_markup=kb_reject)
def register_admin_handlers():
    dp.register_message_handler(command_start,commands="start")
    dp.register_message_handler(command_Statistics,commands="Statistics")
    dp.register_message_handler(command_Send_Ads,commands="SendAds")
    dp.register_message_handler(command_Manage_UserAds,commands="ManageUserAds")
    dp.register_message_handler(Back,commands="Back")
    #----------------------
    dp.register_callback_query_handler(command_SendAds_Back,text="command_back")
    dp.register_callback_query_handler(command_Manage_Ads_Back,text="command_Manage_Ads_Back")
    dp.register_callback_query_handler(command_Read_More,text="command_Read_More")
    dp.register_callback_query_handler(Inline_Back,text="Inline_Back")
    dp.register_callback_query_handler(command_Approve,text="command_Approve")
    dp.register_callback_query_handler(command_Reject,text="command_Reject")
    dp.register_callback_query_handler(send_approve_user,text="send_approve_user")
    dp.register_callback_query_handler(send_reject_user,text="send_reject_user")
