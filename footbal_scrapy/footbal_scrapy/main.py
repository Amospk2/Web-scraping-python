import pandas as pd
from bs4 import BeautifulSoup
import requests

def format_location(text):
    text = text[:text.find('Attendance:')]
    return text

def format_gols(gols):
    try:
        gols = gols.replace('\xa0', '')
        gols = gols.split('\n')
        gols.remove('')
    except:
        pass

    return gols

def get_matchs_from_year(year):
    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'
    request = requests.get(web)
    content = request.text
    soup = BeautifulSoup(content, 'lxml')

    matches = soup.find_all('div', class_="footballbox")

    date = []
    home = []
    away = []
    score = []
    location = []
    home_gols = []
    away_gols = []

    for match in matches:
        home.append(match.find('th', class_="fhome").get_text())
        score.append(match.find('th', class_="fscore").get_text())
        away.append(match.find('th', class_="faway").get_text())
        date.append(match.find('div', class_="fdate").get_text())
        location.append(format_location(match.find('div', class_="fright").get_text()))
        home_gols.append(format_gols(match.find('td', class_="fhgoal").get_text()))
        away_gols.append(format_gols(match.find('td', class_="fagoal").get_text()))



    dict_football = {'home':home, 'score':score, 'away':away, 
                     'date':date, 'location':location, 
                     'home_gols':home_gols, "away_gols":away_gols
                    }
    df = pd.DataFrame(dict_football)
    return df


years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974,
        1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014,
        2018]

fifa_world_cup = [get_matchs_from_year(year) for year in years]
df_fifa_cup = pd.concat(fifa_world_cup, ignore_index=True)
df_fifa_cup.to_csv("fifa_world_cup_matchs.csv", index=False)




