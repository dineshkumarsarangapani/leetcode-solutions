def calculate(a, b):
    #print("called")
    if a < b:
        return calculate(b, a)
    if a == b:
        return b
    diff = a - b
    if diff > b:
            return calculate(diff, b)
    else:
        return calculate(b, diff)


if __name__ == '__main__':
    print(calculate(14, 17))
    print(calculate(17, 14))
    # HCF function
