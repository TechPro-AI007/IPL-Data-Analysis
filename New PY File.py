import pandas as pd

# Load the data
df = pd.read_csv(r'C:\Users\HP\OneDrive\Documents\matches.csv')

print("\n" + "="*40)
print("       IPL ALL-TIME MVPs (MOST POTM)      ")
print("="*40)

# Calculate the top 5 players with the most Player of the Match awards
top_players = df['player_of_match'].value_counts().head(5)

# Print the player leaderboard
for rank, (player, awards) in enumerate(top_players.items(), 1):
    print(f"🌟 Rank {rank}: {player} ({awards} Awards)")

print("="*40 + "\n")