import random

suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
cardFaces = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

def pickACard():
    cardFace = random.choice(cardFaces)
    cardSuit = random.choice(suits)
    return str(cardFace) + " of " + cardSuit

hand = []
for i in range(5):
    card = pickACard()
    hand.append(card)

print(hand)
