from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton


ab1 = KeyboardButton("/Statistics ☎️")
ab2 = KeyboardButton("/SendAds ⏳")
ab3 = KeyboardButton("/ManageUserAds ⚙")

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
kb_admin.add(ab1,ab2).add(ab3)
#Appears when admin use command /start

ib1 = InlineKeyboardButton(text="📬 text",callback_data="1")
ib2 = InlineKeyboardButton(text="📬 text",callback_data="2")
ib3 = InlineKeyboardButton(text="📬 text",callback_data="3")
ib4 = InlineKeyboardButton(text="📬 text",callback_data="4")
ib5 = InlineKeyboardButton(text="📬 text",callback_data="5")
ib6 = InlineKeyboardButton(text="📬 text",callback_data="6")
ib7 = InlineKeyboardButton(text="⬅️ back",callback_data="Inline_Back")

kb_ads_review = InlineKeyboardMarkup()
kb_ads_review.add(ib1).add(ib2).add(ib3).add(ib4).add(ib5).add(ib6).add(ib7)
#Appears when admin use command /SendAds

mb1 = InlineKeyboardButton(text="Read more",callback_data="command_Read_More")
mb2 = InlineKeyboardButton(text="Back",callback_data="command_Manage_Ads_Back")
kb_Manage_User_Ads = InlineKeyboardMarkup()
kb_Manage_User_Ads.add(mb1).add(mb2)
#Appears when admin use command /Manage user Ads

back_button = KeyboardButton("/Back")
kb_back = ReplyKeyboardMarkup(resize_keyboard=True)
kb_back.add(back_button)
#Exit from /Statistics


b1 = InlineKeyboardButton(text="Button text",callback_data="text")
b2 = InlineKeyboardButton(text="Button text",callback_data="text")
b3 = InlineKeyboardButton(text="Button text",callback_data="text")
kb_read_more = InlineKeyboardMarkup()
kb_read_more.add(b1).add(b2,b3)

b1 = InlineKeyboardButton(text="Approve",callback_data="command_Approve")
b2 = InlineKeyboardButton(text="Reject",callback_data="command_Reject")
b3 = InlineKeyboardButton(text="Back",callback_data="text")
kb_redm = InlineKeyboardMarkup()
kb_redm.add(b1,b2).add(b3)
#Inline keyboard for Read more in manage users ads

apbutton1 = InlineKeyboardButton(text="Yes ✅",callback_data="send_approve_user")
apbutton2 = InlineKeyboardButton(text="No ❌",callback_data="data")
kb_approve = InlineKeyboardMarkup()
kb_approve.add(apbutton1,apbutton2)
#Approve ads

rejbutton1 = InlineKeyboardButton(text="Yes ✅",callback_data="send_reject_user")
rejbutton2 = InlineKeyboardButton(text="No ❌",callback_data="data")
kb_reject = InlineKeyboardMarkup()
kb_reject.add(rejbutton1,rejbutton2)
#Reject ads