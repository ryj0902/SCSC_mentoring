def digit(number):
    count = 0
    while number != 0:
        number = int(number / 10)
        count = count + 1
    return count

def hard(number):
    time = 0
    n = digit(number)

    while n != 0:
        unit = number % 10

        if unit % 3 == 0 and  unit != 0:
            time = time + 1

        number = int(number / 10)
        n = n - 1

    return time

	
print 'Input range(1 - 5000) : '

number = 1
Maximum = input()
time = 0
while number <= Maximum:
    time = hard(number)

    if time == 0:
        print number
    else:
        print 'Clap!' * time

    number = number + 1