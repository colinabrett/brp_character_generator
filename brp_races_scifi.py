#!/usr/bin/env python3
#
# Generate stats for a human character in BRP
#dice_roll = straight_dice(number_of_dice, number_of_sides, mods, verbose)
#STR [9] CON [6] SIZ [9] INT [15] POW [13] DEX [15] APP [11] EDU [13]

import sys, getopt, math, random

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

from dice_roller import *

STR = CON = SIZ = INT = POW = DEX = APP = EDU = 0

#
# Function definitions
#

def scifi_human_stats():
    stats = {
       'STR':straight_dice(3,6,0),\
       'CON':straight_dice(3,6,0),\
       'SIZ':straight_dice(2,6,6),\
       'INT':straight_dice(2,6,6),\
       'POW':straight_dice(3,6,0),\
       'DEX':straight_dice(3,6,0),\
       'APP':straight_dice(3,6,0),\
       'EDU':straight_dice(3,6,0)
    }
    return stats

def scifi_eldar_stats():
    stats = {
       'STR':straight_dice(2,6,2),\
       'CON':straight_dice(3,6,0),\
       'SIZ':straight_dice(2,4,4),\
       'INT':straight_dice(3,6,6),\
       'POW':straight_dice(2,6,6),\
       'DEX':straight_dice(3,6,3),\
       'APP':straight_dice(3,6,0),\
       'EDU':straight_dice(3,6,0)
    }
    return stats

def scifi_squat_stats():
    stats = {
       'STR':straight_dice(4,6,0),\
       'CON':straight_dice(1,6,12),\
       'SIZ':straight_dice(1,4,4),\
       'INT':straight_dice(2,6,6),\
       'POW':straight_dice(3,6,0),\
       'DEX':straight_dice(3,6,0),\
       'APP':straight_dice(3,6,0),\
       'EDU':straight_dice(3,6,0)
    }
    return stats

def scifi_ork_stats():
    stats = {
       'STR':straight_dice(4,6,0),\
       'CON':straight_dice(3,6,0),\
       'SIZ':straight_dice(2,6,2),\
       'INT':straight_dice(3,6,0),\
       'POW':straight_dice(2,6,3),\
       'DEX':straight_dice(4,6,0),\
       'APP':straight_dice(2,6,0),\
       'EDU':straight_dice(2,6,0)
    }
    return stats

def scifi_gretchin_stats():
    stats = {
       'STR':straight_dice(2,6,0),\
       'CON':straight_dice(3,6,0),\
       'SIZ':straight_dice(2,6,0),\
       'INT':straight_dice(3,6,0),\
       'POW':straight_dice(2,6,3),\
       'DEX':straight_dice(4,6,0),\
       'APP':straight_dice(2,6,0),\
       'EDU':straight_dice(2,6,0)
    }
    return stats

def scifi_wookiee_stats():
    stats = {
       'STR':straight_dice(3,6,6),\
       'CON':straight_dice(3,6,3),\
       'SIZ':straight_dice(3,6,8),\
       'INT':straight_dice(3,6,0),\
       'POW':straight_dice(3,6,0),\
       'DEX':straight_dice(3,6,0),\
       'APP':straight_dice(2,6,3),\
       'EDU':straight_dice(2,6,6)
    }
    return stats

def scifi_grey_stats():
    stats = {
       'STR':straight_dice(1,6,3),\
       'CON':straight_dice(2,6,0),\
       'SIZ':straight_dice(1,6,3),\
       'INT':straight_dice(2,6,12),\
       'POW':straight_dice(3,6,0),\
       'DEX':straight_dice(3,6,3),\
       'APP':straight_dice(1,6,1),\
       'EDU':straight_dice(2,6,6)
    }
    return stats

def scifi_gungan_stats():
    stats = {
       'STR':straight_dice(3,6,0),\
       'CON':straight_dice(3,6,3),\
       'SIZ':straight_dice(3,6,3),\
       'INT':straight_dice(3,6,0),\
       'POW':straight_dice(3,6,0),\
       'DEX':straight_dice(3,6,0),\
       'APP':straight_dice(3,6,0),\
       'EDU':straight_dice(2,6,6)
    }
    return stats

def scifi_zabrak_stats():
    stats = {
       'STR':straight_dice(3,6,0),\
       'CON':straight_dice(3,6,0),\
       'SIZ':straight_dice(2,6,6),\
       'INT':straight_dice(2,6,6),\
       'POW':straight_dice(3,6,0),\
       'DEX':straight_dice(3,6,0),\
       'APP':straight_dice(3,6,0),\
       'EDU':straight_dice(2,6,6)
    }
    return stats

