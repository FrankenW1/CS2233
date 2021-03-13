word = input()
password = ''
ml = []
new = ''
for x in word:
    ml.append(x)
for i in range(len(ml)):
    if ml[i] == 'i':
        ml[i] = '1'
    if ml[i] == 'a':
        ml[i] = '@'
    if ml[i] == 'm':
        ml[i] = 'M'
    if ml[i] == 'B':
        ml[i] = '8'
    if ml[i] == 's':
        ml[i] = '$'
for a in ml:
    new = new + a
new = new + '!'

print(new)



