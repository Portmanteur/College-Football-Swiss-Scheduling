import team
from team import *

import tournament
from tournament import *

import networkx as nx
# import matplotlib.pyplot as plt
from geopy.distance import geodesic

import pandas as pd
import os
import pickle

def get_all_teams():
  if os.path.exists('cfb_teams_df.pickle'):
    with open('cfb_teams_df.pickle', 'rb') as handle:
      df = pickle.load(handle)
  else:
    df = pd.read_csv("cfb_teams.csv", index_col="nickname")
    for team in df.index:
      df.loc[team,'wins'] = ''
      df.loc[team,'losses'] = ''
    with open('cfb_teams_df.pickle', 'wb') as handle:
      pickle.dump(df, handle)
  return df

def build_graph(teams_df):
  G = nx.Graph() 

  for nickname1 in teams_df.index:
    G.add_node(nickname1)
    for nickname2 in teams_df.index:
      if nickname1 == nickname2:
        break
      coord1 = eval(teams_df.loc[nickname1, 'coords'])
      coord2 = eval(teams_df.loc[nickname2, 'coords'])
      dist = geodesic(coord1, coord2).miles
      G.add_edge(nickname1, nickname2, weight=dist)
  return G

def get_graph(teams):
  if os.path.exists('cfb_distance_graph.pickle'):
    with open('cfb_distance_graph.pickle', 'rb') as handle:
      G = pickle.load(handle)
  else:
    G = build_graph(teams)    
    
    with open('cfb_distance_graph.pickle', 'wb') as handle:
      pickle.dump(G, handle)
  return G

def extract_csv_from_xlsx():
  xlsx = pd.ExcelFile('CFB.xlsx')
  df = pd.read_excel(xlsx, 'cfb_teams') 
  df.to_csv('cfb_teams.csv', index=False)

def start_tourney():
  teams = get_all_teams()
  cfb = Tournament(teams)
  cfb.simulate_tournament()

def get_d1_teams():
  d1_conference_list = [
    "AAC",
    "ACC-ATLANTIC",
    "ACC-COASTAL",
    "BIG 12",
    "BIG TEN-EAST",
    "BIG TEN-WEST",
    "CONF-USA",
    "I-1 IND.",
    "MAC-EAST",
    "MAC-WEST",
    "MWC-MOUNTAIN",
    "MWC-WEST",
    "PAC-12 NORTH",
    "PAC-12 SOUTH",
    "SEC-EAST",
    "SEC-wEST",
    "SUN BELT EAST",
    "SUN BELT WEST",
  ]
  df = get_all_teams()
  df = df[df['conference'].isin(d1_conference_list)]
  return df
  

def get_acc_teams():
  acc_teams = {
    "BC":
    Team("Boston College", 60.84, 42.337, -71.172),
    "Clem":
    Team("Clemson University", 85.58, 34.6837, -82.836),
    "Duke":
    Team("Duke University", 75.57, 36.0014, -78.9382),
    "FSU":
    Team("Florida State University", 84.33, 30.4419, -84.2986),
    "GT":
    Team("Georgia Institute of Technology", 99.43, 33.7756, -84.3963),
    "Lou":
    Team("University of Louisville", 80.41, 38.2123, -85.7585),
    "Mia":
    Team("University of Miami", 66.53, 25.7196, -80.2782),
    "UNC":
    Team("University of North Carolina at Chapel Hill", 74.07, 35.9049,
         -79.0469),
    "NCSU":
    Team("North Carolina State University", 75.01, 35.7847, -78.6821),
    # "ND":   Team("University of Notre Dame", 41.7056, -86.2353),
    "Pitt":
    Team("University of Pittsburgh", 78.02, 40.4442, -79.9532),
    "Syr":
    Team("Syracuse University", 71.72, 43.0392, -76.1351),
    "UVA":
    Team("University of Virginia", 65.12, 38.0356, -78.5055),
    "VPI":
    Team("Virginia Polytechnic Institute and State University", 64.29, 37.2284,
         -80.4234),
    "Wake":
    Team("Wake Forest University", 77.29, 36.1346, -80.2779),
  }
  return acc_teams

def start_acc_tourney():
  teams = get_acc_teams()
  acc = Tournament(teams)
  acc.simulate_tournament()
  