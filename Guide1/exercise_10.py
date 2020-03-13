
abc = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

var = ""
for i in abc:
    if i == 'a':
        continue
    elif i == 'e':
        continue
    elif i == 'I':
        continue
    elif i == 'o':
        continue
    elif i == 'u':
        continue
    else:
        var = var + i

print(var)