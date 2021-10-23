# This will generate a brand new character for gameplay in Oblivion
import random

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

print(raceChoice)

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

print(classChoice)

print('Or make a class with the following attributes')

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
    'Security'
    'Sneak',
    'Speechcraft'
]

skillChoiceOne = random.choice(skillList)

