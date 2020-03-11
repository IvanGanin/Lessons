import random

class Cards:
    cards_list = ['6♠', '6♥', '6♣', '6♦', '7♠', '7♥', '7♣', '7♦',
                 '8♠', '8♥', '8♣', '8♦', '9♠', '9♥', '9♣', '9♦',
                 '10♠', '10♥', '10♣', '10♦', 'A♠', 'A♥', 'A♣', 'A♦',
                 'B♠', 'B♥', 'B♣', 'B♦', 'C♠', 'C♥', 'C♣', 'C♦',
                 'D♠', 'D♥', 'D♣', 'D♦'] #колода - 36 карт

    # выдаем карты на руки по 6 штук
    def on_hand(self):
        self.hand = []
        while len(self.hand) < 6:
            card = random.choice(self.cards_list)
            self.cards_list.remove(card)
            self.hand.append(card)
        return self.hand

    # ходит игрок
    def player_try(self):
        global card
        print("ход игрока")
        counter = None
        while counter is None:
            card = random.choice(player.hand)
            player.hand.remove(card)
            print(card)
            box = [item for item in computer.hand if card[-1] in item]
            print(box)
            if len(box) == 0:
                computer.hand.append(card)
                print("компьютеру нечем бить, ход игрока")
                print(computer.hand)
                card_add = random.choice(player.cards_list)
                player.cards_list.remove(card_add)
                player.hand.append(card_add)
                print(player.hand)
            else:
                play = []
                for item in box:
                    if len(card) == 3 and len(item) == 3:
                        if card[:2] < item[:2]:
                            computer.hand.remove(item)
                            play.append(item)
                            break
                    elif len(card) == 3 and len(item) == 2:
                        if card[:2] < item[0]:
                            computer.hand.remove(item)
                            play.append(item)
                            break
                    elif len(card) == 2 and len(item) == 3:
                        if card[0] < item[:2]:
                            computer.hand.remove(item)
                            play.append(item)
                            break
                    elif len(card) == 2 and len(item) == 2:
                        if card[0] < item[0]:
                            computer.hand.remove(item)
                            play.append(item)
                            break
                if len(play) != 0:
                    counter = 1
                    print("ваша карта быта, ход компьютера")
                    card_add = random.choice(player.cards_list)
                    player.cards_list.remove(card_add)
                    player.hand.append(card_add)
                    card_add = random.choice(computer.cards_list)
                    computer.cards_list.remove(card_add)
                    computer.hand.append(card_add)
                    print(player.hand, len(player.cards_list))
                    print(computer.hand, len(computer.cards_list))
                else:
                    computer.hand.append(card)
                    print("компьютеру нечем бить, ход игрока")
                    print(computer.hand, len(computer.cards_list))
                    card_add = random.choice(player.cards_list)
                    player.cards_list.remove(card_add)
                    player.hand.append(card_add)
                    print(player.hand, len(player.cards_list))
        return card

        # ход компьютера

    def computer_try(self):
        print("ход компьютера")
        counter = None
        while counter is None:
            card = random.choice(computer.hand)
            computer.hand.remove(card)
            print(card)
            box = [item for item in player.hand if card[-1] in item]
            print(box)
            if len(box) == 0:
                player.hand.append(card)
                print("игроку нечем бить, ход компьютера")
                print(player.hand)
                card_add = random.choice(computer.cards_list)
                computer.cards_list.remove(card_add)
                computer.hand.append(card_add)
                print(computer.hand)
            else:
                play = []
                for item in box:
                    if len(card) == 3 and len(item) == 3:
                        if card[:2] < item[:2]:
                            player.hand.remove(item)
                            play.append(item)
                            break
                    elif len(card) == 3 and len(item) == 2:
                        if card[:2] < item[0]:
                            player.hand.remove(item)
                            play.append(item)
                            break
                    elif len(card) == 2 and len(item) == 3:
                        if card[0] < item[:2]:
                            player.hand.remove(item)
                            play.append(item)
                            break
                    elif len(card) == 2 and len(item) == 2:
                        if card[0] < item[0]:
                            player.hand.remove(item)
                            play.append(item)
                            break
                if len(play) != 0:
                    counter = 1
                    print("ваша карта бита, ход игрока")
                    card_add = random.choice(player.cards_list)
                    player.cards_list.remove(card_add)
                    player.hand.append(card_add)
                    card_add = random.choice(computer.cards_list)
                    computer.cards_list.remove(card_add)
                    computer.hand.append(card_add)
                    print(player.hand, len(player.cards_list))
                    print(computer.hand, len(computer.cards_list))
                else:
                    player.hand.append(card)
                    print("игроку нечем бить, ход компьютера")
                    print(computer.hand, len(computer.cards_list))
                    card_add = random.choice(computer.cards_list)
                    computer.cards_list.remove(card_add)
                    computer.hand.append(card_add)
                    print(player.hand, len(player.cards_list))
            return card


if __name__ == "__main__":
    computer = Cards()
    player = Cards()
    computer.on_hand()
    player.on_hand()
    computer.computer_try()
    player.player_try()