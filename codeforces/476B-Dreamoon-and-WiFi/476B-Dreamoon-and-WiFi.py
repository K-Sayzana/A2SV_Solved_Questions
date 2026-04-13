from itertools import count


s1 = input()
s2 = input()


def solve(i, s, pos, res):
    if i == len(s):
        res.append(pos)
        return

    if s[i] == "+":
        solve(i + 1, s, pos + 1, res)
    elif s[i] == "-":
        solve(i + 1, s, pos - 1, res)
    else:
        solve(i + 1, s, pos + 1, res)
        solve(i + 1, s, pos - 1, res)


res1 = []
solve(0, s1, 0, res1)
res2 = []
solve(0, s2, 0, res2)

print(res2.count(res1[0]) / len(res2))