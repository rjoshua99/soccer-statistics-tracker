def show_standings(data):
    table = data["standings"][0]["table"]

    print(f"{'Pos':<5}{'Team:<25'}{'P:<5'}{'W':<5}{'D':<5'}{'L':<5}{'Pts':<5}")

    for team in table:
     position = team["position"]
     name = team["team"]["name"]
     played = team["playedGames"]
     won = team["won"]
     draw = team["draw"]
     lost = team["lost"]
     points = team["points"]

     print(f"{position:<5}{name:<25}{played:<5}{won:<5}{draw:<5}{lost:<5}{points:<5}")


def show_scorers(data):
   scorers = data["scorers"]

   if(len(scorers)==0):
      print("Scorer data is currently unavailable")
      return 

   print(f"{'Player':<25}{'Team':<25}{'Goals':<7}")
    
   for scorer in scorers:
    name = scorer["player"]["name"]
    team = scorer["team"]["name"]
    goals = scorer["goals"]
    print(f"{name:<25}{team:<25}{goals:<7}")

if __name__ == "__main__":
  from api import get_scorers
  data = get_scorers()
  show_scorers(data)


def show_matches(data):
    matches = data["matches"]

    for match in matches:
       matchday = match["matchday"]
       home = match["homeTeam"]["name"]
       away = match["awayTeam"]["name"]
       status = match["status"]
        

       if status == "FINISHED":
        home_score = match["score"]["fullTime"]["home"]
        away_score = match["score"]["fullTime"]["away"]
        print(f"MD{matchday}: {home} {home_score} - {away_score} {away}")

       else:
        date = match["utcDate"]
        print(f"MD{matchday}: {home} vs {away} ({status} - {date})")


if __name__ == "__main__":
  from api import get_matches, get_scorers
  matches_data = get_matches()
  show_matches(matches_data)

  scorers_data = get_scorers()
  show_scorers(scorers_data)