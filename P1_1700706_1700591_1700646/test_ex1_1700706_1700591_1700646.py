# Gustavo Zaik - 1700591
# Luka Gabriel - 1700709
# Jhonatan Rafael - 1700646

from ex1_1700706_1700591_1700646 import contagem
texto1 = 'o doce perguntou pro doce qual é o doce mais doce que o doce de batata-doce o doce respondeu pro doce que o doce mais doce que o doce de batata-doce é o doce de doce de batata-doce'
texto2 = 'olha o sapo dentro do saco o saco com o sapo dentro o sapo batendo papo e o papo soltando o vento'
texto3 = 'a aranha arranha a rã a rã arranha a aranha nem a aranha arranha a rã nem a rã arranha a aranha'

def test_ex1():
    assert contagem(texto1) == {'pro':2,'que':3,'batata-doce':3,'de':4,'o':7,'qual':1,'mais':2,'é':2,'doce':12,'perguntou':1,'respondeu':1}
    assert contagem(texto2) == {'e': 1, 'soltando': 1, 'dentro': 2, 'sapo': 3, 'do': 1, 'vento': 1, 'olha': 1, 'saco': 2, 'com': 1, 'batendo': 1, 'o': 6, 'papo': 2}
    assert contagem(texto3) == {'arranha': 4, 'a': 8, 'rã': 4, 'nem': 2, 'aranha': 4}