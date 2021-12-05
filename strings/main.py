# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part 1
scorer_0 = "Ruud Gullit"
scorer_1 = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = scorer_0 + " " + str(goal_0) + ", " + scorer_1 + " " + str(goal_1)
print(scorers)

report = f"{scorer_0} scored in the {goal_0}nd minute" "\n" f"{scorer_1} scored in the {goal_1}th minute"
print(report)

# Part 2

player = "Erwin Koeman"

print(player.find("Erwin"))
first_name = player[0:5]
print(first_name)

print(player.find("Koeman"))
last_name_len = len(player[6:])
print(last_name_len)

name_short = player[0] + ". " + player[6:]
print(name_short)

chant = (len(first_name) * (first_name + "! ")).rstrip()
print(chant)

good_chant = chant[-1]  != " "
print(good_chant)
