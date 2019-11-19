# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.

seznam = [1, 2, 3, 4, 5, 10]

seznam2 = ["strgjkfd", 1, 1.3, [], True]

print(seznam)

seznam.append(12)
print(seznam)

print(seznam.count(4))
a = seznam.pop()
print(a)
print(seznam)

b = seznam.pop(1)
print(seznam)

t = [4, 5, 7, 8, 1, 4, 9, 10, -1]
t.sort()
print(t)

t.sort(reverse=True)
print(t)

for el in t:
    print(el*4)

