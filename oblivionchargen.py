# This will generate a brand new character for gameplay in Oblivion
import random

sexChoice = random.choice(['Male', 'Female'])

print('This is the sex your character will be')

print(sexChoice)

raceChoice = random.choice([
    'Argonian', 
    'Breton',
    'Dark Elf',
    'High Elf',
    'Imperial',
    'Khajit',
    'Nord',
    'Orc',
    'Wood Elf'
    ])

print('This is the race your character will be')
print(raceChoice)

birthsignChoice = random.choice([
    'Apprentice',
    'Atronach',
    'Lady',
    'Lord',
    'Lover',
    'Mage',
    'Ritual',
    'Serpent',
    'Shadow',
    'Steed',
    'Thief',
    'Tower',
    'Warrior'
])

print('This is the birthsign you will choose')
print(birthsignChoice)

classChoice = random.choice([
    'Acrobat',
    'Agent',
    'Archer',
    'Assassin',
    'Barbarian',
    'Bard',
    'Battlemage',
    'Crusader',
    'Healer',
    'Knight',
    'Mage',
    'Monk',
    'Nightblade',
    'Pilgrim',
    'Rogue',
    'Scout',
    'Sorcerer',
    'Spellsword',
    'Thief',
    'Warrior',
    'Witchhunter'
])

print('This is the prebuilt class you can use')
print(classChoice)

print('Or make a class with the following specialization, attributes and skills')

print('This is your specialization')

specializationList = [
    'Combat',
    'Magic',
    'Stealth'
]

specializationChoice = random.choice(specializationList)

print(specializationChoice)

print('These are your attributes')

attributeList = [
    'Agility',
    'Endurance',
    'Intelligence',
    'Luck',
    'Perception',
    'Speed',
    'Strength',    
]

attributeChoiceOne = random.choice(attributeList)

attributeList.remove(attributeChoiceOne)

attributeChoiceTwo = random.choice(attributeList)

print(
    attributeChoiceOne,
    attributeChoiceTwo
)

skillList = [
    'Armorer',
    'Athletics',
    'Blade',
    'Block',
    'Blunt',
    'Hand to Hand',
    'Heavy Armor',
    'Alchemy',
    'Alteration',
    'Conjuration',
    'Destruction',
    'Illusion',
    'Mysticism',
    'Restoration',
    'Acrobatics',
    'Light Armor',
    'Marksman',
    'Mercantile',
    'Security',
    'Sneak',
    'Speechcraft'
]

print('These are your skills')

skillChoiceOne = random.choice(skillList)

skillList.remove(skillChoiceOne)

skillChoiceTwo = random.choice(skillList)

skillList.remove(skillChoiceTwo)

skillChoiceThree = random.choice(skillList)

skillList.remove(skillChoiceThree)

skillChoiceFour = random.choice(skillList)

skillList.remove(skillChoiceFour)

skillChoiceFive = random.choice(skillList)

skillList.remove(skillChoiceFive)

skillChoiceSix = random.choice(skillList)

skillList.remove(skillChoiceSix)

skillChoiceSeven = random.choice(skillList)

print(skillChoiceOne, skillChoiceTwo, skillChoiceThree, skillChoiceFour, skillChoiceFive, skillChoiceSix, skillChoiceSeven)

difficultyChoice = random.choice([
    'Very Easy',
    'Easy',
    'Medium',
    'Hard',
    'Very Hard'
])

print('This is the difficulty you will play at, good luck!')

print(difficultyChoice)