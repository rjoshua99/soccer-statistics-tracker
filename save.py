import json

def save_json(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent = 4)
    print(f"Saved to {filename}")

import csv

def save_standngs_csv(data, filename):
    table = data["standings"][0]["table"]

    with open(filename, "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerow(["Position", "Team", "Played", "Won", "Draw", "Points"])

    for team in table:
        writer.writerow([
            team["position"],
            team["team"]["name"],
            team["playedGames"],
            team["won"],
            team["draw"],
            team["lost"],
            team["points"]

        ])

def save_scorers_csv(data, filename):
    scorers = data["scorers"]

    if(len(scorers)==0):
          print("Scorer data is currently unavailable")
          return 

    with open(filename, "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerow(["Player", "Team", "Goals"])

        for scorer in scorers:
         writer.writerow([
         scorer["player"]["name"],
         scorer["team"]["name"],
         scorer["goals"]
        ])


def save_matches_csv(data, filename):
    matches = data["matches"]

    with open(filename, "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerow(["Matchday", "Home Team", "Away Team", "Status", "Home Score", "Away Score", "Date"])



        for match in matches:
            matchday = match["matchday"]
            home = match["homeTeam"]["name"]
            away = match["awayTeam"]["name"]
            status = match["status"]
            date = match["utcDate"]
                
        
            if status == "FINISHED":
                home_score = match["score"]["fullTime"]["home"]
                away_score = match["score"]["fullTime"]["away"]
        
            else:
                home_score = ""
                away_score = ""
    
                writer.writerow([matchday,home, away, status, home_score, away_score, date])
        
    
        
if __name__ == "__main__":
    from api import get_scorers, get_matches

    scorers_data = get_scorers()
    save_scorers_csv(scorers_data, "scorers.csv")


    matches_data = get_matches()
    save_matches_csv(matches_data, "matches.csv")
        
        
    

              
              

