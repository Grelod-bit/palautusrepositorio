from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"

    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    nation="FIN"
    players = stats.top_scorers_by_nationality(nation)

    print(f"Players from {nation} ")
    print("")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()