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
        for _ in range(number):
            dial = (dial - 1) % 100
            if dial == 0:
                ans += 1
    else:
        for _ in range(number):
            dial = (dial + 1) % 100
            if dial == 0:
                ans += 1
print(ans)