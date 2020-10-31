# There are 10 animals in a hen coop. 6 of them are chickens and the rest are roosters. Write a program that calculates and prints how many roosters there are?
num_hen = int(input("Enter number of hen: "))
num_roosters = 10 - num_hen
print(num_roosters, "roosters exist in the hen coop")