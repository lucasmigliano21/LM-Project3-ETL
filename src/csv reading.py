from src import functions as fn
import pandas as pd

results=pd.read_csv('./data/results_teams.csv')

fn.column_cleaning(results)

results = fn.filter(results)

results = fn.winner(results)

results_csv=fn.copy(results)

results_csv.to_csv('./data/results.csv', index=False)

