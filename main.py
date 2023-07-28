player = {
    'name': 'Ryu',
    'age': 22,
    'alive': True,
    'fav_food': ["pizza", "korean"],
    'disapear': 'soon'
}
print(player.get('age'))
print(player['alive'])
print(player.get('fav_food'))
player.pop('disapear')
print(player)
player['xp'] = 250
print(player)
player['fav_food'].append("ramyeon")
print(player['fav_food'])
