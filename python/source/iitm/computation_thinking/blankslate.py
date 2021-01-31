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


def numeric(outcomes):
    if len(outcomes) == 0:
        return 0
    if first(outcomes) == "won":
        return numeric(rest(outcomes)) + 1
    else:
        return numeric(rest(outcomes)) - 1
    pass


def blankSlate(outcomes):
    if numeric(outcomes) == 0:
        return True
    return False


if __name__ == '__main__':
    outcomes = ["won", "lost", "won", "lost", "won"]
    print(blankSlate(outcomes))