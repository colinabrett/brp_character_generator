
#
# BRP Professions Horror
#

def skills_and_scores(skills,scores):
    skills_string = ''
    for s in skills:
        ss = str(scores[s])
        skills_string = skills_string + s + " " + ss + "% "
    return skills_string

def horror_mercenary_skillset(raw=False):
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

def horror_occultist_skillset(raw=False):
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

def horror_priest_skillset(raw=False):
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

def horror_criminal_skillset(raw=False):
    skill_list = [ 
        'Bargain', 
        'Brawl', 
        'Melee Weapon', 
        'Appraise', 
        'Hide',
        'Stealth', 
        'Drive (Car)', 
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
        'Drive (Car)': 40,
        'Persuade': 40,
        'Spot': 40,
        'Fine Manipulation': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    if not raw:
        return skill_set
    else:
        return base_skill_scores

def horror_journalist_skillset(raw=False):
    skill_list = [ 
        'Persuade', 
        'Research', 
        'Fast Talk', 
        'Insight', 
        'Listen', 
        'Spot',
        'Knowledge (Any)', 
        'Technical Skill (Photo and Film)', 
        'Disguise', 
        'Language (Other)' ]
    base_skill_scores = {
        'Persuade': 30,
        'Research': 50,
        'Fast Talk': 30,
        'Insight': 40,
        'Listen': 40,
        'Spot': 40,
        'Knowledge (Any)': 40,
        'Technical Skill (Photo and Film)': 40,
        'Disguise': 40,
        'Language (Other)': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    if not raw:
        return skill_set
    else:
        return base_skill_scores

def horror_spy_skillset(raw=False):
    skill_list = [ 
        'Knowledge (Espionage)', 
        'Research', 
        'Firearms (Pistol)', 
        'Listen', 
        'Hide', 
        'Spot', 
        'Stealth', 
        'Brawl', 
        'Disguise', 
        'Technical Skill (Electronic Security)' ]
    base_skill_scores = {
        'Knowledge (Espionage)': 30,
        'Research': 50,
        'Firearms (Pistol)': 30,
        'Listen': 40,
        'Hide': 40,
        'Spot': 40,
        'Stealth': 40,
        'Brawl': 40,
        'Disguise': 40,
        'Technical Skill (Electronic Security)': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    if not raw:
        return skill_set
    else:
        return base_skill_scores

def horror_scientist_skillset(raw=False):
    skill_list = [ 'Science 1', 'Science 2', 'Technical Skill 1', 'Fine Manipulation', 'Persuade', 
                   'Research', 'Technical Skill (Computer Use)', 'Technical Skill 2', 'Science 3', 'Status']
    base_skill_scores = {
        'Science 1': 30,
        'Science 2': 50,
        'Technical Skill (Any)': 30,
        'Fine Manipulation': 40,
        'Persuade': 40,
        'Research': 40,
        'Technical Skill (Computer Use)': 40,
        'Technical Skill 2': 40,
        'Science 3': 40,
        'Status': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    if not raw:
        return skill_set
    else:
        return base_skill_scores

def horror_gambler_skillset(raw=False):
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

def horror_detective_skillset(raw=False):
    skill_list = [ 
        'Firearms (Pistol)', 
        'Knowledge (Law)', 
        'Listen', 
        'Persuade', 
        'Spot', 
        'Brawl', 
        'Drive (Car)', 
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
        'Drive (Car)': 40,
        'Insight': 40,
        'Research': 40,
        'Etiquette (Street)': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    if not raw:
        return skill_set
    else:
        return base_skill_scores

def horror_doctor_skillset(raw=False):
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
