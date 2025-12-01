dial = 50
ans = 0
file = open("input.txt","r")
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines]

commands = []
for cmd in lines:
    direction = cmd[0]
    number = int(cmd[1:])
    commands.append((direction, number))
    
    if direction == "L":
        dial = (dial - number) % 100
        # dial = dial - number
        # if dial < 0:
        #     dial = (100 - number) + dial
        # elif dial > 0:
        #     dial = dial - number
        # else:
        #     ans += 1
        #     dial = 0
    else:
        dial = (dial + number) % 100
        # dial = dial + number - 100
        # if dial == 0 or dial == 100:
        #     ans += 1
        #     dial = 0
    if dial == 0:
        ans += 1
print(ans)