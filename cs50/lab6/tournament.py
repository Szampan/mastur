# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000


def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    # TODO: Read teams into memory from file
    
    filename = sys.argv[1]
    print(f"File name is {filename}")

    with open(filename, mode='r') as f:
        reader = csv.DictReader(f)  #csv.DictReader tworzy słownik z każdej linijki wg schematu {'team': 'x', 'rating': 'y'}
        for country in reader:
            #print(country["team"])
            country['rating'] = int(country['rating'])
            teams.append(country)

    #print("######")
    #print("TEAMS list:")
    #for j in teams:
    #    print(j)



    counts = {}
    # TODO: Simulate N tournaments and keep track of win counts

    for s in range(N):
        sim_winner = simulate_tournament(teams)
        print(f"Round's {s+1} winner is: {sim_winner}")
        if sim_winner in counts:
            counts[sim_winner] += 1
        else:
            counts[sim_winner] = 1
    print("#####")
    print(counts)
    print("#####")



    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # TODO
    while len(teams) > 1:        
        teams = simulate_round(teams)
    winner = teams[0]['team']
    return winner

if __name__ == "__main__":
    main()
