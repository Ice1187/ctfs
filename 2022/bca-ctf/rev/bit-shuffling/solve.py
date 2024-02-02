f = open("shuffled", "rb").read()
deck = [x for x in bin(int.from_bytes(f, 'big'))[2:]]
deck = ['0']*(8 - (len(deck) % 8)) + deck
order = [0, 1, 1, 0, 0, 0, 1, 0]
order.reverse()
for i in order:
    newdeck = []
    if i == 0:
        for j in range(0, int(len(deck)), 2):
            newdeck.append(deck[j])
        for j in range(1, int(len(deck)), 2):
            newdeck.append(deck[j])
    else:
        for j in range(1, int(len(deck)), 2):
            newdeck.append(deck[j])
        for j in range(0, int(len(deck)), 2):
            newdeck.append(deck[j])
    deck = newdeck

print(int("".join(deck), 2).to_bytes(len(deck)//8, byteorder="big"))
