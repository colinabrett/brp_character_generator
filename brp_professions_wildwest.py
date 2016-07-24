#
# BRP Professions Wild West
#

def skills_and_scores(skills,scores):
    skills_string = ''
    for s in skills:
        ss = str(scores[s])
        skills_string = skills_string + s + " " + ss + "% "
    return skills_string

def cavalry_skillset():
    skill_list = ['Rifle', 'Bowie Knife', 'Ride', 'Throw', 'Brawl']
    base_skill_scores = {
        'Rifle': 50,
        'Bowie Knife': 40,
        'Ride': 40,
        'Throw': 30,
        'Brawl': 30
    }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def gambler_skillset():
    skill_list = [ 'Gamble', 'Dagger', 'Sleight', 'Derringer Pistol', 'Brawl']
    base_skill_scores = {
        'Gamble': 30,
        'Dagger': 50,
        'Sleight': 50,
        'Derringer Pistol': 50,
        'Brawl': 30
    }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def madscientist_skillset():
    skill_list = [ 'Sword', 'Repair', 'Mechanics', 
                   'Electrical', 'Medicine' ]
    base_skill_scores = {
        'Sword': 20,
        'Repair' : 50,
        'Mechanics': 40,
        'Electrical': 30,
        'Medicine': 30
    }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def brave_skillset():
    skill_list = [ 'Track', 'Bow', 'Brawl', 'Hide', 
                   'Ride']
    base_skill_scores = {
        'Track': 30,
        'Bow': 50,
        'Brawl': 30,
        'Hide': 40,
        'Ride': 50
    }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

