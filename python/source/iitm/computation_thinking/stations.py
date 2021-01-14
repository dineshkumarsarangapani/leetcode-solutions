def stations(stats):
    z = {}
    for a in stats.keys():
        c = 0
        y = 0
        d = stats[a]
        for b in d.keys():
            if y == d[b]:
                c = c + 1
            print(d[b])
            if y < d[b]:
                c = 1
                y = d[b]
            if c not in z.keys():
                z[c] = 0
            z[c] = z[c] + 1

    print(z)


if __name__ == '__main__':
    stats = {"chennai": {"m": 0, "t":0, "w":0, "th":0, "f":0, "s":0, "sun":0},
             "mumbai": {"m": 0, "t":3, "w":3, "th":14, "f":15, "s":63, "sun":0}}
    stations(stats)