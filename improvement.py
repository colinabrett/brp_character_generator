# Improvement: a collection of skills which improve
# Examples: personality, cultural background, profession skills, other skills
# or general knowledge.
# At minimum, spits out a dictionary of skills and bonus:
# { 'Skill1' : bonus, Skill2 : bonus }
# Some Improvements do more than just spit out their contents.
# Profession might do more for example
#
# A GameSystem takes a list of these things.
# need another type which takes maybe a list of tuples of skills, points
# a la Magic World. Like ProfessionImprovement; maybe a subclass
from dice_roller import *
from random import shuffle
from collections import Iterable
def typecheck(obj):
    return not isinstance(obj, str) and isinstance(obj, Iterable)

class Improvement():
    def __init__(self, skills_dict):
        self.skills = skills_dict
    
    def getSkills(self):
        """return the skills dictionary"""
        return self.skills

class ProfessionImprovement(Improvement):
    """This one takes a number of skill points and allocates them in some way to the skills dictionary"""
    def __init__(self, skills_dict):
        self.skills = skills_dict
        self.points = 0
        self.categorised_skills = {}
        
    def getSkills(self):
        """return the skills dictionary"""
        return self.skills

    def allocateSkillPoints(self, skill_points):
        """Allocate a number of points to be divided in some way between the skills"""
        self.points = int(math.floor(skill_points))
        self.chooseSkills()

    def chooseSkills(self):
        """Decide how the skill points will be divided between the available skills"""
        self.categoriseSkills()
        types = ['Primary', 'Secondary', 'Other']
        ratio = [0.4, 0.35, 0.25]
        types_ratio = dict(zip(types,ratio))
        # if categories empty, re-allocate ratio
        reallocate = 0
        for key, skills in self.categorised_skills.items():
            if len(skills) == 0:
                reallocate += types_ratio[key]
                types_ratio.pop(key, None)
        if reallocate > 0:
            newratio = reallocate / len(types_ratio)
            for key, value in types_ratio.items():
                value += newratio
        # allocate (allocate skill points proportionally to profession skills)
        for type in types:
            if len(self.categorised_skills[type]) > 0:
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
            
class ProfesssionImprovementMW(Improvement):
    """As ProfessionImprovement, except that the allocation method is by tuples of (number of skills, points to allocate), rather than a ratio and a pool of points."""
    def __init__(self, skills_dict):
        self.skills = skills_dict
        self.points = 0
        self.categorised_skills = {}
    def getSkills(self):
        """return the skills dictionary"""
        return self.skills
    
    def allocateSkillPoints(self, skill_points):
        """Allocate a number of points to be divided in some way between the skills. Here, skill_points is a list of tuples of (number of skills, point to add). For example: [(1,60), (2,40)] indicates one skill to be allocated 60 points and 2 to be allocated 40 points"""
        if typecheck(skill_points):
            self.points = skill_points
        # zero all skills values before allocation
        for skill in self.skills:
            self.skills[skill] = 0
        self.chooseSkills()

    def chooseSkills(self):
        """Decide how the skill points will be divided between the available skills"""
        self.categoriseSkills()
        # Add the points from the categories to the skills_dict
        for category in self.categorised_skills.keys():
            points = category[1]
            skill_list = self.categorised_skills.get(category)
            for skill in skill_list:
                self.skills[skill] = points

    def categoriseSkills(self):
        """Put available skills into number of categories equal to length of points tuple list."""
        # Allocate points based on the points tuples;
        # the tuples become the category names.
        # eg for (1,60):
        # 1. pick 1 random skill from self.skills
        # 2. add 60 points to it
        skill_names = list(self.skills.keys())
        shuffle(skill_names)
        for category in self.points:
            self.categorised_skills[category] = []
            
        for category in self.categorised_skills.keys():
            for x in range(0, category[0]):
                self.categorised_skills[category].append(skill_names.pop())
        
            
