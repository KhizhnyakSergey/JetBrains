A = int(input())
B = int(input())
H = int(input())

if A <= B:
    if H >= A and <= B:
        print("Normal")
    if H < A:
        print("Deficiency")
    if H > B:
        print("Excess")
