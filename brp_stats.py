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

def rolls(incoming_stats):
    char_rolls = {
        'Effort' : incoming_stats['STR'] * 5 ,\
        'Stamina' : incoming_stats['CON'] * 5 ,\
        'Idea' : incoming_stats['INT'] * 5 ,\
        'Luck' : incoming_stats['POW'] * 5 ,\
        'Agility' : incoming_stats['DEX'] * 5 ,\
        'Charisma' : incoming_stats['APP'] * 5 ,\
        'Know' : incoming_stats['EDU'] * 5
    }
    return char_rolls

def scm(incoming_stats):
# Magic World
    bonuses = {
        'Physical' : int(incoming_stats['STR'] / 2 + 0.5 ) ,\
        'Communication' : int(incoming_stats['APP'] / 2 + 0.5 ) ,\
        'Knowledge' : int(incoming_stats['INT'] / 2 + 0.5 ) ,\
        'Manipulation' : int(incoming_stats['DEX'] / 2 + 0.5 ) ,\
        'Perception' : int(incoming_stats['CON'] / 2 + 0.5 ) 
    }
    return bonuses

def calculate_primary_bonus(i):
    a = i
    bonus = 0
    bonus = a - 10
    return bonus

def calculate_secondary_bonus(i):
    a = i
    bonus = 0
    if ( a < 10 ) or ( a > 10 ):
        bonus = int ( ( a - 10 ) / 2 )
    else:
        bonus = 0
    return bonus
       
def calculate_stat_bonuses(incoming_stats):
    b = {
        'pSTR':calculate_primary_bonus(incoming_stats['STR']) ,\
        'pCON':calculate_primary_bonus(incoming_stats['CON']),\
        'pSIZ':calculate_primary_bonus(incoming_stats['SIZ']),\
        'pINT':calculate_primary_bonus(incoming_stats['INT']),\
        'pPOW':calculate_primary_bonus(incoming_stats['POW']),\
        'pDEX':calculate_primary_bonus(incoming_stats['DEX']),\
        'pAPP':calculate_primary_bonus(incoming_stats['APP']),\
        'pEDU':calculate_primary_bonus(incoming_stats['EDU']),\
        'sSTR':calculate_secondary_bonus(incoming_stats['STR']),\
        'sCON':calculate_secondary_bonus(incoming_stats['CON']),\
        'sSIZ':calculate_secondary_bonus(incoming_stats['SIZ']),\
        'sINT':calculate_secondary_bonus(incoming_stats['INT']),\
        'sPOW':calculate_secondary_bonus(incoming_stats['POW']),\
        'sDEX':calculate_secondary_bonus(incoming_stats['DEX']) ,\
        'sAPP':calculate_secondary_bonus(incoming_stats['APP']) ,\
        'sEDU':calculate_secondary_bonus(incoming_stats['EDU']) 
    }
    return b


def scb(incoming_stats):
# BRP
    sb = calculate_stat_bonuses(incoming_stats)
    skill_groups = {
        'Combat': sb['pDEX'] + sb['sINT'] + sb['sSTR'] ,\
        'Communication': sb['pINT'] + sb['sPOW'] + sb['sAPP'] ,\
        'Manipulation': sb['pDEX'] + sb['sINT'] + sb['sSTR'] ,\
        'Mental': sb['pINT'] + sb['sPOW'] + sb['sEDU'] ,\
        'Perception': sb['pINT'] + sb['sPOW'] + sb['sCON'] ,\
        'Physical': sb['pDEX'] + sb['sSTR'] + sb['sCON'] - sb['sSIZ']
    }
    return skill_groups

import math
def damage_bonus(str,siz):
    """calculate damage bonus from STR and SIZ, return string damage bonus"""
    db = "None"
    combined = int(str) + int(siz)
    if combined <= 40 :
        if combined <= 12:
            db = '-1D6'
        elif combined <= 16:
            db = '-1D4'
        elif combined <= 24:
            db = 'None'
        elif combined <= 32:
            db = '+1D4'
        elif combined <= 40:
            db = '+1D6'
        else:
            db = 'None'
    else:
        #add dice 6 per 16
        n = 1 + math.ceil((combined-40)/16)
        db = '+{0}D6'.format(n)
    return db
