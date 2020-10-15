# url = "https://www.espncricinfo.com/series/8048/game/1216531/royal-challengers-bangalore-vs-kings-xi-punjab-31st-match-indian-premier-league-2020-21"

from bs4 import BeautifulSoup
import requests, sched, time

def fetchScore():
    source = requests.get("https://www.espncricinfo.com/series/8048/game/1216531/royal-challengers-bangalore-vs-kings-xi-punjab-31st-match-indian-premier-league-2020-21"
).text
    soup = BeautifulSoup(source, 'lxml')
    score = soup.find('div', class_='score-run').text.split('/')
    team = soup.find('a', class_='team-name').span['title']
    print(f"Batting team : {team}")
    print(f"Wickets: {score[1]} Runs: {score[0]}")
    schedule.enter(60, 1, fetchScore)

schedule = sched.scheduler(time.time, time.sleep)
schedule.enter(1, 1, fetchScore)
schedule.run()