'''
LIGHT

Реализовать класс для карточный игры "Игра в дурака" в простейшем виде(без козырей, можно без "добора" карт и т.д.).
Структура класса может быть на Ваше усмотрение.
Можно реализовать следующие методы: инициализация игры (раздача карт себе и компьютеру), ход Ваш, ход компьютера.

PRO

Реализовать класс для карточный игры "Игра в дурака" как можно ближе к правилам (можно реализовать класс на Ваш выбор,
в котором будет представлен пройденный на уроке функционал).

'''
import random


class Deck:
    deck_list = ['6♠', '6♥', '6♣', '6♦', '7♠', '7♥', '7♣', '7♦',
                 '8♠', '8♥', '8♣', '8♦', '9♠', '9♥', '9♣', '9♦',
                 '10♠', '10♥', '10♣', '10♦', 'A♠', 'A♥', 'A♣', 'A♦',
                 'B♠', 'B♥', 'B♣', 'B♦', 'C♠', 'C♥', 'C♣', 'C♦',
                 'D♠', 'D♥', 'D♣', 'D♦']

    # выдаем по 6 карт на руки
    def on_hand(self):
        self.hand = []
        while len(self.hand) < 6:
            card = random.choice(self.deck_list)
            self.deck_list.remove(card)
            self.hand.append(card)
        return self.hand

    # ход игрока
    def player_try(self):
        print("ходит игрок")
        counter = None
        while counter is None:
            card = random.choice(player.hand)
            player.hand.remove(card)
            print(card)
            box = [item for item in computer.hand if card[-1] in item]
            print(box)
            if len(box) == 0:
                computer.hand.append(card)
                print("компьютеру нечем бить1, ходит игрок")
                print(computer.hand)
                card_add = random.choice(player.deck_list)
                player.deck_list.remove(card_add)
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
                    print("ваша карта быта, ходит компьютер")
                    card_add = random.choice(player.deck_list)
                    player.deck_list.remove(card_add)
                    player.hand.append(card_add)
                    card_add = random.choice(computer.deck_list)
                    computer.deck_list.remove(card_add)
                    computer.hand.append(card_add)
                    print(player.hand, len(player.deck_list))
                    print(computer.hand, len(computer.deck_list))
                else:
                    computer.hand.append(card)
                    print("компьютеру нечем бить2, ходит игрок")
                    print(computer.hand, len(computer.deck_list))
                    card_add = random.choice(player.deck_list)
                    player.deck_list.remove(card_add)
                    player.hand.append(card_add)
                    print(player.hand, len(player.deck_list))
        return card

        # ход компьютера

    def computer_try(self):
        print("ходит компьютер")
        counter = None
        while counter is None:
            card = random.choice(computer.hand)
            computer.hand.remove(card)
            print(card)
            box = [item for item in player.hand if card[-1] in item]
            print(box)
            if len(box) == 0:
                player.hand.append(card)
                print("игроку нечем бить1, ходит компьютер")
                print(player.hand)
                card_add = random.choice(computer.deck_list)
                computer.deck_list.remove(card_add)
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
                    print("ваша карта бита, ходит игрок")
                    card_add = random.choice(player.deck_list)
                    player.deck_list.remove(card_add)
                    player.hand.append(card_add)
                    card_add = random.choice(computer.deck_list)
                    computer.deck_list.remove(card_add)
                    computer.hand.append(card_add)
                    print(player.hand, len(player.deck_list))
                    print(computer.hand, len(computer.deck_list))
                else:
                    player.hand.append(card)
                    print("игроку нечем бить, ходит компьютер")
                    print(computer.hand, len(computer.deck_list))
                    card_add = random.choice(computer.deck_list)
                    computer.deck_list.remove(card_add)
                    computer.hand.append(card_add)
                    print(player.hand, len(player.deck_list))
            return card


if __name__ == "__main__":
    player = Deck()
    computer = Deck()
    player.on_hand()
    computer.on_hand()
    player.player_try()
    computer.computer_try()