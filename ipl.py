import numpy as np
import pandas as pd

# ipl_matches= "ipl-matches.csv" # Path to the file
ipl_matches= "https://docs.google.com/spreadsheets/d/e/2PACX-1vTgCcxYBcqxUAuYHgrqUPsdXpausK3AF-B712JJaGHHA6BKtN3LCuoiJ1VQakm_umUU1nNkxy2K79QA/pub?output=csv"
matches=pd.read_csv(ipl_matches)

#print(matches.head(5))

def teamsapi():
    teams= list(matches.Team1.unique())
    teams_dict= {
        "teams": teams
    }   
    return teams_dict

def teamsvsteams(team1, team2):
    valid_teams= list(matches.Team1.unique())
    if team1 and team2 in valid_teams:
        temp_df=matches[(matches['Team1']==team1) & (matches['Team2']==team2) | (matches['Team1']==team2) & (matches['Team2']==team1)]
        total_matches=temp_df.shape[0]
        matches_wonby_team1=int(temp_df['WinningTeam'].value_counts()[team1])
        matches_wonby_team2=int(temp_df['WinningTeam'].value_counts()[team2])

        draws=total_matches-matches_wonby_team1-matches_wonby_team2

        response={
            "team1": team1,
            "team2": team2,
            "total_matches": total_matches,
            "team1_wins": matches_wonby_team1,
            "team2_wins": matches_wonby_team2,
            "draws": draws
        }
        return response
    else:
        return {"message": "Invalid team names"}

      


