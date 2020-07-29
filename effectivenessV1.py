weakness = {
    'normal': ['fighting'],
    'water': ['electric', 'grass'],
    'fire': ['water', 'ground', 'rock'],
    'grass': ['fire', 'ice', 'poison', 'flying', 'bug'],
    'ice': ['fire', 'fighting', 'rock', 'steel'],
    'fighting': ['flying', 'psychic', 'fairy'],
    'poison': ['ground', 'psychic'],
    'ground': ['water', 'grass', 'ice'],
    'flying': ['electric', 'ice', 'rock'],
    'psychic': ['bug', 'ghost', 'dark'],
    'bug': ['fire', 'flying', 'rock'],
    'rock': ['water', 'grass', 'fighting', 'ground', 'steel'],
    'ghost': ['ghost', 'dark'],
    'dragon': ['ice', 'dragon', 'fairy'],
    'dark': ['fighting', 'bug', 'fairy'],
    'steel': ['fire', 'fighting', 'ground'],
    'fairy': ['poison', 'steel']
}

user_input = input('Enter a whose weakness you want to calculate: ').lower()
weaknesses = weakness[user_input]
result = f'{user_input} is weak to: \n'
for t in weaknesses:
    result += f'{t} \n'
print(result)
