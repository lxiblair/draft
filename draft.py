import csv
import numpy as np
import pandas as pd
from operator import itemgetter
# You may or may not want to use this package, or others like it
# this is just a starting point for you
from sklearn.linear_model import LinearRegression

# Read the player database into an array of dictionaries
players = []
with open('playerDB.csv', mode='r') as player_csv:
    player_reader = csv.DictReader(player_csv)
    line_count = 0
    for row in player_reader:
        players.append(dict(row))


# Read the draft database into an array of dictionaries
draftPicks = []
with open('draftDB.csv', mode='r') as draft_csv:
    draft_reader = csv.DictReader(draft_csv)
    line_count = 0
    for row in draft_reader:
        draftPicks.append(dict(row))



# Get the draft picks to give/receive from the user
# You can assume that this input will be entered as expected
# DO NOT CHANGE THESE PROMPTS
print("\nSelect the picks to be traded away and the picks to be received in return.")
print("For each entry, provide 1 or more pick numbers from 1-60 as a comma-separated list.")
print("As an example, to trade the 1st, 3rd, and 25th pick you would enter: 1, 3, 25.\n")
give_str = input("Picks to give away: ")
receive_str = input("Picks to receive: ")

# Convert user input to an array of ints
give_picks = list(map(int, give_str.split(',')))
receive_picks = list(map(int, receive_str.split(',')))

# Success indicator that you will need to update based on your trade analysis
success = True


# YOUR SOLUTION GOES HERE

# assign each player a value 
# first solution: average rank across all seasons played 

new_players = sorted(players, key=itemgetter('Player'))

prev = new_players[0]['Player']
count = 1
total_rank = int(new_players[0]['Rk'])

player_arr = []

# make array of (name, avg rank)
for i in range(1, len(new_players)):
  curr_player = new_players[i]['Player']

  if curr_player == prev: 
    count = count + 1
    total_rank = total_rank + int(new_players[i]['Rk'])
  else: 
    avg_rank = total_rank / count
    tup = ({'namePlayer':prev, 'rank': avg_rank})
    player_arr.append(tup)

    prev = new_players[i]['Player']
    count = 1
    total_rank = int(new_players[i]['Rk'])



# join name, rank with draft attributes
pd_players = pd.DataFrame(player_arr)
pd_picks = pd.DataFrame(draftPicks)

new_table = pd.merge(pd_players, pd_picks, on='namePlayer')


# create a dict of players and draft picks
draft_dict = {}
num_picks = 240

for i in range(num_picks):
  arr = []
  draft_dict[i] = arr

length = len(new_table)

for i in range(length):
  num_pick = new_table.at[i, 'numberPickOverall']
  player_name = new_table.at[i, 'namePlayer']
  player_rank = new_table.at[i, 'rank']
  tup = ({'name': player_name, 'rank': player_rank})
  draft_dict[int(num_pick)].append(tup)

# x is draft pic values, y is avg rank of draft pics
x = np.arange(240)
y = []
y = np.array([], dtype=np.float128)
# np.x = []
# np.y = []

print(num_picks2
      )
for i in range(num_picks):
  print("in loop")
  
  totalrank = 0
  value = draft_dict[i]

  if len(value) == 0:
    np.y.append(0)
  else: 
    for j in value:
      totalrank = totalrank + j['rank']
    avgrank = totalrank / len(value)
    np.y.append(avgrank)


print(len(y))
print(len(x))
x = x.reshape((-1, 1))
model = LinearRegression()
model.fit(x, y)
model = LinearRegression().fit(x, y)
# y_pred = model.predict(np.x)

print('intercept:', model.intercept_)
print('slope:', model.coef_)





# Print feeback on trade
# DO NOT CHANGE THESE OUTPUT MESSAGES
if success:
    print("\nTrade result: Success! This trade receives more value than it gives away.\n")
    # Print additional metrics/reasoning here
else:
    print("\nTrade result: Don't do it! This trade gives away more value than it receives.\n")
    # Print additional metrics/reasoning here

