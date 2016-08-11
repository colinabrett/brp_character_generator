#
# BRP Professions Cyberpunk
#

def skills_and_scores(skills,scores):
    skills_string = ''
    for s in skills:
        ss = str(scores[s])
        skills_string = skills_string + s + " " + ss + "% "
    return skills_string

def cyber_solo_skillset(raw=False):
    skill_list = [
        'Firearms (Pistol)', 
        'Firearms (SMG)', 
        'Firearms (Rifle)', 
        'Spot', 
        'Martial Arts', 
        'Melee Weapon', 
        'Brawl', 
        'Stealth',
        'Listen', 
        'Technical Skill (WeaponsTech)' ]
    base_skill_scores = {
        'Firearms (Pistol)': 50,
        'Firearms (SMG)': 40,
        'Firearms (Rifle)': 40,
        'Spot': 30,
        'Martial Arts': 30,
        'Melee Weapon': 30,
        'Brawl': 30,
        'Stealth': 30,
        'Listen': 30,
        'Technical Skill (WeaponsTech)': 30 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    if not raw:
        return skill_set
    else:
        return base_skill_scores

def cyber_fixer_skillset(raw=False):
    skill_list = [ 
        'Etiquette (Street)', 
        'Bargain', 
        'Persuade', 
        'Spot', 
        'Stealth', 
        'Technical Skill (Forgery)', 
        'Sleight of Hand', 
        'Brawl', 
        'Fine Manipulation', 
        'Firearms (Pistol)' ]
    base_skill_scores = {
        'Etiquette (Street)': 30,
        'Bargain': 50,
        'Persuade': 50,
        'Spot': 50,
        'Stealth': 50,
        'Technical Skill (Forgery)': 50,
        'Sleight of Hand': 50,
        'Brawl': 50,
        'Fine Manipulation': 50,
        'Firearms (Pistol)': 30 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    if not raw:
        return skill_set
    else:
        return base_skill_scores

def cyber_rocker_skillset(raw=False):
    skill_list = [ 
        'Perform (Play Instrument)', 
        'Perform (Sing)', 
        'Art (Musical Composition)', 
        'Etiquette (Street)', 
        'Brawl', 
        'Fast Talk', 
        'Spot', 
        'Status', 
        'Disguise', 
        'Persuade' ]
    base_skill_scores = {
        'Perform (Play Instrument)': 20,
        'Perform (Sing)': 50,
        'Art (Musical Composition)': 40,
        'Etiquette (Street)': 30,
        'Brawl': 30,
        'Fast Talk': 30,
        'Spot': 30,
        'Status': 30,
        'Disguise': 30,
        'Persuade': 30 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    if not raw:
        return skill_set
    else:
        return base_skill_scores

def cyber_techie_skillset(raw=False):
    skill_list = [ 
        'Repair (Electrical)', 
        'Repair (Mechanical)', 
        'Technical Skill (Electronics)', 
        'Technical Skill (Cybernetics)', 
        'Science (Physics)', 
        'Science (Chemistry)', 
        'Teach', 
        'Fine Manipulation', 
        'Research', 
        'Heavy Machinery' ]
    base_skill_scores = {
        'Repair (Electrical)': 30,
        'Repair (Mechanical)': 50,
        'Technical Skill (Electronics)': 30,
        'Technical Skill (Cybernetics)': 40,
        'Science (Physics)': 40,
        'Science (Chemistry)': 40,
        'Teach': 40,
        'Fine Manipulation': 40,
        'Research': 40,
        'Heavy Machinery': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    if not raw:
        return skill_set
    else:
        return base_skill_scores

def cyber_corporate_skillset(raw=False):
    skill_list = [ 
        'Status', 
        'Knowledge (Stock Market)', 
        'Research', 
        'Insight', 
        'Persuade', 
        'Command', 
        'Knowledge (Accounting)', 
        'Etiquette (Corporate)', 
        'Knowledge (Business)', 
        'Drive (Car)' ]
    base_skill_scores = {
        'Status': 30,
        'Knowledge (Stock Market)': 50,
        'Research': 30,
        'Insight': 40,
        'Persuade': 40,
        'Command': 40,
        'Knowledge (Accounting)': 40,
        'Etiquette (Corporate)': 40,
        'Knowledge (Business)': 40,
        'Drive (Car)': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    if not raw:
        return skill_set
    else:
        return base_skill_scores

def cyber_cop_skillset(raw=False):
    skill_list = [ 
        'Spot', 
        'Status', 
        'Firearms (Pistol)', 
        'Brawl', 
        'Melee Weapon (Baton)', 
        'Etiquette (Street)', 
        'Insight', 
        'Command', 
        'Persuade', 
        'Drive (Car)' ]
    base_skill_scores = {
        'Spot': 30,
        'Status': 50,
        'Firearms (Pistol)': 30,
        'Brawl': 40,
        'Melee Weapon (Baton)': 40,
        'Etiquette (Street)': 40,
        'Insight': 40,
        'Command': 40,
        'Persuade': 40,
        'Drive (Car)': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    if not raw:
        return skill_set
    else:
        return base_skill_scores

def cyber_nomad_skillset(raw=False):
    skill_list = [ 
        'Drive (Car)', 
        'Ride (Motorcycle)', 
        'Spot', 
        'Firearms (Rifle)', 
        'Melee Weapon', 
        'Brawl', 
        'Repair (Mechanical)', 
        'Track', 
        'Navigate', 
        'Knowledge (Survival)' ] 
    base_skill_scores = {
        'Drive (Car)': 30,
        'Ride (Motorcycle)': 50,
        'Spot': 30,
        'Firearms (Rifle)': 40,
        'Melee Weapon': 40,
        'Brawl': 40,
        'Repair (Mechanical)': 40,
        'Track': 40,
        'Navigate': 40,
        'Knowledge (Survival)': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    if not raw:
        return skill_set
    else:
        return base_skill_scores

def cyber_medtech_skillset(raw=False):
    skill_list = [ 
        'Medicine', 
        'First Aid', 
        'Technical Skill (Cryotank Operation)', 
        'Technical Skill (Cybernetics)', 
        'Insight', 
        'Science (Pharmacy)', 
        'Science (Zoology)', 
        'Spot', 
        'Persuade', 
        'Research' ]
    base_skill_scores = {
        'Medicine': 30,
        'First Aid': 50,
        'Technical Skill (Cryotank Operation)': 30,
        'Technical Skill (Cybernetics)': 40,
        'Insight': 40,
        'Science (Pharmacy)': 40,
        'Science (Zoology)': 40,
        'Spot': 40,
        'Persuade': 40,
        'Research': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    if not raw:
        return skill_set
    else:
        return base_skill_scores

def cyber_netrunner_skillset(raw=False):
    skill_list = [ 
        'Technical Skill (Computer Use)', 
        'Technical Skill (Computer Programming)', 
        'Technical Skill (Cyberdecks)', 
        'Technical Skill (Cybernetics)', 
        'Technical Skill (Electronic Security)', 
        'Research', 
        'Knowledge (The NET)',
        'Fine Manipulation', 
        'Spot', 
        'Persuade' ]
    base_skill_scores = {
        'Technical Skill (Computer Use)': 30,
        'Technical Skill (Computer Programming)': 50,
        'Technical Skill (Cyberdecks)': 30,
        'Technical Skill (Cybernetics)': 40,
        'Technical Skill (Electronic Security)': 40,
        'Research': 40,
        'Knowledge (The NET)': 40,
        'Fine Manipulation': 40,
        'Spot': 40,
        'Persuade': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    if not raw:
        return skill_set
    else:
        return base_skill_scores

def cyber_media_skillset(raw=False):
    skill_list = [ 
        'Persuade', 
        'Perform (Orate)', 
        'Research', 
        'Spot', 
        'Listen', 
        'Insight',
        'Etiquette (Corporate)', 
        'Etiquette (Street)', 
        'Technical Skill (Photo and Film)', 
        'Status' ]
    base_skill_scores = {
        'Persuade': 30,
        'Perform (Orate)': 50,
        'Research': 30,
        'Spot': 40,
        'Listen': 40,
        'Insight': 40,
        'Etiquette (Corporate)': 40,
        'Etiquette (Street)': 40,
        'Technical Skill (Photo and Film)': 40,
        'Status': 50 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    if not raw:
        return skill_set
    else:
        return base_skill_scores
