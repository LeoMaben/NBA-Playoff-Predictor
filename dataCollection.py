import pandas as pd


def getEasternStandings(tables):
    return tables[0]

def getWesternStandings(tables):
    return tables[1]

def getPerGameStats(tables):
    return tables[4]

def getTotalStats(tables):
    return tables[6]

def getPer100Stats(tables):
    return tables[8]



stats_url = "https://www.basketball-reference.com/leagues/NBA_2025.html"
playoffs_url = "https://www.basketball-reference.com/playoffs/NBA_2025.html"

stat_tables = pd.read_html(stats_url)
matchup_tables = pd.read_html(playoffs_url)

print(stat_tables)
