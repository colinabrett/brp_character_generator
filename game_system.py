#
# game system classes
# defines the basics of the character sheet
#
from dice_roller import *
from brp_stats import *
from decimal import Decimal, ROUND_HALF_UP
from improvement import *
from brp_skills import *
from improvement import *
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

        def improve(self, improvement, skill_points=0):
                """Apply the skills of an Improvement to the modified skills attribute"""
                # allocate the skill points first if it's a ProfessionImprovement
                if skill_points == 0:
                        skill_points = self.skill_points
                if hasattr(improvement, "allocateSkillPoints") and callable(getattr(improvement, "allocateSkillPoints")):
                        improvement.allocateSkillPoints(skill_points)
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

        def randomSkill(self, except_skills = None):
                """pick a random skill from those available. 'except_skills' is a list of skill names to be ignored, like self.supressed_skills but on a per-call basis"""
                skill_list = set(self.skills.keys()) - set(self.suppressed_skills)
                if except_skills:
                        skill_list -= set(except_skills)
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
                self.skill_points = 0
                self.suppressed_stats = []
                self.bonuses = {}
                self.improvements = []
                self.skills = {}
                self.modified_skills = {}
                self.suppressed_skills = []

        def calculateStats(self, statslist):
                """ assign stats as parent, then recalculate other things """
                super(Brp, self).calculateStats(statslist)
                self.calculateBaseSkills()
                self.calculateSkillPoints()
                self.calculateBonuses()
                self.calculateDerived()

        def calculateBaseSkills(self):
                """Not all of these require calculation. This should be performed after calculateStats"""
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

        def calculateImprovements(self, profession_skill_dict):
                """BRP has a profession and other skills"""
                # profession is a ProfessionImprovement
                # other skills an ProfessionImprovement with points divided between 1d4+1 random skills
                # process each Improvement then
                # finish with finalise, to even out skills
                other_points = self.statblock['INT'] * 10
                other_skills = {}
                n = straight_dice(1,4,1)
                for x in range(1, n):
                        other_skills[self.randomSkill()] = 0
                self.calculateSkillPoints()
                improvement_list = [(ProfessionImprovement(profession_skill_dict), self.skill_points), (ProfessionImprovement(other_skills), other_points)]
                for i in improvement_list:
                        self.improve(i[0], i[1]) 
                self.finalise()

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
                        addvalue = y if y < 10 else 10
                        addskill = self.randomSkill()
                        if self.modified_skills.get(addskill, 0) < (self.power_level['max'] - 10):
                                final_dict[addskill] = addvalue
                                y = y - addvalue
                                
                self.improve(Improvement(final_dict))

        
class MagicWorld(GameSystem):
        def __init__(self, power_level='Normal'):
                """constructor for Magic World character"""
                # power levels 'POW' is the amount added to POW;
                # 'stats' are points added to non-POW stats (probably also not SIZ)
                power_levels = {
                        'Normal' : {'profession' : [(1,60), (3,40), (4,20)], 'other' : [(1,40), (3,20)], 'POW' :0, 'stats' : 0, 'spells' : 3},
                        'Veteran' : {'profession' : [(2,60), (3,40), (3,20)], 'other' : [(3,40), (6,20)], 'POW' : 1, 'stats': 1, 'spells' : 6},
                        'Heroic' : {'profession' : [(1,80), (2,60), (2,40), (3,20)], 'other' : [(4,40), (6,20)], 'POW' : 2, 'stats' : 2, 'spells' : 9},
                        'Legendary' : {'profession' : [(2,80), (3,60), (3,40)], 'other' : [(5,40), (8,20)], 'POW' : 3, 'stats' : 4, 'spells' : 12}
                }
                self.power_level = power_levels.get(power_level, 'Normal')
                self.statblock = {
                        'STR' : 0,
                        'CON' : 0,
                        'POW' : 0,
                        'DEX' : 0,
                        'APP' : 0,
                        'INT' : 0,
                        'SIZ' : 0
                }
                self.skills = {}
                self.skill_points = 0
                self.suppressed_stats = []
                self.bonuses = {}
                self.improvements = []
                self.modified_skills = {}
                self.suppressed_skills = []
                
        def calculateStats(self, statslist):
                """ assign stats as parent, then recalculate other things """
                super(MagicWorld, self).calculateStats(statslist)
                # adjust stats for power level
                self.statblock['POW'] += self.power_level['POW']
                nonpow = ['STR', 'CON', 'DEX', 'APP', 'INT', 'SIZ']
                for x in range(0, self.power_level['stats']):
                        self.statblock[random.choice(nonpow)] += 1
                self.calculateBaseSkills()
                self.calculateBonuses()
                self.calculateDerived()

        def calculateBaseSkills(self):
                """not all of these require calculation, but it should be run after calculateStats"""
                # note these are lifted straight from mw_skills.py
                self.skills = {
                        'Art' : 5,
                        'Bargain' :  15,
                        'Brawl' : 20,
                        'Climb' : 40,
                        'Conceal Object'  : 25,
                        'Craft'  : 5,
                        'Disguise' : 15,
                        'Dodge' : self.statblock["DEX"] * 2,
                        'Evaluate' : 15,
                        'Fast Talk' : 5,
                        'Hide' : 20,
                        'Insight' : 15,
                        'Jump' : 5,
                        'Listen' : 25,
                        'Lore' : 15,
                        'Lore Rare' : 0,
                        'Move Quietly' : 20,
                        'Nature' : 25,
                        'Navigate' : 10,
                        'Oratory'  : 5,
                        'Other Language'  : 0,
                        'Own Language'  : self.statblock["INT"] * 5,
                        'Physik'  : 30,
                        'Pick Lock'  : 5,
                        'Potions' : 0,
                        'Repair/Devise' : self.statblock["DEX"] * 4,
                        'Ride' :  35,
                        'Sailing' : 15,
                        'Scribe' : 0,
                        'Search' : 20,
                        'Sense' : 15,
                        'Swim' : 25,
                        'Throw' : 25,
                        'Track' : 10,
                        'Trap' : 5,
                        'Weapon Skill' :  0,
                        'World Lore' : 15,
                        'Wrestle' : 25
                }  
                

        def calculateBonuses(self):
                """Calculate skill modifiers, based on attributes (like scm function)"""
                self.bonuses = {
                        'Physical' : int(Decimal(self.statblock['STR'] / 2).quantize(0, ROUND_HALF_UP)),
                        'Communication' : int(Decimal(self.statblock['APP'] / 2).quantize(0, ROUND_HALF_UP)),
                        'Knowledge' : int(Decimal(self.statblock['INT'] / 2).quantize(0, ROUND_HALF_UP)),
                        'Manipulation' : int(Decimal(self.statblock['DEX'] / 2).quantize(0, ROUND_HALF_UP)),
                        'Perception' : int(Decimal(self.statblock['CON'] / 2).quantize(0, ROUND_HALF_UP))
                }

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

        def calculateImprovements(self, profession_skill_dict):
                """MagicWorld has a minimum of profession and other skills"""
                # profession is a ProfessionImprovementMW
                # other skills an ProfessionImprovementMW
                # process each Improvement
                # Other skills are explicitly not professional skills
                other_skills = {}
                professional_skills = profession_skill_dict.keys()
                # find number of skills from tuple
                n = 0
                for points in self.power_level['other']:
                        n += points[0]
                # pick n skills from the set of skills which are *not* professional
                while len(other_skills) < n:
                        other_skills[self.randomSkill(professional_skills)] = 0
                print("Other skills: ", len(other_skills))
                print("Should be ", n)
                improvement_list = [
                        (ProfessionImprovementMW(profession_skill_dict), self.power_level['profession']),
                        (ProfessionImprovementMW(other_skills), self.power_level['other'])
                ]
                for i in improvement_list:
                        self.improve(i[0], i[1])

