import random

# Return a list of integers with length `num_dice`.
# Each integer in the returned list is a random number between
# 1 and 6, inclusive.

def roll_dice(num_dice):
 
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results


# Calcuate the total of numbers dice rolled
def total(roll_result):

    sum = 0
    for roll in roll_result:
        sum += roll

    return sum


# Calculate the average
def ave(roll_result):

    ave = sum(roll_results) / len(roll_result)
    return ave


################################################

while(1):

    num_times = int(input("How many times would u like to roll the dice? "))
    print("Rolling the dice " + str(num_times) + " times.")
    roll_results = roll_dice(num_times)
    print("The numbers rolled are: ", roll_results)
    total_results = total(roll_results)
    print("Total sum of numbers rolled are: ", total_results)
    ave_results = ave(roll_results)
    print("Average number of numbers rolled are: ", ave_results)
    roll_again = input("Do you want to roll the dice again? (y/n):")
    if roll_again != 'y':
        print("Exit the game. Bye!")
        break

###############################################

# Write rolls to the file, append new rolls to existing rolls
with open('file.txt', 'a') as f:
    f.write("".join(str(item) for item in roll_results))


# Read rolls from the file display list of rolls, total and average.
with open('file.txt', 'r') as r:
    file_content = r.read()
    file_content = list(file_content)
    file_content = list(map(int, file_content))
    print("The rolls read from the file:",file_content)
    total_results = total(file_content)
    print("Total number of rolls from the file", total_results)
    avg_results = ave(file_content)
    print("Average number of rolls from the file", avg_results)
