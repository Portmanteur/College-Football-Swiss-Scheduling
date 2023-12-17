import networkx as nx
from geopy.distance import geodesic
# import polars as pl
from math import sqrt
import pandas as pd

from team import *
# import team
import swiss


class Tournament:

  def __init__(self, teams_df):
    self.teams = teams_df
    self.round = 0
    self.G = swiss.get_graph(teams_df)
    self.H = self.G.copy()

  def get_pairings(self):
    pairings = nx.min_weight_matching(self.H)
    pair_df = pd.DataFrame(data = pairings)
    pair_df.to_csv(f"round{ self.round }_pairings.csv", index=False)
    return pairings

  def simulate_round(self):
    self.round += 1
    pairings = self.get_pairings()
    
    for team_a, team_b in pairings:    
      spread = self.teams.loc[team_a,'rating'] - self.teams.loc[team_b,'rating']
      team_a_win_prob = spread * 0.025 + 0.5
     
      rng = random()
      winner = team_a if rng < team_a_win_prob else team_b
      loser = team_b if rng < team_a_win_prob else team_a

      self.teams.loc[winner,'score'] += 1
      self.teams.loc[winner,'wins'] += loser+' '
      self.teams.loc[loser,'losses'] += winner+' '
      
      self.G.remove_edge(team_a, team_b)

  def get_standings(self):
    pass
    # Convert the dictionary to a list of dicts
    # data = [{
    #   "name": name,
    #   # "rating": team.rating,
    #   "score": team.score,
    #   "wins": team.wins,
    #   "losses": team.losses
    # } for name, team in self.teams.items()]

    # Create a Polars DataFrame
    # df = pl.DataFrame(data)

    # Sort the DataFrame by score:
    # df_sorted = df.sort("score")

    # Reverse the DataFrame to make it in descending order:
    # df_sorted = df_sorted[::-1]

    # return df_sorted

  def update_distances(self):
    #if team_a = team_b:
    #   break
    # if team_a.home == 'AA'
    self.H = self.G.copy()
    for team1 in self.teams.index:
      for team2 in self.teams.index:
        if team1 == team2:
          continue
        if not self.H.has_edge(team1, team2):
          continue
        diff = self.teams.loc[team1,'score'] - self.teams.loc[team2,'score']
        if diff > 0:
          self.H[team1][team2]["weight"] *= (diff + 1)

  def simulate_tournament(self):

    while self.round < 12:
      self.simulate_round()
      self.update_distances()

      # df = self.get_standings()
      self.teams = self.teams.sort_values( ['score','rating'], ascending=[False,False])
      self.teams.to_csv(f"round{ self.round }_standings.csv")
      print(f"Round {self.round} complete")
      
      # choice = input(f"Start round {self.round}? (y/n): ")
      # if choice.lower() != 'y':
      #   break
