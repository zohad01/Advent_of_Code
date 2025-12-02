file = open("input3.txt","r")
lines = file.readlines()
file.close()

lines = [line.split(",") for line in lines]
# lines = lines.split(",")
lines = lines[0]
# print(len(lines))
# print(lines)
total = 0
for r in lines:
    start, end = r.split("-")
    start = int(start)
    end = int(end)

    for line in range(start, end+1):
        s = str(line)
        if len(s) % 2 == 0:
            half = len(s) // 2
            if s[:half] == s[half:]:
                total += line

print(total)