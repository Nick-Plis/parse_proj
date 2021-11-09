import requests
from bs4 import BeautifulSoup
import time

URL = 'https://boxrec.com/en/ratings'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'accept': '*/*'}
session = requests.Session()

tr_list = []
td_list = []
boxers = []

#print(td_list[1].text, '\npoints: ', td_list[2].text, 'division: ', td_list[4].text, 'stance: ', td_list[8].text, 'residence: ', td_list[9].text)

def get_html(url, params=None):
    r = session.get(url, headers=HEADERS, params=params)
    return r


def auth():
    url = 'https://boxrec.com/en/login'
    params = {
        '_target_path': 'https://boxrec.com/',
        '_username': 'boxrec228@gmail.com',
        '_password': 'Boxrecparse228',
        'login[go]': ''
    }
    r = session.post(url, params).text


def auth2():
    url = 'https://boxrec.com/en/login'
    params = {
        '_target_path': 'https://boxrec.com/',
        '_username': 'boxrec1337@gmail.com',
        '_password': 'Boxrecparse1337',
        'login[go]': ''
    }
    r = session.post(url, params).text


def auth3():
    url = 'https://boxrec.com/en/login'
    params = {
        '_target_path': 'https://boxrec.com/',
        '_username': 'boxrec777@gmail.com',
        '_password': 'Boxrecparse777',
        'login[go]': ''
    }
    r = session.post(url, params).text


# find tbody, then find all tr and get them into a list as divided elements with index
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    tbody = soup.find('tbody')
    tr_list.append(tbody.find('tr'))
    for tr in tbody:
        tr_list.append(
            tr.findNext('tr')
        )
    #print(tr_list)


def td_jump(tr_list, min_points, max_points, min_age, max_age, division_ask, min_wins, max_wins, min_loses, max_loses, residence_ask):
    global boxers
    for tr in tr_list[0:25]:
        td_list = tr.find_all('td')
        name_part = td_list[1].find('a').get('href')
        name = "boxrec.com" + name_part
        points = float(td_list[2].text)
        wins_loses = td_list[6].find_all('span')
        wins = int(wins_loses[0].text)
        loses = int(wins_loses[1].text)

        if min_points <= points <= max_points:
            if td_list[5].text == '':
                pass
            else:
                age = int(td_list[5].text)
                if min_age <= age <= max_age:
                    if td_list[4] == '':
                        pass
                    else:
                        division = td_list[4].text
                        division = division.strip()
                        for i in division_ask:
                            if division == i:
                                if min_wins <= wins <= max_wins:
                                    if min_loses <= loses <= max_loses:
                                        if td_list[9].text == '':
                                            pass
                                        else:
                                            residence_full = td_list[9].find_all('a')
                                            if len(residence_full) > 1:

                                                residence = residence_full[-1].text
                                                for i in residence_ask:
                                                    if residence == i:
                                                        boxers.append(name)
                                                    else:
                                                        pass
                                            else:
                                                pass
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                pass
                else:
                    pass
        else:
            pass

    for tr in tr_list[27:52]:
        td_list = tr.find_all('td')
        name_part = td_list[1].find('a').get('href')
        name = "boxrec.com" + name_part
        points = float(td_list[2].text)
        wins_loses = td_list[6].find_all('span')
        wins = int(wins_loses[0].text)
        loses = int(wins_loses[1].text)

        if min_points <= points <= max_points:
            if td_list[5].text == '':
                pass
            else:
                age = int(td_list[5].text)
                if min_age <= age <= max_age:
                    if td_list[4] == '':
                        pass
                    else:
                        division = td_list[4].text
                        division = division.strip()
                        for i in division_ask:
                            if division == i:
                                if min_wins <= wins <= max_wins:
                                    if min_loses <= loses <= max_loses:
                                        if td_list[9].text == '':
                                            pass
                                        else:
                                            residence_full = td_list[9].find_all('a')
                                            if len(residence_full) > 1:

                                                residence = residence_full[-1].text
                                                for i in residence_ask:
                                                    if residence == i:
                                                        boxers.append(name)
                                                    else:
                                                        pass
                                            else:
                                                pass
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                pass
                else:
                    pass
        else:
            pass


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('div', class_='pagerElement')
    if pagination:
        return int(pagination[4].get_text())
    else:
        print('Error')


residence_ask = ['Portugal', 'Spain', 'France', 'Monaco', 'United Kingdom', 'Ireland', 'Iceland', 'Belgium', 'Netherlands', 'Luxembourg', 'Liechtenstein', 'Switzerland', 'Italy', 'San Marino', 'Malta', 'Austria', 'Germany', 'Denmark', 'Norway', 'Sweden', 'Finland', 'Czech Republic', 'Poland', 'Slovakia', 'Hungary', 'Slovenia', 'Croatia', 'Bosnia and Herzegovina', 'Montenegro', 'Serbia', 'Kosovo', 'Albania', 'Andorra', 'Macedonia', 'Greece', 'Bulgaria', 'Turkey', 'Romania', 'Moldova', 'Ukraine', 'Belarus', 'Latvia', 'Lithuania', 'Estonia', 'Armenia', 'Georgia', 'Azerbaijan']
#q = int(input("Number of countries: "))
#for i in range(q):
    #residence_input = input("Country: ")
    #residence_ask.append(residence_input)


min_points = float(input("Minimal points: "))
max_points = float(input("Maximal points: "))

division_ask = []
n = int(input("Number of divisions: "))
for i in range(n):
    convert = input("Division: ")
    convert.join('\n\n')
    division_ask.append(convert)

min_wins = int(input("Minimal wins: "))
max_wins = int(input("Maximal wins: "))

min_loses = int(input("Minimal loses: "))
max_loses = int(input("Maximal loses: "))

min_age = int(input("Minimal age: "))
max_age = int(input("Maximal age: "))

urls = []
border = 0



def parse(min_points, max_points, min_age, max_age, division_ask, min_wins, max_wins, min_loses, max_loses, residence_ask):
    urls = []
    border = 0
    global boxers
    global tr_list
    auth()
    html = get_html(URL)
    pages_count = get_pages_count(html.text)
    pages_count = pages_count * 50
    for i in range(0, pages_count+50, 50):
        x = f'https://boxrec.com/en/ratings?&offset={i}'
        urls.append(x)

    for url in urls:
        html = get_html(url)
        print(html.text)
        get_content(html.text)
        td_jump(tr_list, min_points, max_points, min_age, max_age, division_ask, min_wins, max_wins, min_loses, max_loses, residence_ask)
        tr_list = []
        session.cookies.clear()
        time.sleep(1)
        border = border + 1

    return boxers

'''
    try:
        for url in urls:
            html = get_html(url)
            get_content(html.text)
            td_jump(tr_list, min_points, max_points, min_age, max_age, division_ask, min_wins, max_wins, min_loses, max_loses, residence_ask)
            tr_list = []
            session.cookies.clear()
            time.sleep(1)
            border = border + 1

    except AttributeError:
        auth2()
        try:
            for url in urls[border:]:
                html = get_html(url)
                get_content(html.text)
                td_jump(tr_list, min_points, max_points, min_age, max_age, division_ask, min_wins, max_wins, min_loses, max_loses, residence_ask)
                tr_list = []
                session.cookies.clear()
                time.sleep(1)
                border = border + 1

        except AttributeError:
            auth3()
            try:
                for url in urls[border:]:
                    html = get_html(url)
                    get_content(html.text)
                    td_jump(tr_list, min_points, max_points, min_age, max_age, division_ask, min_wins, max_wins, min_loses, max_loses, residence_ask)
                    tr_list = []
                    session.cookies.clear()
                    time.sleep(1)
                    border = border + 1

            except AttributeError:
                # parse3(min_points, max_points, min_age, max_age, division_ask, min_wins, max_wins, min_loses, max_loses, residence_ask, border)
                print('Fucked up')

    return boxers
'''


'''
def parse2(min_points, max_points, min_age, max_age, division_ask, min_wins, max_wins, min_loses, max_loses, residence_ask, border):
    global urls
    global boxers
    global tr_list

    auth2()
    try:
        for url in urls:
            html = get_html(url)
            get_content(html.text)
            td_jump(tr_list, min_points, max_points, min_age, max_age, division_ask, min_wins, max_wins, min_loses, max_loses, residence_ask)
            tr_list = []
            session.cookies.clear()
            time.sleep(1)
            border = border + 1
        return boxers
    except AttributeError:
        parse3(min_points, max_points, min_age, max_age, division_ask, min_wins, max_wins, min_loses, max_loses, residence_ask, border)




def parse3(min_points, max_points, min_age, max_age, division_ask, min_wins, max_wins, min_loses, max_loses, residence_ask, border):
    global urls
    global boxers
    global tr_list
    auth3()

    try:
        for url in urls:
            html = get_html(url)
            get_content(html.text)
            td_jump(tr_list, min_points, max_points, min_age, max_age, division_ask, min_wins, max_wins, min_loses, max_loses, residence_ask)
            tr_list = []
            session.cookies.clear()
            time.sleep(1)
            border = border + 1
        return boxers
    except AttributeError:
        #parse3(min_points, max_points, min_age, max_age, division_ask, min_wins, max_wins, min_loses, max_loses, residence_ask, border)
        print('Fucked up')
'''



boxers_done = parse(min_points, max_points, min_age, max_age, division_ask, min_wins, max_wins, min_loses, max_loses, residence_ask)
print(boxers_done)
