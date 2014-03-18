# Week6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
player = 0
dealer = 0
deck = 0
# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos,):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.card_list = []	

    def __str__(self):
        # return a string representation of a hand
        s = "Hand contains"
        for i in self.card_list:
            s += " " + str(i)
        return s

    def add_card(self, card):
        # add a card object to a hand
        self.card_list.append(card)
        
    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        Ace_is_exist = False
        value = 0
        for i in self.card_list:
            if i.get_rank() == 'A':
                Ace_is_exist = True
            value += VALUES[i.get_rank()]
            
        if Ace_is_exist and (value + 10 <= 21):
            value += 10
        
        return value
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        global in_play
        offset = 75
        count = 0
        for i in self.card_list:
            i.draw(canvas,(pos[0] + offset * count,pos[1]))
            count += 1
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.card_list = [Card(suit,rank) for suit in SUITS for rank in RANKS]
   
    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.card_list)    # use random.shuffle()

    def deal_card(self):
        # deal a card object from the deck
        return self.card_list.pop(len(self.card_list)-1)
    
    def __str__(self):
        # return a string representing the deck
        s = "Deck contains"
        for i in self.card_list:
            s += " " + str(i)
        return s

#define event handlers for buttons
def deal():
    global outcome, in_play, player, dealer, deck
    outcome = ""
    player = Hand()
    dealer = Hand()
    deck = Deck()
    deck.shuffle()
    deck.shuffle()
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    in_play = True
    # print player
    # print dealer
    # print deck
def hit():
    global player, deck, outcome, score,in_play
    # if the hand is in play, hit the player
    if in_play:
        player.add_card(deck.deal_card())
    else:
        return
    # if busted, assign a message to outcome, update in_play and score
    if player.get_value() > 21:
        outcome = "You have busted"
        in_play = False
        score -= 1
        
def stand():
    global dealer, deck, outcome,in_play,score
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
    else:
        return
    # assign a message to outcome, update in_play and score
    if dealer.get_value() < player.get_value() or dealer.get_value() > 21:
        score += 1
        outcome = "You win!"
    else:
        score -= 1
        outcome = "The dealer win!"
    in_play = False
    
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global outcome
    # canvas.draw_text(str(dealer.get_value()), (80, 500), 40, 'Black')
    # canvas.draw_text(str(player.get_value()), (80, 550), 40, 'Black')
    canvas.draw_text('Blackjack', (50, 80), 50, '#31FBC9')
    canvas.draw_text('Score '+str(score), (350, 80), 50, 'Black')
    canvas.draw_text('Dealer', (50, 130), 40, 'Black')
    canvas.draw_text(str(player.get_value())+" points", (50, 500), 40, 'White')
    canvas.draw_text(outcome, (280, 130), 40, 'Black')
    if in_play:
        canvas.draw_text('Player     Hit or stand?', (50, 350), 40, 'Black')
    else:
        canvas.draw_text('Player     New deal?', (50, 350), 40, 'Black')
        canvas.draw_text(str(dealer.get_value())+" points", (50, 280), 40, 'White')
    dealer.draw(canvas,(50,150))
    player.draw(canvas,(50,370))
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [50 + CARD_BACK_CENTER[0], 150 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric