player = {
    'name': 'Ryu',
    'age': 22,
    'alive': True,
    'fav_food': ["pizza", "korean"],
    'disappear': 'soon',
    'best_song': ("Best of me", "Male fantasy", "Light switch"),
    'friend': {
        'name': 'Shin',
        'age': 21,
        'fav_food': ["pasta"],
        'best_song': ("Save our lives", "Utopia", "Hijo dela luna"),

    }
}
# Player Update
player['best_song'] = ["Microkosmos", "Make it right"]
print(player)
# Player Update 2
player.pop('disappear')
# Player Update 3
player['friend']['fav_food'].append("creamy stuff")
print(player)
