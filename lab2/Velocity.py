#Write a program that solves the following problem: There are two cars that start at the same time and drive towards each other. Velocity of the cars are fixed at 80 km/h and 70 km/h. At the beginning, the distance between the cars is 490 km. After how many minutes will the distance between them be 150 km?
firstcar_velocity = float(input("Please, enter first car's velocity: "))
secondcar_velocity = float(input("Please, enter second car's velocity: "))
distance_total = float(input("Please, enter initial distance: "))
distance_desired = float(input("Please, enter desired distance: "))
time_passing = (distance_total-distance_desired)//(firstcar_velocity+secondcar_velocity)
print("The time passing: ", time_passing, "hours")