def exact_change(tot):
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


if __name__ == '__main__':

    inp = int(input())
    nd, nq, ndi, nn, np = exact_change(inp)

    if inp <= 0:
        print('no change')
    else:
        if nd > 1:
            print('%d dollars' % nd)
        elif nd == 1:
            print('%d dollar' % nd)
        if nq > 1:
            print('%d quarters' % nq)
        elif nq == 1:
            print('%d quarter' % nq)

        if ndi > 1:
            print('%d dimes' % ndi)
        elif ndi == 1:
            print('%d dime' % ndi)

        if nn > 1:
            print('%d nickels' % nn)
        elif nn == 1:
            print('%d nickel' % nn)

        if np > 1:
            print('%d pennies' % np)
        elif np == 1:
            print('%d penny' % np)
