n = int(raw_input())
string = raw_input()

print n - 2*min(string.count('0'), string.count('1'))