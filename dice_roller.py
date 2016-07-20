#!/usr/bin/env python3
#
# Dice Roller Module
#

import sys, getopt, math, random

#
# Straight Dice roll and total with modifiers
#
def straight_dice(number_of_dice = 1, number_of_sides = 6 , modifiers = 0, verbose = False):
    if verbose:
        print ("FUNCTION: Straight dice")
        print ("Rolling ", number_of_dice, "d", number_of_sides, " with ", modifiers, " mods", sep="")
    i = 1
    roll_total = 0
    sum = 0
    while i <= int(number_of_dice):
        roll = int(random.random() * int(number_of_sides)) + 1
        if verbose:
            print (roll)
        sum = sum + roll
        i += 1
    roll_total = sum + int(modifiers)
    if verbose:
        print ("Total = ", sum)
        print ("Modified total = ", roll_total)
    return roll_total


#
# Drop Low (Straight Dice roll and total with modifiers then drop lowest die roll)
#
def drop_low(number_of_dice = 1, number_of_sides = 6 , modifiers = 0, verbose = False):
    if verbose:
        print ("FUNCTION: Drop Low")
        print ("Rolling ", number_of_dice, "d", number_of_sides, " with ", modifiers, " mods", sep="")
    i = 1
    roll_total = 0
    min = int(number_of_sides)
    sum = 0
    while i <= int(number_of_dice):
        roll = int(random.random() * int(number_of_sides)) + 1
        if verbose:
            print (roll)
        if roll < min:
            min = roll
        sum = sum + roll
        i += 1
    roll_total = sum + int(modifiers)
    if verbose:
        print ("Total = ", sum)
        print ("Modified total = ", sum + int(modifiers))
        print ("Lowest roll = ", min)
        print ("Total with lowest roll dropped = ", roll_total - min)
    return roll_total - min


#
# Drop High (Straight Dice roll and total with modifiers then drop highest die roll)
#
def drop_high(number_of_dice = 1, number_of_sides = 6 , modifiers = 0, verbose = False):
    if verbose:
        print ("FUNCTION: Drop High")
        print ("Rolling ", number_of_dice, "d", number_of_sides, " with ", modifiers, " mods", sep="")
    i = 1
    roll_total = 0
    sum = 0
    max = 1
    while i <= int(number_of_dice):
        roll = int(random.random() * int(number_of_sides)) + 1
        if verbose:
            print (roll)
        if roll > max:
            max = roll
        sum = sum + roll
        i += 1
    roll_total = sum + int(modifiers)
    if verbose:
        print ("Total = ", sum)
        print ("Modified total = ", roll_total)
        print ("Highest roll = ", max)
        print ("Total with highest roll dropped = ", roll_total - max)
    return roll_total - max


