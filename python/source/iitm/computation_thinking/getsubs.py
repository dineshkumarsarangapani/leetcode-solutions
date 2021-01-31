def first(l):
    if len(l) != 0:
        return l[0]


def last(l):
    if len(l) != 0:
        return l[len(l) - 1]


def init(l):
    if len(l) != 0:
        return l[:-1]


def rest(l):
    if len(l) != 0:
        return l[1:]


def isPresent(l, roll):
    for d in l:
        if d['roll'] == roll:
            return True
    return False


def getSubs(l):
    if len(l) <= 1:
        return l
    firstSub = first(l)
    restSub = rest(l)

    if isPresent(restSub, firstSub['roll']):
        #print("isPresent")
        return getSubs(restSub)
    else:
        #print("no")
        #print(firstSub, restSub)
        a = [firstSub]
        a.extend(getSubs(restSub))
        #print(a)
        return a


if __name__ == '__main__':
    scores = [
        {"roll": 12, "time": "10:20", "score": 80},
        {"roll": 20, "time": "11:23", "score": 70},
        {"roll": 12, "time": "20:40", "score": 90},
        {"roll": 12, "time": "23:50", "score": 95},
        {"roll": 20, "time": "23:53", "score": 65},
    ]
    scores.reverse()
    print(getSubs(scores))
