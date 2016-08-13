#
# BRP Professions SciFi
#

def skills_and_scores(skills,scores):
    skills_string = ''
    for s in skills:
        ss = str(scores[s])
        skills_string = skills_string + s + " " + ss + "% "
    return skills_string

def scifi_warrior_skillset():
    skill_list = [
        'Melee Weapon', 
        'Energy Weapon', 
        'Heavy Weapon', 
        'Brawl', 
        'Dodge', 
        'Hide', 
        'Spot', 
        'First Aid', 
        'Martial Art (Style)', 
        'Repair (Mechanical)' ]
    base_skill_scores = {
        'Melee Weapon': 50,
        'Energy Weapon': 40,
        'Heavy Weapon': 40,
        'Brawl': 30,
        'Dodge': 30,
        'Hide': 30,
        'Spot': 30,
        'First Aid': 30,
        'Martial Art (Style)': 30,
        'Repair (Mechanical)': 30 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def scifi_psyker_skillset():
    skill_list = [
        'Projection', 
        'Knowledge (Psionics)', 
        'Knowledge (Galactic)', 
        'Sense', 
        'Language (Alien)',
        'Research', 
        'Insight', 
        'Psychotherapy', 
        'Spot', 
        'Listen' ]
    base_skill_scores = {
        'Projection': 50,
        'Knowledge (Psionics)': 40,
        'Knowledge (Galactic)': 40,
        'Sense': 30,
        'Language (Alien)': 30,
        'Research': 30,
        'Insight': 30,
        'Psychotherapy': 30,
        'Spot': 30,
        'Listen': 30 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def scifi_jedi_skillset():
    skill_list = [
        'Melee Weapon (Energy Sword)', 
        'Command', 
        'Dodge', 
        'Jump', 
        'Knowledge (Galactic)',
        'Pilot (Starfighter)', 
        'Navigate', 
        'Language (Alien)', 
        'Insight', 
        'Spot' ]
    base_skill_scores = {
        'Melee Weapon (Energy Sword)': 50,
        'Command': 40,
        'Dodge': 40,
        'Jump': 30,
        'Knowledge (Galactic)': 30,
        'Pilot (Starfighter)': 30,
        'Navigate': 30,
        'Language (Alien)': 30,
        'Insight': 30,
        'Spot': 30 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def scifi_rogue_skillset():
    skill_list = [
        'Energy Weapon', 
        'Spot', 
        'Etiquette (Street)', 
        'Brawl', 
        'Hide',
        'Fast Talk', 
        'Melee Weapon', 
        'Knowledge (Law)', 
        'Technical Skill (Electronic Security)', 
        'Insight' ]
    base_skill_scores = {
        'Energy Weapon': 50,
        'Spot': 40,
        'Etiquette (Street)': 40,
        'Brawl': 30,
        'Hide': 30,
        'Fast Talk': 30,
        'Melee Weapon': 30,
        'Knowledge (Law)': 30,
        'Technical Skill (Electronic Security)': 30,
        'Insight': 30 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def scifi_smuggler_skillset():
    skill_list = [
        'Pilot (Starship)', 
        'Hide', 
        'Navigate', 
        'Brawl', 
        'Knowledge (Galactic)',
        'Fast Talk', 
        'Energy Weapon', 
        'Melee Weapon', 
        'Knowledge (Law)', 
        'Technical Skill (Electronic Security)' ]
    base_skill_scores = {
        'Pilot (Starship)': 50,
        'Hide': 40,
        'Navigate': 40,
        'Brawl': 30,
        'Knowledge (Galactic)': 30,
        'Fast Talk': 30,
        'Energy Weapon': 30,
        'Melee Weapon': 30,
        'Knowledge (Law)': 30,
        'Technical Skill (Electronic Security)': 30 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def scifi_noble_skillset():
    skill_list = [
        'Etiquette', 
        'Language (Alien)', 
        'Status', 
        'Technical Skill (Computer Use)', 
        'Bargain',
        'Command', 
        'Knowledge (Politics)', 
        'Knowledge (Galactic)', 
        'Appraise', 
        'Persuade' ]
    base_skill_scores = {
        'Etiquette': 50,
        'Language (Alien)': 40,
        'Status': 40,
        'Technical Skill (Computer Use)': 30,
        'Bargain': 30,
        'Command': 30,
        'Knowledge (Politics)': 30,
        'Knowledge (Galactic)': 30,
        'Appraise': 30,
        'Persuade': 30 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def scifi_technician_skillset():
    skill_list = [
        'Repair (Electrical)', 
        'Repair (Mechanical)', 
        'Technical Skill (Electronics)', 
        'Technical Skill (Computer Use)',
        'Science (Planetology)', 
        'Science (Quantum)', 
        'Teach', 
        'Fine Manipulation', 
        'Research', 
        'Heavy Machinery' ]
    base_skill_scores = {
        'Repair (Electrical)': 50,
        'Repair (Mechanical)': 40,
        'Technical Skill (Electronics)': 40,
        'Technical Skill (Computer Use)': 30,
        'Science (Planetology)': 30,
        'Science (Quantum)': 30,
        'Teach': 30,
        'Fine Manipulation': 30,
        'Research': 30,
        'Heavy Machinery': 30 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def scifi_agent_skillset():
    skill_list = [
        'Energy Weapon', 
        'Knowledge (Espionage)', 
        'Pilot (Any)', 
        'Listen', 
        'Research',
        'Spot', 
        'Stealth', 
        'Brawl', 
        'Disguise', 
        'Technical Skill (Electronic Security)' ]
    base_skill_scores = {
        'Energy Weapon': 50,
        'Knowledge (Espionage)': 40,
        'Pilot (Any)': 40,
        'Listen': 30,
        'Research': 30,
        'Spot': 30,
        'Stealth': 30,
        'Brawl': 30,
        'Disguise': 30,
        'Technical Skill (Electronic Security)': 30 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def scifi_gambler_skillset():
    skill_list = [
        'Gaming', 
        'Fast Talk', 
        'Sleight of Hand', 
        'Bargain', 
        'Brawl',
        'Dodge', 
        'Insight', 
        'Persuade', 
        'Science (Mathematics)', 
        'Spot' ]
    base_skill_scores = {
        'Gaming': 50,
        'Fast Talk': 40,
        'Sleight of Hand': 40,
        'Bargain': 30,
        'Brawl': 30,
        'Dodge': 30,
        'Insight': 30,
        'Persuade': 30,
        'Science (Mathematics)': 30,
        'Spot': 30 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

def scifi_trader_skillset():
    skill_list = [
        'Appraise', 
        'Bargain', 
        'Fast Talk', 
        'Knowledge (Galactic)', 
        'Knowledge (Business)',
        'Persuade', 
        'Research', 
        'Navigate', 
        'Insight', 
        'Pilot (Freighter)' ]
    base_skill_scores = {
        'Appraise': 50,
        'Bargain': 40,
        'Fast Talk': 40,
        'Knowledge (Galactic)': 30,
        'Knowledge (Business)': 30,
        'Persuade': 30,
        'Research': 30,
        'Navigate': 30,
        'Insight': 30,
        'Pilot (Freighter)': 30 }
    skill_set = skills_and_scores(skill_list,base_skill_scores)
    return skill_set

