import random
CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["♥", "♦", "♠", "♦︎"]

deck_of_cards = [f"{card}{suit}" for card in CARDS for suit in SUITS]

# Implement a solution for shuffling a deck of cards without using random.shuffle()
# Using randint() is ok
def shuffle_deck(deck_of_cards):
    shuffled_deck = []
    
    # while len(shuffled_deck) < len(deck_of_cards):
    #     index = random.randint(0, len(deck_of_cards)-1)
    #     if not deck_of_cards[index] in shuffled_deck:
    #         shuffled_deck.append(deck_of_cards[index])
    
    copy_of_deck_of_cards = list(deck_of_cards)
    for _ in range(0, len(deck_of_cards)):
        index = random.randint(0, len(copy_of_deck_of_cards)-1)
        shuffled_deck.append(copy_of_deck_of_cards[index])
        copy_of_deck_of_cards.pop(index)


    return shuffled_deck



shuffled_deck = shuffle_deck(deck_of_cards)
print(shuffled_deck)
print(len(shuffled_deck))
