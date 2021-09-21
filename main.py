# The Advent of code 😊


# DAY 1

def report_repair(data: list) -> int:
    """
    find two numbers (say a, b) from the data provided that sum up to 2020
     and return their product( i.e a*b)

    :param data: list of numbers
    :return: product of two terms (i.e a*b) or 0 if we can't find any (a,b: a+b=2020)
    """
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i] + data[j] == 2020:
                return data[i] * data[j]

    return 0


# Part Two

def report_repair_three_numbers(data):
    """
    find three numbers (say a, b, c) from the data provided that sum up to 2020
     and return their product( i.e a*b*c)

    :param data: list of numbers
    :return: product of three terms (i.e a*b*c) or 0 if we can't find any (a,b,c: a+b+c=2020)
    """
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            for k in range(j + 1, len(data)):

                if data[i] + data[j] + data[k] == 2020:
                    return data[i] * data[j] * data[k]

    return 0


if __name__ == '__main__':
    pass
