N = input()                                  # n = "26"
number = N
count = 0

while True:
    if len(number) == 1:
        number = "0" + number
        print(number)

    plus = str(int(number[0]) + int(number[1]))       # 2 + 6 = "8"
    number = number[-1] + plus[-1]                    # 6 + 8 = "68"

    count += 1

    if number == N:
        print(count)
        break