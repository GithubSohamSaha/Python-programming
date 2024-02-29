def sort_dictionary_by_runs(batsmen):
    sorted_batsmen = sorted(batsmen.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_batsmen)

def display_batsman_with_max_runs(batsmen):
    max_runs_batsman = max(batsmen, key=batsmen.get)
    print(f"Batsman with maximum runs: {max_runs_batsman}")

def display_batsmen_names(batsmen):
    print("Names of batsmen:")
    for batsman in batsmen:
        print(batsman)

def add_new_batsman(batsmen, name, runs):
    batsmen[name] = runs
    print(f"Added {name} with {runs} runs.")

def remove_batsman_with_lowest_runs(batsmen):
    if not batsmen:
        print("Dictionary is empty. Cannot remove batsman.")
        return

    min_runs_batsman = min(batsmen, key=batsmen.get)
    del batsmen[min_runs_batsman]
    print(f"Removed {min_runs_batsman} with lowest runs.")

# Define the dictionary to store batsmen and their runs
batsmen = {
    "Player1": 100,
    "Player2": 200,
    "Player3": 150,
    "Player4": 50,
    "Player5": 300,
    "Player6": 250,
    "Player7": 180,
    "Player8": 120
}

# (a) Sort the dictionary in descending order of runs
sorted_batsmen = sort_dictionary_by_runs(batsmen)
print("Sorted batsmen by runs:", sorted_batsmen)

# (b) Display name of the batsman with maximum runs
display_batsman_with_max_runs(batsmen)

# (c) Display only the names of batsmen
display_batsmen_names(batsmen)

# (d) Add a new batsman
add_new_batsman(batsmen, "Player9", 220)

# (e) Remove the batsman having lowest runs
remove_batsman_with_lowest_runs(batsmen)
