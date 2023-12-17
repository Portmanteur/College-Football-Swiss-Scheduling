
from geopy.distance import geodesic
from random import random

class Team:
  def __init__(self, name, rating, lat, lon):
    self.name = name
    self.nickname = ""
    self.lat = lat
    self.lon = lon
    self.coords = (lat, lon)
    self.score = 0
    self.rating = rating
    self.wins = ""
    self.losses = ""
    self.opponents = set()

  def __str__(self):
    return self.name

  def __repr__(self):
    return self.name
 
def determine_winner(team_a, team_b, verbose=False):
  spread = team_a.rating - team_b.rating
  team_a_win_prob = spread * 0.025 + 0.5
   
  if verbose:
    print(f"{team_a.name} has a {team_a_win_prob} chance of winning")
  
  rng = random()
  if verbose:
    print(rng)
  
  winner = team_a if rng < team_a_win_prob else team_b
  loser = team_b if rng < team_a_win_prob else team_a
  
  if verbose:
    print(f"{winner.name} wins!") 

  return (winner, loser)


