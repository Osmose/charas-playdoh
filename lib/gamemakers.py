from tower import ugettext_lazy as _lazy


GAMEMAKERS = {
    'rm2k': {
        'name': _lazy('RPG Maker 2000'),
    },
    'rm2k3': {
        'name': _lazy('RPG Maker 2003'),
    },
    'rmxp': {
        'name': _lazy('RPG Maker XP'),
    },
    'rmvx': {
        'name': _lazy('RPG Maker VX'),
    },
}


GAMEMAKER_CHOICES = [(key, maker['name']) for key, maker in GAMEMAKERS.items()]
