import math, re
from sys import stdin
input = stdin.readline

while True:
    string = input()[:-1]
    if string == ".":break

    string = re.sub(r"[^\(\)\[\]]", "", string)

    for i in range(string.count("(")+string.count("[")):
        string = string.replace("()", "").replace("[]", "")
    
    print("yes" if string == "" else "no")