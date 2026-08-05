def daily_temperatures(temperatures):
    """
    Given a list of daily temperatures, return a list such that, for each day in the input,
    tells you how many days you would have to wait until a warmer temperature. If there is no
    future day for which this is possible, put 0 instead.

    :param temperatures: List[int] - A list of daily temperatures.
    :return: List[int] - A list indicating the number of days to wait for a warmer temperature.
    """
    n = len(temperatures)
    result = [0] * n
    stack = []


    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            index = stack.pop()
            result[index] = i - index
        stack.append(i)
    return result

if __name__ == '__main__':
    print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    print(daily_temperatures([30, 40, 50, 60]))
    print(daily_temperatures([30, 60, 90]))
    print(daily_temperatures([70, 70, 70]))
    print(daily_temperatures([80, 70, 60, 50]))
    print(daily_temperatures([75, 71, 69, 72]))
    print(daily_temperatures([60, 59, 58, 62]))
    print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
