cards = {'Jack': 11, 'Queen': 12,
         'King': 13, 'Ace': 14}

sum_cards = 0

cnt = 0
while cnt < 6:
    card = input()

    sum_cards += int(cards.get(card, card))

    cnt += 1
print(sum_cards / 6)
