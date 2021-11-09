
import time
import telebot
import parser_box
from parser_box import parse


residence_ask = []
division_ask = []
min_points = 0.0
max_points = 0.0
min_wins = 0
max_wins = 0
min_loses = 0
max_loses = 0
min_age = 0
max_age = 0


bot = telebot.TeleBot('1833912470:AAHHphxHxqt-cBT6JLfMx_G3UAiLSlNHk8U')

from telebot import types

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='State', callback_data='state'))
    markup.add(telebot.types.InlineKeyboardButton(text='Region', callback_data='region'))
    bot.send_message(message.chat.id, text="Region/state?", reply_markup=markup)
    bot.register_next_step_handler(message, residence_answer)


def residence_answer(message):
    global residence_ask
    if message.text == 'State':
        bot.send_message(message.chat.id, text="Input states:", reply_to_message_id='state_x')
        residence_ask = message.text.split(', ')
        bot.register_next_step_handler(message, division_analyse)

    elif message.text == 'Region':
        markup_region = types.ReplyKeyboardMarkup()
        markup_region.add(telebot.types.InlineKeyboardButton(text='Europe', callback_data='europe'))
        markup_region.add(telebot.types.InlineKeyboardButton(text='North America', callback_data='north_america'))
        markup_region.add(telebot.types.InlineKeyboardButton(text='South America', callback_data='south_america'))
        markup_region.add(telebot.types.InlineKeyboardButton(text='Asia', callback_data='asia'))
        markup_region.add(telebot.types.InlineKeyboardButton(text='Oceania', callback_data='oceania'))
        markup_region.add(telebot.types.InlineKeyboardButton(text='Africa', callback_data='africa'))
        markup_region.add(telebot.types.InlineKeyboardButton(text='CIS', callback_data='cis'))
        markup_region.add(telebot.types.InlineKeyboardButton(text='World', callback_data='world'))
        bot.send_message(message.chat.id, text="Choose from below:", reply_markup=markup_region)
        region = message.text
        if region == 'Europe':
            residence_ask = ['Portugal', 'Spain', 'France', 'Monaco', 'United Kingdom', 'Ireland', 'Iceland', 'Belgium',
                             'Netherlands', 'Luxembourg', 'Liechtenstein', 'Switzerland', 'Italy', 'San Marino', 'Malta',
                             'Austria', 'Germany', 'Denmark', 'Norway', 'Sweden', 'Finland', 'Czech Republic', 'Poland',
                             'Slovakia', 'Hungary', 'Slovenia', 'Croatia', 'Bosnia and Herzegovina', 'Montenegro', 'Serbia',
                             'Kosovo', 'Albania', 'Andorra', 'Macedonia', 'Greece', 'Bulgaria', 'Turkey', 'Romania', 'Moldova',
                             'Ukraine', 'Belarus', 'Latvia', 'Lithuania', 'Estonia', 'Armenia', 'Georgia', 'Azerbaijan',
                             'Gibraltar']

        elif region == 'North America':
            residence_ask = ['Canada', 'USA', 'Mexico']

        elif region == 'South America':
            residence_ask = ['Guatemala', 'Belize', 'Honduras', 'Cuba', 'Dominican Republic', 'Puerto Rico', 'Costa Rica',
                             'Panama', 'Colombia', 'Venezuela', 'Ecuador', 'Peru', 'Guyana', 'Suriname', 'Brazil', 'Bolivia',
                             'Paraguay', 'Chile', 'Argentina', 'Uruguay', 'Bermuda', 'Haiti', 'Jamaica', 'Dominica', 'Grenada',
                             'Barbados']

        elif region == 'Asia':
            residence_ask = ['Israel', 'Syria', 'Lebanon', 'Jordan', 'Saudi Arabia', 'UAE', 'Oman', 'Yemen', 'Qatar', 'Kuwait',
                             'Iraq', 'Iran', 'Afghanistan', 'Turkmenistan', 'Uzbekistan', 'Kazakhstan', 'Kyrgyzstan', 'Tajikistan',
                             'Pakistan', 'India', 'Nepal', 'China', 'Mongolia', 'Bhutan', 'Sri Lanka', 'Bangladesh', 'Myanmar',
                             'Thailand', 'Malaysia', 'Cambodia', 'Vietnam', 'Laos', 'Singapore', 'North Korea', 'South Korea',
                             'Japan', 'Taiwan', 'Philippines', 'Indonesia', 'Macao', 'Hong Kong']
        elif region == 'Oceania':
            residence_ask = ['Papua New Guinea', 'Australia', 'New Zealand', 'Fiji', 'Haiti']

        elif region == 'Africa':
            residence_ask = ['South Africa', 'Namibia', 'Botswana', 'Zimbabwe', 'Mozambique', 'Madagascar', 'Zambia',
                             'Angola', 'Gabon', 'Equatorial Guinea', 'DRC', 'Rwanda', 'Burundi', 'Tanzania', 'Kenya',
                             'Uganda', 'Cameroon', 'Central African Republic', 'South Sudan', 'Ethiopia', 'Somalia',
                             'Djibouti', 'Eritrea', 'Sudan', 'Chad', 'Niger', 'Nigeria', 'Benin', 'Togo', 'Ghana',
                             'Côte D’Ivoire', 'Liberia', 'Guinea', 'Gambia', 'Senegal', 'Mali', 'Morocco', 'Algeria',
                             'Tunisia', 'Libya', 'Egypt', 'Lesotho', 'Malawi']

        elif region == 'CIS':
            residence_ask = ['Ukraine', 'Russia', 'Latvia', 'Lithuania', 'Estonia', 'Moldova', 'Kazakhstan', 'Kyrgyzstan',
                             'Uzbekistan', 'Tajikistan', 'Turkmenistan', 'Armenia', 'Georgia', 'Azerbaijan', 'Belarus']

        elif region == 'World':
            residence_ask = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Argentina', 'Armenia', 'Aruba',
                             'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
                             'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana',
                             'Brazil', 'Brunei', 'Bulgaria', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic',
                             'Chad', 'Chile', 'China', 'Colombia', 'Comoros' , 'Congo', 'Cook Island', 'Costa Rica', 'Côte D’Ivoire',
                             'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Democratic Republic Of The Congo', 'Denmark', 'Djibouti',
                             'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Eritrea', 'Estonia', 'Ethiopia',
                             'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece',
                             'Greenland', 'Grenada', 'Guatemala', 'Guinea', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland',
                             'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan',
                             'Kazakhstan', 'Kenya', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho',
                             'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia', 'Madagascar',
                             'Malawi', 'Malaysia', 'Mali', 'Malta', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro',
                             'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nepal', 'Netherlands', 'New Zeland', 'Nicaragua',
                             'Niger', 'Nigeria', 'North Korea', 'Norway', 'Oman', 'Pakistan', 'Palestina', 'Panama',
                             'Papua New Guinea', 'Paraguay', 'Peru', 'Phillipines', 'Poland', 'Portugal', 'Puerto Rico',
                             'Qatar', 'Romania', 'Russia', 'Rwanda', 'San Marino', 'Saudi Arabia', 'Senegal', 'Serbia',
                             'Singapore', 'Slovakia', 'Slovenia', 'Somalia', 'South Africa', 'South Korea', 'South Sudan',
                             'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan',
                             'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Tunisia', 'Turkey', 'Turkmenistan', 'Uganda',
                             'Ukraine', 'United Arab Emirates', 'United Kingdom', 'Uruguay', 'USA', 'Uzbekistan', 'Venezuela',
                             'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']

        bot.register_next_step_handler(message, division_analyse)


# @bot.message_handler(content_types=['text'])
# def residence_input(message):
    # residence = message.text
    # bot.send_message(message.chat.id, text=residence)
    # division_analyse(message)


def division_analyse(message):
    global division_ask
    markup_division = types.ReplyKeyboardMarkup()
    markup_division.add(telebot.types.InlineKeyboardButton(text='minimum', callback_data='1'))
    markup_division.add(telebot.types.InlineKeyboardButton(text='light fly', callback_data='2'))
    markup_division.add(telebot.types.InlineKeyboardButton(text='fly', callback_data='3'))
    markup_division.add(telebot.types.InlineKeyboardButton(text='super fly', callback_data='4'))
    markup_division.add(telebot.types.InlineKeyboardButton(text='bantam', callback_data='5'))
    markup_division.add(telebot.types.InlineKeyboardButton(text='super bantam', callback_data='6'))
    markup_division.add(telebot.types.InlineKeyboardButton(text='feather', callback_data='7'))
    markup_division.add(telebot.types.InlineKeyboardButton(text='super feather', callback_data='8'))
    markup_division.add(telebot.types.InlineKeyboardButton(text='light', callback_data='9'))
    markup_division.add(telebot.types.InlineKeyboardButton(text='super light', callback_data='10'))
    markup_division.add(telebot.types.InlineKeyboardButton(text='welter', callback_data='11'))
    markup_division.add(telebot.types.InlineKeyboardButton(text='super welter', callback_data='12'))
    markup_division.add(telebot.types.InlineKeyboardButton(text='middle', callback_data='13'))
    markup_division.add(telebot.types.InlineKeyboardButton(text='super middle', callback_data='14'))
    markup_division.add(telebot.types.InlineKeyboardButton(text='light heavy', callback_data='15'))
    markup_division.add(telebot.types.InlineKeyboardButton(text='cruiser', callback_data='16'))
    markup_division.add(telebot.types.InlineKeyboardButton(text='heavy', callback_data='17'))

    bot.send_message(message.chat.id, text="Choose division from below, type '-' to stop:", reply_markup=markup_division)
    division_ask = message.text.split(', ')
    # bot.send_message(message.chat.id, text=division)
    bot.register_next_step_handler(message, abc)


def abc(message):
    message = bot.send_message(message.chat.id, text="Input minimal points:", reply_to_message_id='points_min')
    bot.register_next_step_handler(message, points_analyse_min)


def points_analyse_min(message):
    global min_points
    # bot.send_message(message.chat.id, text="Input minimal points:", reply_to_message_id='points_min')
    min_points = float(message.text)
    if min_points < 0:
        bot.send_message(message.chat.id, text="Wrong points")
        abc(message)
    else:
        # bot.register_next_step_handler(message, points_analyse_max)
        cba(message)


def cba(message):
    bot.send_message(message.chat.id, text="Input maximal points:", reply_to_message_id='points_max')
    bot.register_next_step_handler(message, points_analyse_max)


def points_analyse_max(message):
    global max_points
    # bot.send_message(message.chat.id, text="Input maximal points:", reply_to_message_id='points_max')
    max_points = float(message.text)
    if max_points < min_points:
        bot.send_message(message.chat.id, text="Wrong points")
        cba(message)
    else:
        # bot.register_next_step_handler(message, points_analyse_max)
        klm(message)


def klm(message):
    message = bot.send_message(message.chat.id, text="Input minimal wins:", reply_to_message_id='win_min')
    bot.register_next_step_handler(message, wins_analyse_min)


def wins_analyse_min(message):
    global min_wins
    # bot.send_message(message.chat.id, text="Input minimal points:", reply_to_message_id='points_min')
    min_wins = int(message.text)
    if min_wins < 0:
        bot.send_message(message.chat.id, text="Wrong number of wins")
        klm(message)
    else:
        # bot.register_next_step_handler(message, points_analyse_max)
        mlk(message)


def mlk(message):
    bot.send_message(message.chat.id, text="Input maximal wins:", reply_to_message_id='win_max')
    bot.register_next_step_handler(message, wins_analyse_max)


def wins_analyse_max(message):
    global max_wins
    # bot.send_message(message.chat.id, text="Input maximal points:", reply_to_message_id='points_max')
    max_wins = int(message.text)
    if max_wins < min_wins:
        bot.send_message(message.chat.id, text="Wrong number of wins")
        mlk(message)
    else:
        # bot.register_next_step_handler(message, points_analyse_max)
        zxc(message)


def zxc(message):
    message = bot.send_message(message.chat.id, text="Input minimal loses:", reply_to_message_id='lose_min')
    bot.register_next_step_handler(message, lose_analyse_min)


def lose_analyse_min(message):
    global min_loses
    # bot.send_message(message.chat.id, text="Input minimal points:", reply_to_message_id='points_min')
    min_loses = int(message.text)
    if min_loses < 0:
        bot.send_message(message.chat.id, text="Wrong number of loses")
        zxc(message)
    else:
        # bot.register_next_step_handler(message, points_analyse_max)
        cxz(message)


def cxz(message):
    bot.send_message(message.chat.id, text="Input maximal loses:", reply_to_message_id='lose_max')
    bot.register_next_step_handler(message, loses_analyse_max)


def loses_analyse_max(message):
    global max_loses
    # bot.send_message(message.chat.id, text="Input maximal points:", reply_to_message_id='points_max')
    max_loses = int(message.text)
    if max_loses < min_loses:
        bot.send_message(message.chat.id, text="Wrong number of loses")
        cxz(message)
    else:
        # bot.register_next_step_handler(message, points_analyse_max)
        # points_analyse_max(message)
        xyn(message)


def xyn(message):
    message = bot.send_message(message.chat.id, text="Input minimal age:", reply_to_message_id='age_min')
    bot.register_next_step_handler(message, age_analyse_min)


def age_analyse_min(message):
    global min_age
    # bot.send_message(message.chat.id, text="Input minimal points:", reply_to_message_id='points_min')
    min_age = int(message.text)
    if min_age < 0:
        bot.send_message(message.chat.id, text="Wrong age")
        xyn(message)
    else:
        # bot.register_next_step_handler(message, points_analyse_max)
        nyx(message)


def nyx(message):
    bot.send_message(message.chat.id, text="Input maximal age:", reply_to_message_id='age_max')
    bot.register_next_step_handler(message, age_analyse_max)


def age_analyse_max(message):
    global max_age
    # bot.send_message(message.chat.id, text="Input maximal points:", reply_to_message_id='points_max')
    max_age = int(message.text)
    if max_age < min_age:
        bot.send_message(message.chat.id, text="Wrong age")
        nyx(message)
    else:
        # bot.register_next_step_handler(message, points_analyse_max)
        # points_analyse_max(message)
        print("start parsing")
        boxers = parse(min_points, max_points, min_age, max_age, division_ask, min_wins, max_wins, min_loses, max_loses, residence_ask)
        print(boxers)


while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e)
        time.sleep(15)


