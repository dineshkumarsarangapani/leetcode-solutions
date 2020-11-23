from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return 'Player(name=%s, score=%s)' % (self.name, self.score)

    # function returns  if ,  if , and  if .
    def comparator(a, b):
        if a.score > b.score:
            return -1
        if a.score < b.score:
            return 1
        if a.score == b.score:
            if a.name > b.name:
                return 1
            if a.name < b.name:
                return -1
            if a.name == b.name:
                return 0

    pass


n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)