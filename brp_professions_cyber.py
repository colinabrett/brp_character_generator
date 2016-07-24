#
# BRP Professions Cyberpunk
#

def skills_and_scores(skills,scores):
    skills_string = ''
    for s in skills:
        ss = str(scores[s])
        skills_string = skills_string + s + " " + ss + "% "
    return skills_string

def solo_skillset():
    skill_list = ['Pistol Weapon', 'Melee Weapon', 'SMG', 'Throw', 'Brawl']
    base_skill_scores = {
        'Pistol Weapon': 50,
        'Melee Weapon': 40,
        'SMG': 40,
        'Throw': 30,
        'Brawl': 30
    }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def fixer_skillset():
    skill_list = [ 'Pistol Weapon', 'Streetwise', 'Hide', 'Move Quietly', 'Brawl']
    base_skill_scores = {
        'Pistol Weapon': 30,
        'Streetwise': 50,
        'Hide': 50,
        'Move Quietly': 50,
        'Brawl': 30
    }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def rocker_skillset():
    skill_list = [ 'Play Instrument', 'Sing', 'Musical Composition', 
                   'Pistol Weapon', 'Media Relations' ]
    base_skill_scores = {
        'Play Instrument': 20,
        'Sing': 50,
        'Musical Composition': 40,
        'Pistol Weapon': 30,
        'Media Relations': 30
    }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def techie_skillset():
    skill_list = [ 'Repair', 'Electronics', 'Mechanics', 'Computers', 
                   'Science']
    base_skill_scores = {
        'Repair': 30,
        'Electronics': 50,
        'Mechanics': 30,
        'Computers': 40,
        'Science': 50
    }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

