#
# BRP Professions SciFi
#

def skills_and_scores(skills,scores):
    skills_string = ''
    for s in skills:
        ss = str(scores[s])
        skills_string = skills_string + s + " " + ss + "% "
    return skills_string

def soldier_skillset():
    skill_list = ['Energy Weapon', 'Melee Weapon', 'Tactics', 'Throw', 'Brawl']
    base_skill_scores = {
        'Energy Weapon': 50,
        'Melee Weapon': 40,
        'Tactics': 40,
        'Throw': 30,
        'Brawl': 30
    }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def smuggler_skillset():
    skill_list = [ 'Pistol Weapon', 'Dagger', 'Hide', 'Move Quietly', 'Brawl']
    base_skill_scores = {
        'Pistol Weapon': 30,
        'Dagger': 50,
        'Hide': 50,
        'Move Quietly': 50,
        'Brawl': 30
    }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def psyker_skillset():
    skill_list = [ 'Quarterstaff', 'Psionic Power 1', 'Psionic Power 2', 
                   'Psyker Lore', 'Summon Warp Entity' ]
    base_skill_scores = {
        'Quarterstaff': 20,
        'Psionic Power 1': 50,
        'Psionic Power 2': 40,
        'Psyker Lore': 30,
        'Summon Warp Entity': 30
    }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def marine_skillset():
    skill_list = [ 'Boltgun', 'Bolt Pistol', 'Brawl', 'Heavy Weapon', 
                   'Drive Rhino']
    base_skill_scores = {
        'Boltgun': 30,
        'Bolt Pistol': 50,
        'Brawl': 30,
        'Heavy Weapon': 40,
        'Drive Rhino': 50
    }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

