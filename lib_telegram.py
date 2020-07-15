import telegram

def sendTelegram(msg):
    my_token = r'1163113362:AAFtIm0BSzQEFVFR9ArwkBBpP2vALYn00NU'
    bot = telegram.Bot(token = my_token)
    """
    TEST 출력
    updates = bot.getUpdates() 
    print(bot)   
    
    for u in updates: 
        print(u.message)
    """
    bot.sendMessage(chat_id = '1260392260', text = msg)

        
