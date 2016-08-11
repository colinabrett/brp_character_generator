#
# BRP Professions Horror
#

def skills_and_scores(skills,scores):
    skills_string = ''
    for s in skills:
        ss = str(scores[s])
        skills_string = skills_string + s + " " + ss + "% "
    return skills_string

def wildwest_soldier_skillset(raw=False):
    skill_list = [ 
        'Firearms (Rifle)', 
        'Brawl', 
        'Dodge', 
        'Spot', 
        'Navigate',
        'First Aid', 
        'Hide', 
        'Repair (Mechanical)', 
        'Heavy Weapon', 
        'Demolition' ]
    base_skill_scores = {
        'Firearms (Rifle)': 30,
        'Brawl': 50,
        'Dodge': 30,
        'Spot': 40,
        'Navigate': 40,
        'First Aid': 40,
        'Hide': 40,
        'Repair (Mechanical)': 40,
        'Heavy Weapon': 40,
        'Demolition': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    if not raw:
        return skill_set
    else:
        return base_skill_scores

def wildwest_occultist_skillset(raw=False):
    skill_list = [ 
        'Knowledge (Occult)', 
        'Perform (Rituals)', 
        'Fast Talk', 
        'Insight', 
        'Language (Other)',
        'Knowledge (Folklore)', 
        'Research', 
        'Art (Any)', 
        'Craft (Any)', 
        'Knowledge (Blasphemous)' ]
    base_skill_scores = {
        'Knowledge (Occult)': 30,
        'Perform (Rituals)': 50,
        'Fast Talk': 30,
        'Insight': 40,
        'Language (Other)': 40,
        'Knowledge (Folklore)': 40,
        'Research': 40,
        'Art (Any)': 40,
        'Craft (Any)': 40,
        'Knowledge (Blasphemous)': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    if not raw:
        return skill_set
    else:
        return base_skill_scores

def wildwest_preacher_skillset(raw=False):
    skill_list = [ 
        'Knowledge (Religion)', 
        'Perform (Rituals)', 
        'Insight', 
        'Fast Talk', 
        'Knowledge (History)',
        'Persuade', 
        'Perform (Oratory)', 
        'Teach', 
        'Research', 
        'Knowledge (Philosophy)' ]
    base_skill_scores = {
        'Knowledge (Religion)': 30,
        'Perform (Rituals)': 50,
        'Insight': 30,
        'Fast Talk': 40,
        'Knowledge (History)': 40,
        'Persuade': 40,
        'Perform (Oratory)': 40,
        'Teach': 40,
        'Research': 40,
        'Knowledge (Philosophy)': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    if not raw:
        return skill_set
    else:
        return base_skill_scores

def wildwest_criminal_skillset(raw=False):
    skill_list = [ 
        'Bargain', 
        'Brawl', 
        'Melee Weapon', 
        'Appraise', 
        'Hide',
        'Stealth', 
        'Ride', 
        'Persuade', 
        'Spot', 
        'Fine Manipulation' ]
    base_skill_scores = {
        'Bargain': 30,
        'Brawl': 50,
        'Melee Weapon': 30,
        'Appraise': 40,
        'Hide': 40,
        'Stealth': 40,
        'Ride': 40,
        'Persuade': 40,
        'Spot': 40,
        'Fine Manipulation': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    if not raw:
        return skill_set
    else:
        return base_skill_scores

def wildwest_madscientist_skillset(raw=False):
    skill_list = [ 
        'Science 1', 
        'Science 2', 
        'Technical Skill 1', 
        'Fine Manipulation', 
        'Persuade', 
        'Research', 
        'Technical Skill 2', 
        'Technical Skill 3', 
        'Science 3', 
        'Status' ]
    base_skill_scores = {
        'Science 1': 30,
        'Science 2': 50,
        'Technical Skill 1': 30,
        'Fine Manipulation': 40,
        'Persuade': 40,
        'Research': 40,
        'Technical Skill 2': 40,
        'Technical Skill 3': 40,
        'Science 3': 40,
        'Status': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    if not raw:
        return skill_set
    else:
        return base_skill_scores

def wildwest_gambler_skillset(raw=False):
    skill_list = [ 
        'Gaming', 
        'Fast Talk', 
        'Sleight of Hand', 
        'Bargain', 
        'Brawl',
        'Spot', 
        'Insight', 
        'Persuade', 
        'Knowledge (Accounting)', 
        'Dodge' ]
    base_skill_scores = {
        'Gaming': 30,
        'Fast Talk': 50,
        'Sleight of Hand': 30,
        'Bargain': 40,
        'Brawl': 40,
        'Spot': 40,
        'Insight': 40,
        'Persuade': 40,
        'Knowledge (Accounting)': 40,
        'Dodge': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    if not raw:
        return skill_set
    else:
        return base_skill_scores

def wildwest_sheriff_skillset(raw=False):
    skill_list = [ 
        'Firearms (Pistol)', 
        'Knowledge (Law)', 
        'Listen', 
        'Persuade', 
        'Spot', 
        'Brawl', 
        'Ride', 
        'Insight', 
        'Research', 
        'Etiquette (Street)' ]
    base_skill_scores = {
        'Firearms (Pistol)': 30,
        'Knowledge (Law)': 50,
        'Listen': 30,
        'Persuade': 40,
        'Spot': 40,
        'Brawl': 40,
        'Ride': 40,
        'Insight': 40,
        'Research': 40,
        'Etiquette (Street)': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    if not raw:
        return skill_set
    else:
        return base_skill_scores

def wildwest_doctor_skillset(raw=False):
    skill_list = [ 
        'First Aid', 
        'Medicine', 
        'Persuade', 
        'Research', 
        'Spot', 
        'Science (Pharmacy)', 
        'Science (Psychology)', 
        'Psychotherapy', 
        'Status', 
        'Language (Other)' ]
    base_skill_scores = {
        'First Aid': 30,
        'Medicine': 50,
        'Persuade': 30,
        'Research': 40,
        'Spot': 40,
        'Science (Pharmacy)': 40,
        'Science (Psychology)': 40,
        'Psychotherapy': 40,
        'Status': 40,
        'Language (Other)': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    if not raw:
        return skill_set
    else:
        return base_skill_scores

def wildwest_tribesman_skillset(raw=False):
    skill_list = [ 
        'Craft (Any)', 
        'Dodge', 
        'Grapple', 
        'Hide', 
        'Knowledge (Natural History)', 
        'Spot', 
        'Throw', 
        'Track', 
        'Melee Weapon', 
        'Missile Weapon' ]
    base_skill_scores = {
        'Craft (Any)': 30,
        'Dodge': 50,
        'Grapple': 30,
        'Hide': 40,
        'Knowledge (Natural History)': 40,
        'Spot': 40,
        'Throw': 40,
        'Track': 40,
        'Melee Weapon': 40,
        'Missile Weapon': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    if not raw:
        return skill_set
    else:
        return base_skill_scores

def wildwest_frontiersman_skillset(raw=False):
    skill_list = [ 
        'Track',  
        'Hide',  
        'Spot',  
        'Listen',  
        'Climb',  
        'Navigate',  
        'Stealth',
        'Firearms (Rifle)',  
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
        'Firearms (Rifle)': 40,
        'Melee Weapon': 40,
        'Knowledge (Region)': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    if not raw:
        return skill_set
    else:
        return base_skill_scores
