#
# BRP Professions Fantasy
#

def skills_and_scores(skills,scores):
    skills_string = ''
    for s in skills:
        ss = str(scores[s])
        skills_string = skills_string + s + " " + ss + "% "
    return skills_string

def fantasy_warrior_skillset():
    skill_list = [
        'First Melee Weapon', 
        'Second Melee Weapon', 
        'Missile Weapon', 
        'Brawl', 
        'Throw',
        'Grapple', 
        'Parry', 
        'Shield', 
        'Stealth', 
        'Ride' ]
    base_skill_scores = {
        'First Melee Weapon': 50,
        'Second Melee Weapon': 40,
        'Missile Weapon': 40,
        'Brawl': 30,
        'Throw': 30,
        'Grapple': 30,
        'Parry': 30,
        'Shield': 30,
        'Stealth': 30,
        'Ride': 30 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def fantasy_rogue_skillset():
    skill_list = [ 
        'Stealth', 
        'Hide', 
        'Fine Manipulation', 
        'Dodge', 
        'Fast Talk', 
        'Appraise',
        'Listen', 
        'Spot', 
        'Brawl', 
        'Melee Weapon' ]
    base_skill_scores = {
        'Stealth': 30,
        'Hide': 50,
        'Fine Manipulation': 50,
        'Dodge': 50,
        'Fast Talk': 50,
        'Appraise': 50,
        'Listen': 50,
        'Spot': 50,
        'Brawl': 50,
        'Melee Weapon': 30 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def fantasy_wizard_skillset():
    skill_list = [ 
        'Knowledge (Occult)', 
        'Perform (Rituals)', 
        'Language (Other)', 
        'Craft (Any)', 
        'Knowledge 1',
        'Knowledge 2', 
        'Insight', 
        'Persuade', 
        'Research', 
        'Literacy' ]
    base_skill_scores = {
        'Knowledge (Occult)': 20,
        'Perform (Rituals)': 50,
        'Language (Other)': 40,
        'Craft (Any)': 30,
        'Knowledge 1': 30,
        'Knowledge 2': 30,
        'Insight': 30,
        'Persuade': 30,
        'Research': 30,
        'Literacy': 30 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def fantasy_priest_skillset():
    skill_list = [ 
        'Knowledge (Religion)', 
        'Perform (Rituals)', 
        'Perform (Oratory)', 
        'Insight',
        'Research', 
        'Knowledge (History)', 
        'Persuade', 
        'Teach', 
        'Fast Talk', 
        'Literacy' ]
    base_skill_scores = {
        'Knowledge (Religion)': 30,
        'Perform (Rituals)': 50,
        'Perform (Oratory)': 30,
        'Insight': 40,
        'Research': 40,
        'Knowledge (History)': 40,
        'Persuade': 40,
        'Teach': 40,
        'Fast Talk': 40,
        'Literacy': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def fantasy_explorer_skillset():
    skill_list = [ 
        'Track',  
        'Hide',  
        'Spot',  
        'Listen',  
        'Climb',
        'Navigate', 
        'Stealth',  
        'Missile Weapon',  
        'Melee Weapon',  
        'Knowledge (Region)' ]
    base_skill_scores = {
        'Track': 30,
        'Hide': 50,
        'Spot': 30,
        'Listen': 40,
        'Climb': 40,
        'Navigate': 40,
        'Stealth': 40,
        'Missile Weapon': 40,
        'Melee Weapon': 40,
        'Knowledge (Region)': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def fantasy_noble_skillset():
    skill_list = [ 
        'Status',  
        'Etiquette',  
        'Knowledge (Region)',  
        'Literacy',  
        'Melee Weapon', 
        'Language (Other)',  
        'Bargain',  
        'Ride',  
        'Insight',  
        'Craft (Any)' ]
    base_skill_scores = {
        'Status': 30,
        'Etiquette': 50,
        'Knowledge (Region)': 30,
        'Literacy': 40,
        'Melee Weapon': 40,
        'Language (Other)': 40,
        'Bargain': 40,
        'Ride': 40,
        'Insight': 40,
        'Craft (Any)': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def fantasy_assassin_skillset():
    skill_list = [ 
        'Stealth',  
        'Hide',  
        'Dodge',  
        'Listen',  
        'Spot',
        'Missile Weapon',  
        'Melee Weapon',  
        'Disguise',  
        'Knowledge (Poisons)',  
        'Track' ]
    base_skill_scores = {
        'Stealth': 30,
        'Hide': 50,
        'Dodge': 30,
        'Listen': 40,
        'Spot': 40,
        'Missile Weapon': 40,
        'Melee Weapon': 40,
        'Disguise': 40,
        'Knowledge (Poisons)': 40,
        'Track': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def fantasy_beggar_skillset():
    skill_list = [ 
        'Bargain',  
        'Fast Talk',  
        'Hide',  
        'Insight',  
        'Knowledge (Local Area)',
        'Listen',  
        'Persuade',  
        'Sleight of Hand',  
        'Spot',  
        'Stealth' ]
    base_skill_scores = {
        'Bargain': 30,
        'Fast Talk': 50,
        'Hide': 30,
        'Insight': 40,
        'Knowledge (Local Area)': 40,
        'Listen': 40,
        'Persuade': 40,
        'Sleight of Hand': 40,
        'Spot': 40,
        'Stealth': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def fantasy_artisan_skillset():
    skill_list = [ 
        'Craft Skill 1',  
        'Craft Skill 2',  
        'Repair (Mechanical)',  
        'Appraise',  
        'Art (Any)',
        'Bargain',  
        'Spot',  
        'Research',  
        'Status',  
        'Fine Manipulation' ]
    base_skill_scores = {
        'Craft Skill 1': 30,
        'Craft Skill 2': 50,
        'Repair (Mechanical)': 30,
        'Appraise': 40,
        'Art (Any)': 40,
        'Bargain': 40,
        'Spot': 40,
        'Research': 40,
        'Status': 40,
        'Fine Manipulation': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def fantasy_merchant_skillset():
    skill_list = [ 
        'Bargain',  
        'Appraise',  
        'Fast Talk',  
        'Knowledge (Accounting)',  
        'Knowledge (Business)',
        'Persuade',  
        'Research',  
        'Status',  
        'Insight',  
        'Literacy' ]
    base_skill_scores = {
        'Bargain': 30,
        'Appraise': 50,
        'Fast Talk': 30,
        'Knowledge (Accounting)': 40,
        'Knowledge (Business)': 40,
        'Persuade': 40,
        'Research': 40,
        'Status': 40,
        'Insight': 40,
        'Literacy': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def fantasy_shaman_skillset():
    skill_list = [ 
        'Perform (Rituals)',  
        'Knowledge (Occult)',  
        'First Aid',  
        'Art (Any)',  
        'Knowledge (Folklore)',
        'Insight',  
        'Language (Own)',  
        'Listen',  
        'Craft (Any)',  
        'Science (Natural History)' ]
    base_skill_scores = {
        'Perform (Rituals)': 30,
        'Knowledge (Occult)': 50,
        'First Aid': 30,
        'Art (Any)': 40,
        'Knowledge (Folklore)': 40,
        'Insight': 40,
        'Language (Own)': 40,
        'Listen': 40,
        'Craft (Any)': 40,
        'Science (Natural History)': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def fantasy_hunter_skillset():
    skill_list = [ 
        'Track',  
        'Hide',  
        'Spot',  
        'Listen',  
        'Climb',  
        'Navigate',  
        'Stealth',
        'Missile Weapon',  
        'Melee Weapon',  
        'Knowledge (Region)' ]
    base_skill_scores = {
        'Track': 30,
        'Hide': 50,
        'Spot': 30,
        'Listen': 40,
        'Climb': 40,
        'Navigate': 40,
        'Stealth': 40,
        'Missile Weapon': 40,
        'Melee Weapon': 40,
        'Knowledge (Region)': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

