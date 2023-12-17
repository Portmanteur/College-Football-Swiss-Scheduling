
import team, tournament, swiss
from team import *
from tournament import *
from swiss import *

import pandas as pd
import openpyxl
from geopy.distance import geodesic

from random import random

# swiss.start_tourney()

# teams = get_all_teams()
teams = get_d1_teams()
# G = get_graph(teams)


cfb = Tournament(teams)
cfb.simulate_tournament()
print(cfb.teams.iloc[0])

while cfb.teams.iloc[0].team != "Georgia Tech":
  teams = get_d1_teams()
  cfb = Tournament(teams)
  cfb.simulate_tournament()
  print(cfb.teams.iloc[0])

# pairings = cfb.get_pairings()

#pair_df = pd.DataFrame(data=pairings)
#print(pair_df.head())
#pair_df.to_csv("round1_pairings.csv", index=False)

# for team_a, team_b in pairings:
#   break

# print(team_a, team_b)


# spread = teams.loc[team_a,'rating'] - teams.loc[team_b,'rating']
# team_a_win_prob = spread * 0.025 + 0.5

# rng = random()
# winner = team_a if rng < team_a_win_prob else team_b
# loser = team_b if rng < team_a_win_prob else team_a

# teams.loc[winner,'wins']+=loser+' '
# teams.loc[loser,'losses']+=winner+' '
# # loser.losses.append(winner.nickname)

# teams.loc[winner,'score'] += 1

# print(teams.loc[team_a])

# cfb.simulate_round()

# df = cfb.teams.sort_values(['score','rating'], ascending=[False,False])
# df.to_csv('round1_standings.csv',index=False)

# cfb.update_distances()
# pairings = cfb.get_pairings()

# pair_df = pd.DataFrame(data=pairings)
# print(pair_df.head())
# pair_df.to_csv("round2_pairings.csv", index=False)

# cfb.simulate_round()

# df = cfb.teams.sort_values(['score','rating'], ascending=[False,False])
# df.to_csv('round2_standings.csv',index=False)