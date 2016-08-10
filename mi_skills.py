#
# Skill list for Mythras Imperative based games
#

def mi_skill_bases():

    mi_standard_skill_dict = {
        'Athletics' : self.statblock["STR"] + self.statblock["DEX"],
        'Boating' : self.statblock["STR"] + self.statblock["CON"],
        'Brawn' : self.statblock["STR"] + self.statblock["SIZ"],
        'Combat Style' : self.statblock["STR"] + self.statblock["DEX"],
        'Conceal' : self.statblock["DEX"] + self.statblock["POW"],
        'Customs' : self.statblock["INT"] * 2 + 40,
        'Dance' : self.statblock["DEX"] + self.statblock["CHA"],
        'Deceit' : self.statblock["INT"] + self.statblock["CHA"],
        'Drive' : self.statblock["DEX"] + self.statblock["POW"],
        'Endurance' : self.statblock["CON"] * 2,
        'Evade' : self.statblock["DEX"] * 2,
        'First Aid' : self.statblock["INT"] + self.statblock["DEX"],
        'Influence' : self.statblock["CHA"] * 2,
        'Insight' : self.statblock["INT"] + self.statblock["POW"],
        'Locale' : self.statblock["INT"] * 2,
        'Native Tongue' : self.statblock["INT"] + self.statblock["CHA"] + 40,
        'Perception' : self.statblock["INT"] + self.statblock["POW"],
        'Ride' : self.statblock["DEX"] + self.statblock["POW"],
        'Sing' : self.statblock["CHA"] + self.statblock["POW"],
        'Stealth' : self.statblock["DEX"] + self.statblock["INT"],
        'Swim' : self.statblock["STR"] + self.statblock["CON"],
        'Unarmed' : self.statblock["STR"] + self.statblock["DEX"],
        'Willpower' : self.statblock["POW"] * 2
}

    mi_professional_skill_dicy = {
        'Acting' : self.statblock["CHA"] * 2,
        'Acrobatics' : self.statblock["STR"] + self.statblock["DEX"],
        'Art' : self.statblock["POW"] + self.statblock["CHA"],
        'Astrogation' : self.statblock["INT"] * 2,
        'Bureaucracy' : self.statblock["INT"] * 2,
        'Commerce' : self.statblock["INT"] + self.statblock["CHA"],
        'Comms' : self.statblock["INT"] * 2,
        'Computers' : self.statblock["INT"] * 2,
        'Courtesy' : self.statblock["INT"] + self.statblock["CHA"],
        'Craft' : self.statblock["DEX"] + self.statblock["INT"],
        'Culture' : self.statblock["INT"] * 2,
        'Demolitions' : self.statblock["INT"] + self.statblock["POW"],
        'Disguise' : self.statblock["INT"] + self.statblock["CHA"],
        'Electronics' : self.statblock["DEX"] + self.statblock["INT"],
        'Engineering' : self.statblock["INT"] * 2,
        'Forgery' : self.statblock["DEX"] + self.statblock["INT"],
        'Gambling' : self.statblock["INT"] + self.statblock["POW"],
        'Healing' : self.statblock["INT"] + self.statblock["POW"],
        'Language (Specific Language)' : self.statblock["INT"] + self.statblock["CHA"],
        'Literacy (Specific Language)' : self.statblock["INT"] * 2,
        'Lockpicking' : self.statblock["DEX"] * 2,
        'Lore' : self.statblock["INT"] * 2,
        'Mechanisms' : self.statblock["DEX"] + self.statblock["INT"],
        'Musicianship' : self.statblock["DEX"] + self.statblock["CHA"],
        'Navigation' : self.statblock["INT"] + self.statblock["POW"],
        'Oratory' : self.statblock["POW"] + self.statblock["CHA"],
        'Pilot' : self.statblock["DEX"] + self.statblock["INT"],
        'Politics' : self.statblock["INT"] + self.statblock["CHA"],
        'Research' : self.statblock["INT"] + self.statblock["POW"],
        'Science' : self.statblock["INT"] * 2,
        'Seamanship' : self.statblock["INT"] + self.statblock["CON"],
        'Seduction' : self.statblock["INT"] + self.statblock["CHA"],
        'Sensors' : self.statblock["INT"] + self.statblock["POW"],
        'Sleight' : self.statblock["DEX"] + self.statblock["CHA"],
        'Streetwise' : self.statblock["POW"] + self.statblock["CHA"],
        'Survival' : self.statblock["CON"] + self.statblock["POW"],
        'Teach' : self.statblock["INT"] + self.statblock["CHA"],
        'Track' : self.statblock["INT"] + self.statblock["CON"]
}

