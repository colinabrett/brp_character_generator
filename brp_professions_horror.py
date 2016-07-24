#
# BRP Professions Horror
#

def skills_and_scores(skills,scores):
    skills_string = ''
    for s in skills:
        ss = str(scores[s])
        skills_string = skills_string + s + " " + ss + "% "
    return skills_string

def doctor_skillset():
    skill_list = ['Medicine', 'First Aid', 'Science', 'Psychotherapy', 'Bargain']
    base_skill_scores = {
        'Medicine': 50,
        'First Aid': 40,
        'Science': 40,
        'Psychotherapy': 30,
        'Bargain': 30
    }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def detective_skillset():
    skill_list = [ 'Pistol Weapon', 'Baton', 'Law', 'Move Quietly', 'Brawl']
    base_skill_scores = {
        'Pistol Weapon': 30,
        'Baton': 50,
        'Law': 50,
        'Move Quietly': 50,
        'Brawl': 30
    }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def sorcerer_skillset():
    skill_list = [ 'Quarterstaff', 'Psionic Power 1', 'Psionic Power 2', 
                   'Forbidden Lore', 'Summon Entity' ]
    base_skill_scores = {
        'Quarterstaff': 20,
        'Psionic Power 1': 50,
        'Psionic Power 2': 40,
        'Forbidden Lore': 30,
        'Summon Entity': 30
    }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def adventurer_skillset():
    skill_list = [ 'Track', 'Pistol', 'Brawl', 'Climb', 
                   'Drive']
    base_skill_scores = {
        'Track': 30,
        'Pistol': 50,
        'Brawl': 30,
        'Climb': 40,
        'Drive': 50
    }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

