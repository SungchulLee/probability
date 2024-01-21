import matplotlib.pyplot as plt
import random

from download import download_poker_card_images

class Poker:
    def __init__(self, num_players=2):
        self.num_players = num_players
        self.numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
        self.shapes = ['s', 'd', 'h', 'c'] # 무늬: 스페이드, 다이아몬드, 하트, 클로버
        self.cards = [number + shape for number in self.numbers for shape in self.shapes]
    def run(self):
        self.chosen_cards = random.sample(self.cards, 5*self.num_players)
    def display_cards(self):
        self.run()
        _, axes = plt.subplots(self.num_players, 5, figsize=(5,self.num_players*1.5), squeeze=False)
        for i in range(self.num_players):
            for j, five_card in enumerate(self.chosen_cards[i*5:(i+1)*5]):
                img = plt.imread(f'BlackJackPython/DECK/{five_card}.gif')
                axes[i,j].imshow(img)
                axes[i,j].set_xticks([])
                axes[i,j].set_yticks([])
        plt.tight_layout
        plt.show()


def main():
    download_poker_card_images()

    obj = Poker()
    obj.display_cards()

if __name__ == "__main__":
    main()
