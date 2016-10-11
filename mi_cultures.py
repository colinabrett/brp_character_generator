# Mythras Imperative cultures
# skills are categorised as standard or professional
from dice_roller import *
def barbarian():
    skill_list = {
        "standard" : {
            "Athletics" : 0,
            "Brawn" : 0,
            "Endurance" : 0,
            "First Aid" : 0,
            "Locale" : 0,
            "Perception" : 0,
            "Combat Style" : 0,
            
        },
        "professional" : {
            "Craft" : 0,
            "Healing" : 0,
            "Lore" : 0,
            "Musicianship" : 0,
            "Navigate" : 0,
            "Seamanship" : 0,
            "Survival" : 0,
            "Track" : 0
        }
    }
    if straight_dice() < 4:
        skill_list["standard"]["Boating"] = 0
    else:
        skill_list["standard"]["Ride"] = 0
    return skill_list

def civilised():
    skill_list = {
        "standard" : {
            "Conceal" : 0,
            "Deceit" : 0,
            "Drive" : 0,
            "Influence" : 0,
            "Insight" : 0,
            "Locale" : 0,
            "Willpower" : 0,
            "Combat Style" : 0
        },
        "professional" : {
            "Art (any)" : 0,
            "Commerce" : 0,
            "Craft (any)" : 0,
            "Courtesy" : 0,
            "Language (any)" : 0,
            "Lore (any)" : 0,
            "Musicianship" : 0,
            "Streetwise" : 0
        }
    }
    return skill_list

def nomadic():
    """; Standard and two Skills: of the , Athletics, , , , , , Drive or Ride. Combat Style
 Professional Skills: Craft (any), Culture (any), Language
 (any), Lore (any), Musicianship, Navigate, Survival, Track
 Primitive
 """
    skill_list = {
        "standard" : {
            "Endurance" : 0,
            "First Aid" : 0,
            "Locale" : 0,
            "Perception" : 0,
            "Stealth" : 0,
            "Combat Style" : 0
        },
        "professional" : {
            "Art (any)" : 0,
            "Commerce" : 0,
            "Craft (any)" : 0,
            "Courtesy" : 0,
            "Language (any)" : 0,
            "Lore (any)" : 0,
            "Musicianship" : 0,
            "Streetwise" : 0
        }
    }
    additional_standard = ["Athletics", "Boating", "Swim"]
    if straight_dice() < 4:
        additional_standard.append("Drive")
    else:
        additional_standard.append("Ride")
    extras = random.sample(set(additional_standard), 2)
    for skill in extras:
        skill_list["standard"][skill] = 0
    
    return skill_list

def primitive():
    """Primitive cultural skills"""
    skill_list = {
        "standard" : {
            "Brawn" : 0,
            "Endurance" : 0,
            "Evade" : 0,
            "Locale" : 0,
            "Perception" : 0,
            "Stealth" : 0
        },
        "professional" : {
            "Craft (any)" : 0,
            "Healing" : 0,
            "Navigate" : 0,
            "Lore (any)" : 0,
            "Musicianship" : 0,
            "Survival" : 0,
            "Track" :0
        }
    }
    additional_standard = ["Athletics", "Boating", "Swim"]
    extras = random.sample(set(additional_standard), 1)
    for skill in extras:
        skill_list["standard"][skill] = 0
    return skill_list
    

