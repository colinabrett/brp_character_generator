#
# Import Kivy Modules
#

import kivy
import sys
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, ListProperty

#
# Import custom modules
#

from brp_stats import *
#from brp_skills import *
from brp_professions_fantasy import *
from brp_professions_scifi import *
from brp_professions_cyber import *
from brp_professions_wildwest import *
from brp_professions_horror import *
from brp_races_fantasy import *
from brp_races_scifi import *
from brp_races_cyber import *
from brp_races_wildwest import *
from brp_races_horror import *
from dice_roller import *

Builder.load_file("gui_brp.kv")

class WelcomeScreen(Screen):
    pass

class SelectSystem(Screen):

    game = StringProperty()
    ruleset = StringProperty()

    def brp_system(self,*args):
        game = 'Basic Roleplaying'
#       print(game)
        sm.get_screen("character_sheet").printrules(game)

    def mw_system(self,*args):
        game='Magic World'
#       print(game)
        sm.get_screen("character_sheet").printrules(game)

    def mi_system(self,*args):
        game='Mythras Imperative'
#       print(game)
        sm.get_screen("character_sheet").printrules(game)

    def coc_system(self,*args):
        game='Call of Cthulhu'
#       print(game)
        sm.get_screen("character_sheet").printrules(game)

class SelectGenre(Screen):
#   pass
    def fantasy_genre(self,*args):
        genre_type='Fantasy'
#       print(genre_type)
        sm.get_screen("character_sheet").printgenre(genre_type)
        sm.current = 'race_fantasy'

    def scifi_genre(self,*args):
        genre_type='Sci-Fi'
#       print(genre_type)
        sm.get_screen("character_sheet").printgenre(genre_type)
        sm.current = 'race_scifi'

    def cyberpunk_genre(self,*args):
        genre_type='Cyberpunk'
#       print(genre_type)
        sm.get_screen("character_sheet").printgenre(genre_type)
        sm.current = 'race_cyberpunk'

    def wildwest_genre(self,*args):
        genre_type='Wild West'
#       print(genre_type)
        sm.get_screen("character_sheet").printgenre(genre_type)
        sm.current = 'race_wildwest'

    def horror_genre(self,*args):
        genre_type='Horror'
#       print(genre_type)
        sm.get_screen("character_sheet").printgenre(genre_type)
        sm.current = 'race_horror'

class SelectRaceFantasy(Screen):

    def fantasy_human(self,a,b):
        if b==True:
            race="Human"
            statblock = fantasy_human_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)
            sm.current = 'profession_fantasy'

    def fantasy_elf(self,a,b):
        if b==True:
            race="Elf"
            statblock = fantasy_elf_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)
            sm.current = 'profession_fantasy'

    def fantasy_dwarf(self,a,b):
        if b==True:
            race="Dwarf"
            statblock = fantasy_dwarf_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)
            sm.current = 'profession_fantasy'

    def fantasy_orc(self,a,b):
        if b==True:
            race="Orc"
            statblock = fantasy_orc_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)
            sm.current = 'profession_fantasy'

    def fantasy_goblin(self,a,b):
        if b==True:
            race="Goblin"
            statblock = fantasy_goblin_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)
            sm.current = 'profession_fantasy'

class SelectRaceSciFi(Screen):

    def scifi_human(self,a,b):
        if b==True:
            race="Human"
            statblock = scifi_human_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)
            sm.current = 'profession_scifi'

    def scifi_eldar(self,a,b):
        if b==True:
            race="Eldar"
            statblock = scifi_eldar_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)
            sm.current = 'profession_scifi'

    def scifi_squat(self,a,b):
        if b==True:
            race="Squat"
            statblock = scifi_squat_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)
            sm.current = 'profession_scifi'

    def scifi_ork(self,a,b):
        if b==True:
            race="Ork"
            statblock = scifi_ork_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)
            sm.current = 'profession_scifi'

    def scifi_gretchin(self,a,b):
        if b==True:
            race="Gretchin"
            statblock = scifi_gretchin_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)
            sm.current = 'profession_scifi'


class SelectRaceWildWest(Screen):

    def wildwest_human(self,a,b):
        if b==True:
            race="Human"
            statblock = wildwest_human_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)
            sm.current = 'profession_wildwest'

    def wildwest_elf(self,a,b):
        if b==True:
            race="Elf"
            statblock = wildwest_elf_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)
            sm.current = 'profession_wildwest'

    def wildwest_dwarf(self,a,b):
        if b==True:
            race="Dwarf"
            statblock = wildwest_dwarf_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)
            sm.current = 'profession_wildwest'

    def wildwest_orc(self,a,b):
        if b==True:
            race="Orc Tribe"
            statblock = wildwest_orc_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)
            sm.current = 'profession_wildwest'

    def wildwest_goblin(self,a,b):
        if b==True:
            race="Goblin Tribe"
            statblock = wildwest_goblin_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)
            sm.current = 'profession_wildwest'


class SelectRaceHorror(Screen):

    def horror_human(self,a,b):
        if b==True:
            race="Horror Human"
            statblock = horror_human_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)
            sm.current = 'profession_horror'

    def horror_elf(self,a,b):
        if b==True:
            race="Horror Elf"
            statblock = horror_elf_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)
            sm.current = 'profession_horror'

    def horror_dwarf(self,a,b):
        if b==True:
            race="Horror Dwarf"
            statblock = horror_dwarf_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)
            sm.current = 'profession_horror'

    def horror_orc(self,a,b):
        if b==True:
            race="Horror Orc"
            statblock = horror_orc_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)
            sm.current = 'profession_horror'

    def horror_goblin(self,a,b):
        if b==True:
            race="Horror Goblin"
            statblock = horror_goblin_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)
            sm.current = 'profession_horror'


class SelectRaceCyberpunk(Screen):

    def cyber_human(self,a,b):
        if b==True:
            race="Cyber Human"
            statblock = cyber_human_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)
            sm.current = 'profession_cyberpunk'

    def cyber_elf(self,a,b):
        if b==True:
            race="Cyber Elf"
            statblock = cyber_elf_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)
            sm.current = 'profession_cyberpunk'

    def cyber_dwarf(self,a,b):
        if b==True:
            race="Cyber Dwarf"
            statblock = cyber_dwarf_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)
            sm.current = 'profession_cyberpunk'

    def cyber_orc(self,a,b):
        if b==True:
            race="Cyber Orc"
            statblock = cyber_orc_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)
            sm.current = 'profession_cyberpunk'

    def cyber_goblin(self,a,b):
        if b==True:
            race="Cyber Goblin"
            statblock = cyber_goblin_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)
            sm.current = 'profession_cyberpunk'



class SelectProfessionFantasy(Screen):
#   pass

    def warrior(self,*args):
        prof = 'Warrior'
        skills_list = warrior_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def rogue(self,*args):
        prof = 'Rogue'
        skills_list = rogue_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def wizard(self,*args):
        prof = 'Wizard'
        skills_list = wizard_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def priest(self,*args):
        prof = 'Priest'
        skills_list = priest_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

class SelectProfessionSciFi(Screen):
#   pass

    def soldier(self,*args):
        prof = 'Soldier'
        skills_list = warrior_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def smuggler(self,*args):
        prof = 'Smuggler'
        skills_list = smuggler_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def psyker(self,*args):
        prof = 'Psyker'
        skills_list = psyker_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def marine(self,*args):
        prof = 'Marine'
        skills_list = marine_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

class SelectProfessionCyberpunk(Screen):
#   pass

    def solo(self,*args):
        prof = 'Solo'
        skills_list = solo_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def fixer(self,*args):
        prof = 'Fixer'
        skills_list = fixer_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def rocker(self,*args):
        prof = 'Rocker'
        skills_list = rocker_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def techie(self,*args):
        prof = 'Techie'
        skills_list = techie_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

class SelectProfessionWildWest(Screen):
#   pass

    def cavalry(self,*args):
        prof = 'Cavalry'
        skills_list = cavalry_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def gambler(self,*args):
        prof = 'Gambler'
        skills_list = gambler_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def madscientist(self,*args):
        prof = 'Mad Scientist'
        skills_list = madscientist_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def brave(self,*args):
        prof = 'Brave'
        skills_list = brave_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

class SelectProfessionHorror(Screen):
#   pass

    def doctor(self,*args):
        prof = 'Doctor'
        skills_list = doctor_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def detective(self,*args):
        prof = 'Detective'
        skills_list = detective_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def sorcerer(self,*args):
        prof = 'Sorcerer'
        skills_list = sorcerer_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def adventurer(self,*args):
        prof = 'Adventurer'
        skills_list = adventurer_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

class CharacterSheet(Screen):

    mysb = StringProperty()
    mycr = StringProperty()
    myscm = StringProperty()
    myscb = StringProperty()
    ruleset = StringProperty()
#   game = StringProperty()
    race = StringProperty()
    genre = StringProperty()
    profession = StringProperty()
    skills = StringProperty()

    def print_stats(self,mystats):
#       print(mystats)
        stat_string = ''
        statlist = [ 'STR' , 'CON' , 'SIZ' , 'INT' , 'POW' , 'DEX' , 'APP' , 'EDU' ]
        for stat in statlist:
            ss = str(mystats[stat])
            stat_string = stat_string + stat + " [" + ss + "] "
        return stat_string


    def print_rolls(self,myrolls):
#       print(myrolls)
        char_string = ''
        rolls_list = [ 'Effort' , 'Stamina' , 'Idea' , 'Luck' , 'Agility' , 'Charisma' , 'Know' ]
        for r in rolls_list:
            qq = str(myrolls[r])
            char_string = char_string + r + " " + qq + "% "
        return char_string

    def print_scm(self,myscm):
#       print(myscm)
        scm_string = ''
        scm_list = [ 'Physical' , 'Communication' , 'Knowledge' , 'Manipulation' , 'Perception' ]
        for s in scm_list:
            tt = str(myscm[s])
            scm_string = scm_string + s + " " + tt + "% "
        return scm_string

    def print_scb(self,myscb):
#       print(myscb)
        scb_string = ''
        scb_list = [ 'Combat' , 'Communication' , 'Manipulation' , 'Mental' , 'Perception', 'Physical' ]
        for s in scb_list:
            zz = str(myscb[s])
            scb_string = scb_string + s + " " + zz + "% "
        return scb_string

    def printcharacter(self,my_sb,my_cr,my_scm,my_scb):
#       print(game)
        self.mysb = self.print_stats(my_sb)
        self.mycr = self.print_rolls(my_cr)
        self.myscm = self.print_scm(my_scm)
        self.myscb = self.print_scb(my_scb)

#       print (self.mysb)
#       print (self.mycr)
#       print (self.myscm)
#       print (self.myscb)

    def printrules(self,rs):
        ruleset = str(rs)
        self.ruleset = str(rs)
        return ruleset

    def printrace(self,rc):
        race = str(rc)
        self.race = str(rc)
        return race

    def printgenre(self,rg):
        genre = str(rg)
        self.genre = str(rg)
        return genre

    def printprofession(self,p):
        profession = str(p)
        self.profession = str(p)
        return profession

    def printskills(self,p):
        skills_string = ''
        skills = p
        self.skills = p
        return skills

sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='welcome'))
sm.add_widget(SelectSystem(name='system_type'))
sm.add_widget(SelectGenre(name='genre'))
sm.add_widget(SelectRaceFantasy(name='race_fantasy'))
sm.add_widget(SelectRaceSciFi(name='race_scifi'))
sm.add_widget(SelectRaceCyberpunk(name='race_cyberpunk'))
sm.add_widget(SelectRaceWildWest(name='race_wildwest'))
sm.add_widget(SelectRaceHorror(name='race_horror'))
sm.add_widget(SelectProfessionFantasy(name='profession_fantasy'))
sm.add_widget(SelectProfessionSciFi(name='profession_scifi'))
sm.add_widget(SelectProfessionCyberpunk(name='profession_cyberpunk'))
sm.add_widget(SelectProfessionWildWest(name='profession_wildwest'))
sm.add_widget(SelectProfessionHorror(name='profession_horror'))
sm.add_widget(CharacterSheet(name='character_sheet'))

class GuiBrp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    GuiBrp().run()
