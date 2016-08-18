#
# game system classes
# defines the basics of the character sheet
#
from dice_roller import *
from brp_stats import *
from decimal import Decimal, ROUND_HALF_UP
from improvement import *
from brp_skills import *
#from coc_skills import *
#from mw_skills import *
class GameSystem():
        def __init__(self):
                self.statblock = {}
                self.derived = {}
                self.skills = {}
                self.modified_skills = {}
                self.suppressed_skills = []
                self.suppressed_stats = []
                self.bonuses = {}
                self.skill_points = 0

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


        def modifyBaseSkill(self, skill, modifier) :
                """change the value of a known skill, or add a new skill and base value to the list"""
                return

        def suppressSkill(self, skill):
                """remove a skill from the base list for a particular genre"""
                if skill in self.skills.keys():
                        self.suppressed_skills.append(skill.title())

        def suppressStat(self, stat):
                """remove a stat from the base list for a particular genre eg. no EDU in a fantasy game"""
                # for a stat to be added it should be in the statblock and not in the suppressed_stats list
                ustat = stat.upper()
                if ustat in self.statblock and ustat not in self.suppressed_stats:
                        self.suppressed_stats.append(ustat)
                return

        def improve(self, improvement):
                """Apply the skills of an Improvement to the modified skills attribute"""
                # allocate the skill points first if it's a ProfessionImprovement
                if hasattr(improvement, "allocateSkillPoints") and callable(getattr(improvement, "allocateSkillPoints")):
                        improvement.allocateSkillPoints(self.skill_points)
                for skill, value in improvement.getSkills().items():
                        # ignore subskills - everything after a '('
                        if '(' in skill:
                                essential_skill = skill.rpartition('(')[0].strip()
                        else:
                                essential_skill = skill
                        
                        if self.modified_skills.get(skill) and self.modified_skills.get(skill) > self.skills.get(essential_skill, 0):
                                self.modified_skills[skill] += value
                        else:
                                self.modified_skills[skill] = self.skills.get(essential_skill, 0) + value

        def randomSkill(self):
                """pick a random skill from those available."""
                skill_list = set(self.skills.keys()) - set(self.suppressed_skills)
                skill = random.sample(skill_list, 1)
                return skill[0]
                
        
class Brp(GameSystem):
        def __init__(self, power_level='Normal'):
                """constructor for BRP character"""
                power_levels = {
                        'Normal' : { 'points' : 250, 'EDU' : 20, 'max' : 75 },
                        'Heroic' : { 'points' : 325, 'EDU' : 25, 'max' : 90 },
                        'Epic' : { 'points' : 400, 'EDU' : 30, 'max' : 101 },
                        'Superhuman' : { 'points': 500, 'EDU' : 40, 'max': 9999}
                }
                self.power_level = power_levels.get( power_level, 'Normal')
                self.statblock = {
                        'STR':0,
                        'CON':0,
                        'SIZ':0,
                        'INT':0,
                        'POW':0,
                        'DEX':0,
                        'APP':0,
                        'EDU':0
                }
                # note these are lifted straight from brp_skills.py
                self.skills = {'Appraise' : 15,
                               'Art' : 5,
                               'Artillery' : 0,
                               'Bargain' :  5,
                               'Brawl' : 25,
                               'Climb' : 40,
                               'Command' : 5,
                               'Craft'  : 5,
                               'Demolition' : 1,
                               'Disguise' : 1,
                               'Dodge' : self.statblock["DEX"] * 2,
                               'Drive' : 20,
                               'Drive Rare' : 1,
                               'Energy Weapon' : 0,
                               'Etiquette' : 5,
                               'Fast Talk' : 5,
                               'Fine Manipulation' : 5,
                               'Firearm' : 0,
                               'First Aid' : 30,
                               'Fly Gear' : self.statblock["DEX"] / 2,
                               'Fly Wings' : self.statblock["DEX"] * 4,
                               'Gaming' : self.statblock["INT"] + self.statblock["POW"],
                               'Grapple' : 25,
                               'Heavy Machine'  : 1,
                               'Heavy Weapon'  : 0,
                               'Hide' : 10,
                               'Insight' : 5,
                               'Jump' : 25,
                               'Knowledge'  : 5,
                               'Knowledge Rare'  : 1,
                               'Language Other' : 0,
                               'Language Own' : 0,
                               'Listen' : 25,
                               'Literacy INT' : self.statblock["INT"] * 4,
                               'Literacy EDU' : self.statblock["POW"] * 4,
                               'Martial Arts' : 1,
                               'Medicine Modern' : 5,
                               'Medicine Ancient' : 0,
                               'Melee Weapon' :  0,
                               'Missile Weapon' :  0,
                               'Navigate' : 10,
                               'Parry'  : 0,
                               'Perform'  : 5,
                               'Persuade' : 15,
                               'Pilot'  : 1,
                               'Projection' : self.statblock["DEX"] * 2,
                               'Psychotherapy' : 1,
                               'Psychotherapy Rare' : 0,
                               'Repair' :  15,
                               'Research' : 25,
                               'Ride' :  5,
                               'Science' : 1,
                               'Sense' :  10,
                               'Shield' : 0,
                               'Sleight of Hand' : 5,
                               'Spot' : 25,
                               'Status' : 15,
                               'Stealth' : 10,
                               'Strategy' : 1,
                               'Swim' : 25,
                               'Teach' : 10,
                               'Technical Skill Ancient' :  0,
                               'Technical Skill Rare' :  1,
                               'Technical Skill' :  5,
                               'Throw' : 25,
                               'Track' : 10 }
                self.skill_points = 0
                self.suppressed_stats = []
                self.bonuses = {}
                self.improvements = []
                self.modified_skills = {}
                self.suppressed_skills = []

        def calculateBaseSkills(self):
                self.skills = brp_skill_bases()
                
        def calculateSkillPoints(self):
                """Skill points are derived from campaign power level and EDU if it's present; otherwise a fixed pool based on campaign power level"""
                if 'EDU' not in self.suppressed_stats:
                        self.skill_points = self.statblock['EDU'] * self.power_level['EDU']
                else:
                        self.skill_points = self.power_level['points']
        
        def calculateBonuses(self):
                """calculate BRP skill category bonuses"""
                skill_groups = {
                'Combat' : {'primary' : ['DEX'], 'secondary' : ['INT','STR'], 'negative' : []},
                'Communication' : {'primary' : ['INT'], 'secondary' : ['POW','APP'], 'negative' : []},
                'Manipulation': {'primary' : ['DEX'], 'secondary' : ['INT','STR'], 'negative' : []},
                'Mental': {'primary' : ['INT'], 'secondary' : ['POW'], 'negative' : []},
                'Perception': {'primary' : ['INT'], 'secondary' : ['POW','CON'], 'negative' : []},
                'Physical': {'primary' : ['DEX'], 'secondary' : ['STR','CON'], 'negative' : ['SIZ']}
                }
                if 'EDU' not in self.suppressed_stats:
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
                        'Damage Bonus': damage_bonus(self.statblock['STR'], self.statblock['SIZ']),
                        'Hit Points' : int(Decimal((self.statblock['CON'] + self.statblock['SIZ'])/2).quantize(0, ROUND_HALF_UP)),
                        'Experience Bonus' : int(Decimal(self.statblock['INT']/2).quantize(0, ROUND_HALF_UP)),
                        'Effort Roll' : self.statblock['STR'] * 5,
                        'Stamina Roll' : self.statblock['CON'] * 5,
                        'Idea Roll' : self.statblock['INT'] * 5,
                        'Luck Roll' : self.statblock['POW'] * 5,
                        'Agility Roll' : self.statblock['DEX'] *5,
                        'Charisma Roll' : self.statblock['APP'] *5
                        }
                self.derived['Major Wound level'] = int(Decimal(self.derived['Hit Points']/2).quantize(0, ROUND_HALF_UP))
                if 'EDU' not in self.suppressed_stats:
                                self.derived['Know Roll'] = self.statblock['EDU'] * 5

        def finalise(self):
                """make sure no skills are above the Power level for the campaign. Re-allocate skills which are too high"""
                # go through the modified skills
                # any above (power level max) add to x
                # create dict with that skill and the minus
                # y = x
                # while y > 0
                # pick a random skill with a value of less than max -10
                # add 10 or y to it if y < 10
                # add the skill to the dict
                # add the dict to an Improvement
                # process the improvement
                final_dict = {}
                x = 0
                y = 0
                for skill, value in self.modified_skills.items():
                        if value > self.power_level['max']:
                                final_dict[skill] = self.power_level['max'] - value
                                x += (self.power_level['max'] - value)
                y = abs(x)
                # pick a number of skills and add 10 points to each
                while y > 0:
                        print(y)
                        addvalue = y if y < 10 else 10
                        addskill = self.randomSkill()
                        if self.modified_skills.get(addskill, 0) < (self.power_level['max'] - 10):
                                final_dict[addskill] = addvalue
                                y = y - addvalue
                                
                self.improve(Improvement(final_dict))

        
