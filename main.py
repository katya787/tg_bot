import telebot 
from telebot.types import Message 
import random 
from random import choice

bot = telebot.TeleBot()


@bot.message_handler(commands=['start'])
def start_cmd(message: Message):
    bot.send_message(message.chat.id, 'Привет! Я тестовый бот(∩▂∩)')

@bot.message_handler(commands=['coin'])
def coin_cmd(message: Message):
    x = random.randint(0,1)
    if x == 0:
        bot.reply_to(message, 'Вам выпал орёл!')
    else:
        bot.reply_to(message, 'Вам выпала решка!')

@bot.message_handler(commands=['bye'])
def bye_cmd(message: Message):
    bot.send_message(message.chat.id, 'Пока! всегда буду рад тебе (∩︵∩)')

@bot.message_handler(commands=['emoji'])
def emoji_cmd(message: Message):
    custom_emojis = ["¯_(ツ)_/¯", "(╯°□°）╯︵ ┻━┻", "ಠ_ಠ", "(¬‿¬)", "(ง'̀-'́)ง", "ʕ•ᴥ•ʔ", "( •_•)>⌐■-■", "(⌐■_■)", " (◣_◢) ", "(~￣▽￣)~", "(✿ ♥‿♥)", "٩(͡๏̯͡๏)۶", "(╯︵╰,)", "(╯ಊ╰)", "٩(̾●̮̮̃̾•̃̾)۶"]
    em = random.choice(custom_emojis)
    bot.send_message(message.chat.id, em)   

@bot.message_handler(commands=['gen_pass'])
def gen_pass_cmd(message: Message):
    number = '1234567890'
    sogl = 'QWRTPSDFGHJKLZXCVBNMqwrtpsdfghjlkzxcvbnm'
    glas = 'EYUIOAeyuoai'
    symbols = '!@#$%^&*-=_+'
    password = ''
    for i in range(4):
        password += choice(sogl) + choice(glas)
    for i in range(5):
        password += choice(number)
    for i in range(3):
        password += choice(symbols)  
    bot.reply_to(message, password)

@bot.message_handler(commands=['knb'])
def knb_cmd(message: Message):
    bot.send_message(message.chat.id, 'Игра запустилась, напишите камень/ножницы/бумага или отмена(чтобы отменить игру)')
    bot.register_next_step_handler(message, knb_game)

def knb_game(message: Message):
    text = message.text.lower()
    if text == 'отмена':
        bot.send_message(message.chat.id, 'Игра остановлена, вам снова доступны все команды')
        return
    if text not in['камень', 'ножницы', 'бумага']:
        bot.send_message(message.chat.id, 'Вы написали что-то не то, игра остановлена, вам снова доступны все команды')
        return
    comp = random.choice(['камень', 'ножницы', 'бумага'])
    if text == comp:
        bot.send_message(message.chat.id,'Ничья, если хотите поиграть снова, напишите /knb')
        return
    elif (text == 'камень' and bot == 'ножницы') or (text == 'ножницы' and bot == 'бумага') or (text == 'бумага' and bot == 'камень'):
        bot.send_message(message.chat.id, "Вы победили, если хотите поиграть снова, напишите /knb")
        return
    else:
        bot.send_message(message.chat.id, 'Вы проиграли, если хотите поигратьснова, напишите /knb')
        return
    
@bot.massage_handler(command=['door'])
def door_cmd(message: Message):
    bot.send_message(message.chat.id, 'Игра запустилась, напишите 1/2/3(дабы выбрать дверь) или отмена(чтобы отменить игру)')
    bot.register_next_step_handler(message, door_game)

def door_game(message: Message):
    text = message.text.lower()
    if text == 'отмена':
        bot.send_message(message.chat.id, 'Игра остановлена, вам снова доступны все команды')
        return
    if text not in['1', '2', '3']:
        bot.send_message(message.chat.id, 'Вы написали что-то не то, игра остановлена, вам снова доступны все команды')
        return
    comp = random.choice(['1', '2', '3'])
    if text == comp:
        bot.send_message(message.chat.id,'Вы открыли дверь где находились сокровища, если хотите играть снова, напишите /door')
        return
    else:
        bot.send_message(message.chat.id, 'Вы открыли дверь,но вдруг под вами проваливается пол, к сожалению вы проиграли, если хотите поигратьснова, напишите /door')
        return




@bot.message_handler(commands=['help'])
def help_cmd(message: Message):
    text = "<b>Мои команды:</b>\n /start - <i>запуск бота</i>\n /coin - <i>монетка</i>\n /help - <i>все команды</i>\n /bye - <i>бот попрощается</i>\n /emoji - <i>рандомный эмоджи</i>\n /gen_pass - <i>генерация пароля</i>\n /knb - <i>игра кнб</i>\n /door - <i>игра двери<i>"
    bot.send_message(message.chat.id, text, parse_mode = 'html')
   

@bot.message_handler(func=lambda message: message.text == 'Привет')
def hello_text(message: Message):
    bot.send_message(message.chat.id, 'И тебе привет (∩︵∩)')
 
@bot.message_handler(func=lambda message: message.text == 'Как дела?')
def hay_text(message: Message):
    bot.send_message(message.chat.id, 'Лучше не бывает (｡◕‿◕｡)')



bot.infinity_polling()
