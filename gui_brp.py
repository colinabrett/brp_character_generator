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
from brp_stats import *
#from brp_skills import *
from brp_professions import *
from dice_roller import *

Builder.load_file("gui_brp.kv")

class WelcomeScreen(Screen):
    pass

class SelectSystem(Screen):

    game = StringProperty()
    ruleset = StringProperty()

    def brp_system(self,*args):
        game = 'Basic Roleplaying'
        print(game)
        sm.get_screen("character_sheet").printrules(game)

    def mw_system(self,*args):
        game='Magic World'
        print(game)
        sm.get_screen("character_sheet").printrules(game)

    def mi_system(self,*args):
        game='Mythras Imperative'
        print(game)
        sm.get_screen("character_sheet").printrules(game)

    def coc_system(self,*args):
        game='Call of Cthulhu'
        print(game)
        sm.get_screen("character_sheet").printrules(game)

class SelectGenre(Screen):
#   pass
    def fantasy_genre(self,*args):
        genre_type='Fantasy'
        print(genre_type)
        sm.get_screen("character_sheet").printgenre(genre_type)

    def scifi_genre(self,*args):
        genre_type='Sci-Fi'
        print(genre_type)
        sm.get_screen("character_sheet").printgenre(genre_type)

    def cyberpunk_genre(self,*args):
        genre_type='Cyberpunk'
        print(genre_type)
        sm.get_screen("character_sheet").printgenre(genre_type)

    def wildwest_genre(self,*args):
        genre_type='Wild West'
        print(genre_type)
        sm.get_screen("character_sheet").printgenre(genre_type)

    def horror_genre(self,*args):
        genre_type='Horror'
        print(genre_type)
        sm.get_screen("character_sheet").printgenre(genre_type)


class SelectRace(Screen):

    def human(self,a,b):
        if b==True:
            race="Human"
            statblock = human_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

    def elf(self,a,b):
        if b==True:
            race="Elf"
            statblock = elf_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

    def dwarf(self,a,b):
        if b==True:
            race="Dwarf"
            statblock = dwarf_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

    def orc(self,a,b):
        if b==True:
            race="Orc"
            statblock = orc_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

    def goblin(self,a,b):
        if b==True:
            race="Goblin"
            statblock = goblin_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)


class SelectProfession(Screen):
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
        skills_list = rogue_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def priest(self,*args):
        prof = 'Priest'
        skills_list = rogue_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

class CharacterSheet(Screen):

    mysb = StringProperty()
    mycr = StringProperty()
    myscm = StringProperty()
    myscb = StringProperty()
    ruleset = StringProperty()
    race = StringProperty()
    genre = StringProperty()
    profession = StringProperty()
    skills = StringProperty()

    def print_stats(self,mystats):
        print(mystats)
        stat_string = ''
        statlist = [ 'STR' , 'CON' , 'SIZ' , 'INT' , 'POW' , 'DEX' , 'APP' , 'EDU' ]
        for stat in statlist:
            ss = str(mystats[stat])
            stat_string = stat_string + stat + " [" + ss + "] "
        return stat_string


    def print_rolls(self,myrolls):
        print(myrolls)
        char_string = ''
        rolls_list = [ 'Effort' , 'Stamina' , 'Idea' , 'Luck' , 'Agility' , 'Charisma' , 'Know' ]
        for r in rolls_list:
            qq = str(myrolls[r])
            char_string = char_string + r + " " + qq + "% "
        return char_string

    def print_scm(self,myscm):
        print(myscm)
        scm_string = ''
        scm_list = [ 'Physical' , 'Communication' , 'Knowledge' , 'Manipulation' , 'Perception' ]
        for s in scm_list:
            tt = str(myscm[s])
            scm_string = scm_string + s + " " + tt + "% "
        return scm_string

    def print_scb(self,myscb):
        print(myscb)
        scb_string = ''
        scb_list = [ 'Combat' , 'Communication' , 'Manipulation' , 'Mental' , 'Perception', 'Physical' ]
        for s in scb_list:
            zz = str(myscb[s])
            scb_string = scb_string + s + " " + zz + "% "
        return scb_string

    def printcharacter(self,my_sb,my_cr,my_scm,my_scb):

        self.mysb = self.print_stats(my_sb)
        self.mycr = self.print_rolls(my_cr)
        self.myscm = self.print_scm(my_scm)
        self.myscb = self.print_scb(my_scb)

        print (self.mysb)
        print (self.mycr)
        print (self.myscm)
        print (self.myscb)

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
sm.add_widget(SelectRace(name='race'))
sm.add_widget(SelectProfession(name='profession'))
sm.add_widget(CharacterSheet(name='character_sheet'))

class GuiBrp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    GuiBrp().run()
