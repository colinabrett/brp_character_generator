# Improvement: a collection of skills which improve
# Examples: personality, cultural background, profession skills, other skills
# or general knowledge.
# At minimum, spits out a dictionary of skills and bonus:
# { 'Skill1' : bonus, Skill2 : bonus }
# Some Improvements do more than just spit out their contents.
# Profession might do more for example
#
# A GameSystem takes a list of these things.
from dice_roller import *
from random import shuffle

class Improvement():
    def __init__(self, skills_dict):
        self.skills = skills_dict
    
    def getSkills():
        return self.skills

class ProfessionImprovement(Improvement):
    def __init__(self, skills_dict):
        self.skills = skills_dict
        self.points = 0
        self.categorised_skills = {}

    def allocateSkillPoints(self, skill_points):
        """Allocate a number of points to be divided in some way between the skills"""
        self.points = int(math.floor(skill_points))

    def chooseSkills(self):
        """Decide how the skill points will be divided between the available skills"""
        # allocate (allocate skill points proportionally to profession skills)
        self.categoriseSkills()
        types = ['Primary', 'Secondary', 'Other']
        ratio = [0.4, 0.35, 0.25]
        types_ratio = dict(zip(types,ratio))
        for type in types:
            points = int(round((self.points * types_ratio[type])/len(self.categorised_skills[type]),0))
            skill_list = self.categorised_skills.get(type)
            for skill in skill_list:
                self.skills[skill] = points
            
    def categoriseSkills(self):
        """put available skills into categories primary, secondary, other"""
        self.categorised_skills = {'Primary' : [], 'Secondary' : [], 'Other' : []}
        skill_names = list(self.skills.keys())
        shuffle(skill_names)
        n_pri = straight_dice(1,3,0)
        n_sec = straight_dice(1,4,1)
        for i in range(0, (n_pri)):
            try:
                self.categorised_skills['Primary'].append(skill_names.pop())
            except IndexError:
                break
        for j in range(0, (n_sec)):
            try: 
                self.categorised_skills['Secondary'].append(skill_names.pop())
            except IndexError:
                break   
        while skill_names:
            self.categorised_skills['Other'].append(skill_names.pop())
        
        
    
