import random
import itertools
from datetime import datetime, timedelta

def UEFA_Champions_League():
    teams = ["Manchester City", "Manchester United", "Everton", "Liverpool FC",
             "Chelsea FC", "Barcelona", "Real Madrid", "Inter Milan", 
             "Paris Saint-Germain", "Juventus", "Borussia Dortmund", "Arsenal",
             "Aston Villa", "Sporting", "Flamengo", "Spartak"]

    random.shuffle(teams) #перемешка
    groups = [teams[i * 4:(i + 1) * 4] for i in range(4)] #формовка 4 групп по 4 команды

    year = datetime.now().year
    hour = random.randint(12, 22) #часы с 12 до 22
    minute = random.choice([0, 15, 30, 45]) #минуты: 0, 15, 30, 45
    start_date = datetime(year, 9, 14, hour, minute)

    for idx, group in enumerate(groups, 1): #вывод групп
        print("Группа {}: {}".format(idx, group))

    for idx, group in enumerate(groups, 1): #составление календаря игр
        print("Календарь игр для Группы {}:".format(idx))
        matches = list(itertools.combinations(group, 2))
        match_date = datetime(year, 9, 14)  #дата первой игры в группе
        times = [12, 14, 16, 18, 20, 22]  #возможные часы игр
        for match in matches:
            team1, team2 = match
            hour = random.choice(times)
            minute = random.choice([0, 15, 30, 45])
            current_match = match_date.replace(hour=hour, minute=minute) #для того чтобы время матчей было разное
            print(f"{current_match.strftime('%d/%m/%Y, %H:%M')} — {team1} vs {team2}") #dd/mm/yyyy HH:MM
            match_date += timedelta(weeks=2) 