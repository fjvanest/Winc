# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#Create a variable for every player that scored, for example:
from gettext import find


goal_scorer_0 = "Ruud Gullit"
goal_scorer_1 = "Marco van Basten"

#Create a variable for each minute of the match that a goal was scored in, for example:
goal_0 = 32
goal_1 = 54

"""
Using the +-operator, create a string that reports on who scored when, according to the format:
<scorer_name> <when_they_scored>, <scorer_name> <when_they_scored>
"""
scorers = f"{goal_scorer_0} {goal_0}, {goal_scorer_1} {goal_1}"
scorers_plus = goal_scorer_0 + " " + str(goal_0) + ", " + goal_scorer_1 + " " + str(goal_1)
print(scorers_plus)

# Use f-strings or the +-operator to create a single string with information about who scored when in the format:

# <scorer_name> scored in the <when_they_scored>nd minute
# <scorer_name> scored in the <when_they_scored>th minute
# The result should be stored in a variable report.

report = f'{goal_scorer_0} scored in the {goal_0}nd minute\n{goal_scorer_1} scored in the {goal_1}th minute'
print(report)

# Store the following values in the given variable, and do each of those exercises in a single line of code. Make sure that your code still produces the correct results for different values for the player  value.
# 1. Choose a player that played in the soccer match and store his name as a string in the variable player.
player = "David van den Berg"

# 2.first_name: use slicing and the find-method (help) to isolate and store the player's first name.
first_name_x = player.find(" ")
first_name = player[0:first_name_x]

# 3. last_name_len: use find, slicing and len to isolate and store the length of their last name.
last_name_x = first_name_x + 1
last_name = player[last_name_x:]
last_name_len = len(last_name)

# 4. name_short: isolate and store the player's name in this format:
# G. von Examplestein
name_short = player[0:1] + ". " + last_name
print(name_short)

# 5. chant: this is what the crowd chants when it looks like your player is going to score a goal -- their first name plus an exclamation mark(!), x-times, where x is the number of characters in their first name. 
# Make sure the last character of this string is not a space! For our example player:
# Gut! Gut! Gut!
amount_chant = len(first_name)
chant_pre = ((first_name + "! ") * amount_chant) 
chant = chant_pre[:-1]
print(chant)

# 6. good_chant: Make super-sure the last character of chant is not a space by using the inequality operator (!=). Try this in your REPL for an example: print(2 != 3). Also try: print(2 != 2).
good_chant =(chant[-1] != " ")
print(good_chant)

