#
# game system classes
# defines the basics of the character sheet
#
from dice_roller import *
from brp_stats import *
from decimal import Decimal, ROUND_HALF_UP

class GameSystem():
        def __init__(self):
                self.statblock = {}
                self.derived = {}
                self.skills = {}
                self.supressed_skills = []
                self.supressed_stats = {}
                self.bonuses = {}

        def calculateStats(self, statslist):
                """modify STATS if they exist in the statblock eg. statslist {'STR':'2d6', 'EDU':'2d8'}"""
                for attribute, value in statslist.items():
                        if attribute in self.statblock:
                                if not isinstance(value, int):
                                        self.statblock[attribute] = straight_dice(*parseDiceString(value))
                                else:
                                        self.statblock[attribute] = value
                return

        def calculateDerived(self) :
                """calculate the derived stats from the game system"""
                return

        def calculateBonuses(self) :
                """calculate skill bonuses"""
                return

        def modifySkill(self, skill, modifier) :
                """change the value of a known skill, or add a new skill and base value to the list"""
                return

        def supressSkill(self, skill):
                """remove a skill from the base list for a particular genre"""
                return

        def supressStat(self, stat):
                """remove a stat from the base list for a particular genre eg. no EDU in a fantasy game"""
                # for a stat to be added it should be in the statblock and not in the suppressed_stats list
                ustat = stat.upper()
                if ustat in self.statblock and ustat not in self.supressed_stats:
                        self.supressed_stats.append(ustat)
                return

class Brp(GameSystem):
        def __init__(self):
                """constructor for BRP character"""
                self.statblock = {
                        'STR':0,\
                        'CON':0,\
                        'SIZ':0,\
                        'INT':0,\
                        'POW':0,\
                        'DEX':0,\
                        'APP':0,\
                        'EDU':0
                }
                # note these are lifted straight from brp_skills.py
                self.skills = {'Appraise' : 15,\
                               'Art' : 5,\
                               'Artillery' : 0,\
                               'Bargain' :  5,\
                               'Brawl' : 25,\
                               'Climb' : 40,\
                               'Command' : 5,\
                               'Craft'  : 5,\
                               'Demolition' : 1,\
                               'Disguise' : 1,\
                               'Dodge' : self.statblock["DEX"] * 2,\
                               'Drive Common' : 20,\
                               'Drive Rare' : 1,\
                               'Energy Weapon' : 0,\
                               'Etiquette' : 5,\
                               'Fast Talk' : 5,\
                               'Fine Manipulation' : 5,\
                               'Firearm' : 0,\
                               'First Aid' : 30,\
                               'Fly Gear' : self.statblock["DEX"] / 2,\
                               'Fly Wings' : self.statblock["DEX"] * 4,\
                               'Gaming' : self.statblock["INT"] + self.statblock["POW"],\
                               'Grapple' : 25,\
                               'Heavy Machine'  : 1,\
                               'Heavy Weapon'  : 0,\
                               'Hide' : 10,\
                               'Insight' : 5,\
                               'Jump' : 25,\
                               'Knowledge Common'  : 5,\
                               'Knowledge Rare'  : 1,\
                               'Language Other' : 0,\
                               'Language Own' : 0,\
                               'Listen' : 25,\
                               'Literacy INT' : self.statblock["INT"] * 4,\
                               'Literacy EDU' : self.statblock["POW"] * 4,\
                               'Martial Arts' : 1,\
                               'Medicine Modern' : 5,\
                               'Medicine Ancient' : 0,\
                               'Melee Weapon' :  0,\
                               'Missile Weapon' :  0,\
                               'Navigate' : 10,\
                               'Parry'  : 0,\
                               'Perform'  : 5,\
                               'Persuade' : 15,\
                               'Pilot'  : 1,\
                               'Projection' : self.statblock["DEX"] * 2,\
                               'Psychotherapy Common' : 1,\
                               'Psychotherapy Rare' : 0,\
                               'Repair' :  15,\
                               'Research' : 25,\
                               'Ride' :  5,\
                               'Science' : 1,\
                               'Sense' :  10,\
                               'Shield' : 0,\
                               'Sleight of Hand' : 5,\
                               'Spot' : 25,\
                               'Status' : 15,\
                               'Stealth' : 10,\
                               'Strategy' : 1,\
                               'Swim' : 25,\
                               'Teach' : 10,\
                               'Technical Skill Ancient' :  0,\
                               'Technical Skill Rare' :  1,\
                               'Technical Skill Common' :  5,\
                               'Throw' : 25,\
                               'Track' : 10 }
                self.supressed_stats = []
                self.bonuses = {}

        def calculateBonuses(self):
                """calculate BRP skill category bonuses"""
                skill_groups = {
                'Combat' : {'primary' : ['DEX'], 'secondary' : ['INT','STR'], 'negative' : []},\
                'Communication' : {'primary' : ['INT'], 'secondary' : ['POW','APP'], 'negative' : []},\
                'Manipulation': {'primary' : ['DEX'], 'secondary' : ['INT','STR'], 'negative' : []},\
                'Mental': {'primary' : ['INT'], 'secondary' : ['POW'], 'negative' : []},\
                'Perception': {'primary' : ['INT'], 'secondary' : ['POW','CON'], 'negative' : []},\
                'Physical': {'primary' : ['DEX'], 'secondary' : ['STR','CON'], 'negative' : ['SIZ']}
                }
                if 'EDU' not in self.supressed_stats:
                        skill_groups['Mental']['secondary'].append('EDU')
                        
                for category,modifiers in skill_groups.items():
                        bonus = 0
                        primary = modifiers['primary']
                        secondary = modifiers['secondary']
                        negative = modifiers['negative']
                        for stat in primary:
                                bonus += calculate_primary_bonus(self.statblock[stat])
                        for stat in secondary:
                                bonus += calculate_secondary_bonus(self.statblock[stat])
                        for stat in negative:
                                bonus -= calculate_primary_bonus(self.statblock[stat])
                        self.bonuses[category] = bonus
                        
        def calculateDerived(self):
                """calculate rolls and stats derived from attributes. Supercedes rolls() in brp_stats"""
                self.derived = {
                        'Damage Bonus': damage_bonus(self.statblock['STR'], self.statblock['SIZ']),\
                        'Hit Points' : int(Decimal((self.statblock['CON'] + self.statblock['SIZ'])/2).quantize(0, ROUND_HALF_UP)),\
                        'Experience Bonus' : int(Decimal(self.statblock['INT']/2).quantize(0, ROUND_HALF_UP)),\
                        'Effort Roll' : self.statblock['STR'] * 5,\
                        'Stamina Roll' : self.statblock['CON'] * 5,\
                        'Idea Roll' : self.statblock['INT'] * 5,\
                        'Luck Roll' : self.statblock['POW'] * 5,\
                        'Agility Roll' : self.statblock['DEX'] *5,\
                        'Charisma Roll' : self.statblock['APP'] *5\
                        }
                self.derived['Major Wound level'] = int(Decimal(self.derived['Hit Points']/2).quantize(0, ROUND_HALF_UP))
                if 'EDU' not in self.supressed_stats:
                                self.derived['Know Roll'] = self.statblock['EDU'] * 5

    
    
            
        
    
