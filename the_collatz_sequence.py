def collatz(number):
    if (number % 2) == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


print('What number do you choose ?')
number = input()
while True:
    number = collatz(int(number))
    if number == 1:
        break
