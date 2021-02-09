start_atom = int(input())
finish_atom = int(input())
count = 0
while finish_atom < start_atom:
    start_atom = start_atom / 2
    count += 1
    if start_atom == finish_atom:
        count = count + 1
print(count * 12)
