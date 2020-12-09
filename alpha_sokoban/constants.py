#mapping of moves to change in index:
MOVES = {'u': (-1,0),
         'd': (1,0),
         'l': (0,-1),
         'r': (0,1)}

#mapping of integers to tile types:
TILE_TYPES = {0: 'open_space',
              1: 'wall',
              2: 'box',
              3: 'storage',
              4: 'player',
              5: 'box_on_storage',
              6: 'player_on_storage'}

INVALID_TILE = -1

#mapping of tiles integers to symbols:
TILE_SYMBOLS = {0: ' ',
                1: '#',
                2: '$',
                3: '.',
                4: '@',
                5: '*',
                6: '+'}

INVALLID_TILE_SYMBOL = "!"
