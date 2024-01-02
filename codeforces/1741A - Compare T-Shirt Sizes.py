n = int(input())
for _ in range(n):
    test = list(map(str, input().split()))
    if test[0][-1] == test[1][-1]:
        if test[0].count("X") == test[1].count("X"):
            print("=")
        elif test[0][-1] == "L" and test[0].count("X") > test[1].count("X"):
            print(">")
        elif test[0][-1] == "L" and test[0].count("X") < test[1].count("X"):
            print("<")
        elif test[0].count("X") > test[1].count("X"):
            print("<")
        elif test[0].count("X") < test[1].count("X"):
            print(">")
    else:
        if test[0][-1] == "L":
            print(">")
        elif test[1][-1] == "L":
            print("<")
        elif test[0][-1] == "M":
            print(">")
        elif test[1][-1] == "M":
            print("<")
