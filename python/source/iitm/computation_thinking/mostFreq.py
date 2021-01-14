def mostFreq(marks):
    prev = marks[0]
    mfreq = prev
    count = 1
    max = 1
    for x in marks[1:len(marks)]:
        if x == prev:
            count = count+1
        else:
            if count > max:
                max = count
                mfreq = prev
                count=1
        prev = x
    return mfreq

if __name__ == '__main__':
    marks = [10,10,10,11,11,11,11,11,11,12,12,12,12,12,12,12,12,12,12,13,13,13]
    print(marks[0])
    print(mostFreq(marks))