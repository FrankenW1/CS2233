def change(tot):
    nd = tot // 100
    tot %= 100
    nq = tot // 25
    tot %= 25
    ndi = tot // 10
    tot %= 10
    nn = tot // 5
    tot %= 5
    np = tot
    return nd, nq, ndi, nn, np




inp = int(input())
nd, nq, ndi, nn, np = change(inp)

if inp <= 0:
    print('no change')
else:
    if nd > 1:
        print('%d Dollars' % nd)
    elif nd == 1:
        print('%d Dollar' % nd)

    if nq > 1:
        print('%d Quarters' % nq)
    elif nq == 1:
        print('%d Quarter' % nq)

    if ndi > 1:
        print('%d Dimes' % ndi)
    elif ndi == 1:
        print('%d Dime' % ndi)

    if nn > 1:
        print('%d Nickels' % nn)
    elif nn == 1:
        print('%d Nickel' % nn)

    if np > 1:
        print('%d Pennies' % np)
    elif np == 1:
        print('%d Penny' % np)
