# Professions for Mythras Imperative
from brp_professions_fantasy import skills_and_scores
def mi_agent(raw=False):
    """ Agent (Agitator, Assassin, Detective, Informer, Spy...) skills"""
    base_skill_scores = {
        "standard" : {
            "Conceal" : 0, 
            "Deceit" : 0, 
            "Evade" : 0, 
            "Insight" : 0, 
            "Perception" : 0, 
            "Stealth" : 0, 
            "Combat Style (Specific Agent or Cultural Style)" : 0
        },
        "professional" : {
            "Culture (any)" : 0, 
            "Disguise" : 0,
            "Language (any)" : 0, 
            "Sleight" : 0, 
            "Streetwise" : 0, 
            "Survival" : 0, 
            "Track" : 0
        }
    }
    skill_set = skills_and_scores(base_skill_scores.keys(),base_skill_scores)
    if not raw:
        return skill_set
    else:
        return base_skill_scores
