import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    # print("JSON-muotoinen vastaus:")
    # print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    # print("Oliot:")

    # for player in players:
    #     print(player)


    nationality="FIN"
    print(f"players from {nationality}: ")
    for player in players:

        if player.nationality == nationality:
            print(f"{player.name} team {player.team} games {player.games} goals {player.goals} assists {player.assists}")

if __name__ == "__main__":
    main()