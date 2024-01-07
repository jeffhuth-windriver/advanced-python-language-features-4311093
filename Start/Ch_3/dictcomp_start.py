# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate how to use dictionary comprehensions


# define a list of temperature values
ctemps = [0, 12, 34, 100]

# TODO: Use a comprehension to build a dictionary
temp_dict = {t: (t*9/5) + 32 for t in ctemps if t<100}
print(temp_dict)
print(temp_dict[12])

# TODO: Merge two dictionaries with a comprehension
team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
team2 = {"White": 12, "Macke": 88, "Perce": 4}

new_team = {key: val for team in (team1, team2) for key, val in team.items()}
print(new_team)