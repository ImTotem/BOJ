import sys
input = lambda:sys.stdin.readline().strip()

from re import sub

def regex(sentence):
    sentence = sub(r'([a-zA-Z]+)( of Korea)+([ .?!,])', lambda x:'_'*x.group(0).count(" of Korea")+x.group(1)+x.group(3), sentence)
    sentence = sub(r'\bKorea +', '_', sentence)
    sentence = sub(r'\_[a-zA-Z]', lambda x:x.group(0).upper(), sentence)
    return sentence.replace("_", "K-")

def main():
    ans = [input() for _ in range(int(input()))]
    print(*map(regex, ans), sep="\n")

main()