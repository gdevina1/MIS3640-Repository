# Strings - Exercise 3

team = "Manchester United Football Club"
print(team.split(sep=None,maxsplit=2))
print(team.split(maxsplit=1))
print(team.split())

print(team.strip())
print(team.strip("Man"))

team = "Manchester United Football Club Club"
print(team.replace('Football','Futbol'))
print(team.replace('Club','Klump',1))


