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