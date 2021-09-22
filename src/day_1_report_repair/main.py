# The Advent of code 😊


# DAY 1

def report_repair(data: list) -> int:
    """
    find two numbers (say a, b) from the data provided that sum up to 2020
     and return their product( i.e a*b)

    :param data: list of numbers
    :return: product of two terms (i.e a*b) or 0 if we can't find any (a,b: a+b=2020)
    """
    try:
        for i in range(len(data)):
            for j in range(i+1, len(data)):
                if data[i] + data[j] == 2020:
                    return data[i] * data[j]

    except TypeError:
        print("Error: expected data to be of type list[int]")

    return 0


# Part Two

def report_repair_three_numbers(data):
    """
    find three numbers (say a, b, c) from the data provided that sum up to 2020
     and return their product( i.e a*b*c)

    :param data: list of numbers
    :return: product of three terms (i.e a*b*c) or 0 if we can't find any (a,b,c: a+b+c=2020)
    :raises: TypeError: when data is not of type list[int]
    """
    try:
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                for k in range(j + 1, len(data)):

                    if data[i] + data[j] + data[k] == 2020:
                        return data[i] * data[j] * data[k]

    except TypeError as e:
        raise TypeError("expected input param - data: list[int]") from e

    return 0


if __name__ == '__main__':
    with open("../../resources/day1_input_data") as f:
        # read data and cast to integers
        testData = list(map(int, f.readlines()))

        print("report_repair(testData) ->",report_repair(testData))

        print("report_repair_three_numbers(testData) ->", report_repair_three_numbers(testData))
