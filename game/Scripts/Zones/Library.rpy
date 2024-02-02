default prepared_blink = False
default prepared_q_inv = False
default spells_known = []
default spells_researched = []
default actual_learning = None
default text = ""
default at_least_one_spell_to_show = False

init python:
    class Spell:
        def __init__(self, name, req_lvl, cost, description):
            self.name = name
            self.rLvl = req_lvl
            self.cost = cost
            self.desc = description

default allowed_spells = [
    Spell("Invisibility", 3, 0, "A spell that takes time to cast but then grants user to be invisible for short period of time."),
    Spell("Levitate", 6, 0, "A spell that takes time to cast and you need to concentrate on it but allows to make anything lighter then you as light as feather."),
    Spell("Blink", 9, 0, "It have be prepared at home but then can be cast anytime to temporarily blind anyone looking, giving you time to run. You yourself will get partialy blinded as well so it's not reccomended to use offensively."),
    Spell("Imbue", 12, 0, "You need safe place and time to cast this on a magical item. Such item will get new charges. Usefull for locking runes and such.")
]
default restricted_spells = [
    Spell("Strip", 10, 100, "A spell that takes time to cast and is required to be very close to target. Once used it removes clothing temporarily."),
    Spell("Quick invisibility", 12, 150, "Extremly fast spell that takes a long time to prepare but can be used instantly to get invisible. Prepare at safe place."),
    Spell("Giant strength", 15, 200, "A fast spell usable in combat that counts as +10 sword skill."),
    Spell("Howkeye", 15, 200, "A fast spell usable in combat that counts as +10 bow skill."),
    Spell("Irresistible look", 20, 300, "A spell taht takes time to cast but once applied on a target, that target can force any sexual act on opposit sex."),
    Spell("Blessed seed", 30, 500, "This is more a squible then a spell... like an idea of a crazy perv written on side of one less atractive book. You'll need to research this yourself but when completed, it's possible to fertile even sterile women or other spieces as it artifically creates an egg from partner's body and mix it directly with your seed."),
]

label learnSpell:
    if actual_learning.rLvl > magiclvl:
        $ renpy.notify ("{color=#fff}Magic skill check: {color=#A50000}Fail. ([magiclvl] < [actual_learning.rLvl])")
        mc "{i}This spell is still too complicated for me to learn."
        jump cleanLearning

    # "To learn this spell you need to spent gold for special items that helps with your research. Do you want to pay [actual_learning.cost] gp?"
    "You've learned new spell: [actual_learning.name]"
    $ spells_known.append(actual_learning.name)
    $ time += 2
    jump cleanLearning


label researchSpell:
    scene library with fade
    mc "{i}To research about this spell I need to spent gold for special items and experiments. It will cost [actual_learning.cost] gp."
    if money >= actual_learning.cost:
        menu:
            "Do it later...":
                pass
            "Let's research it!":
                hide screen hud
                show animationread
                play sound chime
                $ money -= actual_learning.cost
                $ time += 2
                $ allowed_spells.append(actual_learning)
                $ spells_researched.append(actual_learning.name)
                "You've researched new spell: [actual_learning.name] and you can learn to cast it later."
                hide animationread
    jump cleanLearning


label cleanLearning:
    $actual_learning = None
    hide screen learn_magic
    hide screen research_magic
    jump library


screen research_magic(spell_list):
    tag menu
    style_prefix "choice"
    frame:
        xalign 0.5 yalign 0.5
        vbox:
            for spell in spell_list:
                textbutton f"{spell.name}: required skill {spell.rLvl}, research cost {spell.cost}" action [Hide("research_magic"), SetVariable("actual_learning", spell), Jump("researchSpell")]
            textbutton "Go back" action [Hide("learn_magic"), Jump("library")]


screen learn_magic(spell_list):
    tag menu
    style_prefix "choice"
    frame:
        xalign 0.5 yalign 0.5
        vbox:
            for spell in spell_list:
                textbutton f"{spell.name}: required skill {spell.rLvl}" action [Hide("learn_magic"), SetVariable("actual_learning", spell), Jump("learnSpell")]
            textbutton "Go back" action [Hide("learn_magic"), Jump("library")]


label library:
    if time >= 4:
        scene villagen
        mc "The Library is closed."
        jump maplimbo
    hide screen screenmap
    show screen hud
    stop music
    scene library
    "You arrive at the library."
    menu:
        "Lori":
            jump loriTalk
        "Book of Monsters":
            jump monsterindex
        "Study Astyllian with Lori":
            hide screen hud
            if loritea == 0:
                scene black with fade
                l "Oh, [mc]. Would you, uhm, would you like some tea to drink while you read?"
                mc "Oh, that would be great! Thanks."
                l "I'll bring you a cup right away... You're ok with Kahata tea, right?"
                mc "Yeah."
                l "Ok, awesome!"
                $ loritea += 1
            show animationreadl
            "Lori brings a huge book and slumps it on the desk. She opens it and thus begins the lesson."
            mc "Thanks, Lori."
            l "Anytime... was the tea good?"
            if magiclvl == 1:
                mc "Yeah, as always."
            else:
                mc "Yeah, it's great."
            l "Thanks!"
            hide animationreadl
            $ magic += 1
            if chartrait == 1:
                $ magic = 2
            if magic == 2:
                play sound chime
                $ renpy.notify ("{color=#00C413}Your Sorcery stat has increased.")
                $ magiclvl += 1
                $ magic -= 2
            $ time += 1
            jump library
        "Study restricted magic":
            if time > 2:
                "You are after some new means of going around using magic but you are aware that library would close before you get anything useful. You should come early next time."
                jump library
            "You roam the library and read random books in search for new knowledge and opportunities to learn something new."
            $ spell_list = [spell for spell in restricted_spells if not spell.name in spells_researched and not spell.name in spells_known and magiclvl*2 >= spell.rLvl]
            if spell_list == []:
                mc "{i}I haven't find anything of use right now... maybe if I study more I can locate some rarities then."
            else:
                mc "{i} I've found few mysteries... which should I study?"
                call screen research_magic(spell_list)
            jump library
        "Learn new spells":
            if time > 2:
                mc "{i}Finding the correct book to learn from and learning any spell takes a long time so I should come back early next time."
                jump library
            $ spell_list = [spell for spell in allowed_spells if not spell.name in spells_known and magiclvl*2 >= spell.rLvl]
            if spell_list == []:
                mc "{i}I haven't find anything of use right now... maybe if I study more I can locate some usefull spells then."
            else:
                call screen learn_magic(spell_list)
            jump library