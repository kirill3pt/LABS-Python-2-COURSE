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
    match_hours = [12, 14, 16, 18, 20, 22]
    match_minutes = [0, 15, 30, 45]
    start_date = datetime(year, 9, 14)

    for idx, group in enumerate(groups, 1): #вывод групп
        print("Группа {}: {}".format(idx, group))

    for idx, group in enumerate(groups, 1):
        print(f"Календарь игр для Группы {idx}:")
        match_date = start_date

        for team1, team2 in itertools.combinations(group, 2):
            # выбираем случайное время для каждого матча
            current_match = match_date.replace(
                hour=random.choice(match_hours),
                minute=random.choice(match_minutes)
            )
            print(f"{current_match.strftime('%d/%m/%Y, %H:%M')} — {team1} vs {team2}")
            match_date += timedelta(weeks=2)