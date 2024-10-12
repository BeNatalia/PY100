list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
#fst_team = list_players[1::2]
#sec_team = list_players[-2::-2]
#print(fst_team, sec_team, sep='\n')

fst_team_2 = list_players[:3]
sec_team_2 = list_players[3:]
print(fst_team_2, sec_team_2, sep='\n')
