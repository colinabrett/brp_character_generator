#
# BRP Professions
#

def skills_and_scores(skills,scores):
    skills_string = ''
    for s in skills:
        ss = str(scores[s])
        skills_string = skills_string + s + " " + ss + "% "
    return skills_string

def warrior_skillset():
    skill_list = ['Melee Weapon', 'Missile Weapon', 'Shield', 'Ride', 'Throw', 'Wrestle']
    base_skill_scores = {
        'Melee Weapon': 50,
        'Missile Weapon': 40,
        'Shield': 40,
        'Ride': 30,
        'Throw': 30,
        'Wrestle': 30
    }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def rogue_skillset():
    skill_list = [ 'Melee Weapon', 'Dagger', 'Hide', 'Move Quietly', 'Brawl']
    base_skill_scores = {
        'Melee Weapon': 30,
        'Dagger': 50,
        'Hide': 50,
        'Move Quietly': 50,
        'Brawl': 30
    }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def wizard_skillset():
    skill_list = [ 'Quarterstaff', 'Magic Spell 1', 'Magic Spell 2', 
                   'Spell Lore', 'Summon Elemental' ]
    base_skill_scores = {
        'Quarterstaff': 20,
        'Magic Spell 1': 50,
        'Magic Spell 2': 40,
        'Spell Lore': 30,
        'Summon Elemental': 30
    }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def priest_skillset():
    skill_list = [ 'Mace', 'Repel Undead', 'Shield', 'Theology', 
                   'Divine Spell']
    base_skill_scores = {
        'Mace': 30,
        'Repel Undead': 50,
        'Shield': 30,
        'Theology': 40,
        'Divine Spell': 50
    }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

