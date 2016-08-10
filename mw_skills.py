#
# Skills list for Magic World based games
#

def mw_skill_bases():

    mw_skill_dict = {
        'Art' : 05,
        'Bargain' :  15,
        'Brawl' : 20,
        'Climb' : 40,
        'Conceal Object'  : 25,
        'Craft'  : 05,
        'Disguise' : 15,
        'Dodge' : self.statblock["DEX"] * 2,
        'Evaluate' : 15,
        'Fast Talk' : 05,
        'Hide' : 20,
        'Insight' : 15,
        'Jump' : 05,
        'Listen' : 25,
        'Lore Common' : 15,
        'Lore Rare' : 0,
        'Move Quietly' : 20,
        'Nature' : 25,
        'Navigate' : 10,
        'Oratory'  : 05,
        'Other Language'  : 0,
        'Own Language'  : self.statblock["INT"] * 5,
        'Physik'  : 30,
        'Pick Lock'  : 05,
        'Potions' : 0,
        'Repair/Devise' : self.statblock["DEX"] * 4,
        'Ride' :  35,
        'Sailing' : 15,
        'Scribe' : 0,
        'Search' : 20,
        'Sense' : 15,
        'Swim' : 25,
        'Throw' : 25,
        'Track' : 10,
        'Trap' : 05,
        'Weapon Skill' :  0,
        'World Lore' : 15,
        'Wrestle' : 25
}
