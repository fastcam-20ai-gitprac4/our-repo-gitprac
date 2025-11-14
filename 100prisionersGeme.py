import random
#A
def main():
    NUM_DRAWERS = 10
    NUM_REPETITIONS = int(1E5)

    print('{:15}: {:5} ({})'.format('approach', 'wins', 'ratio'))
    for approach in PrisionersGame.approaches:
        num_victories = 0
        for _ in range(NUM_REPETITIONS):
            game = PrisionersGame(NUM_DRAWERS)
            num_victories += PrisionersGame.victory(game.play(approach))

        print('{:15}: {:5} ({:.2%})'.format(
            approach.__name__, num_victories, num_victories / NUM_REPETITIONS))
#B
class PrisionersGame:
    """docstring for PrisionersGame"""
    def __init__(self, num_drawers):
        # 100개가 짝수인지 확인 (assert는 그대로 둬도 됨)
        assert num_drawers % 2 == 0
        self.num_drawers = num_drawers
        self.max_attempts = int(self.num_drawers / 2)
        self.drawer_ids = list(range(1, num_drawers + 1))
        shuffled = self.drawer_ids[:]
        random.shuffle(shuffled)
        self.drawers = dict(zip(self.drawer_ids, shuffled))
    def play_naive(self, player_number):
        """ Randomly open drawers """
        for attempt in range(self.max_attempts):
            if self.drawers[random.choice(self.drawer_ids)] == player_number:
                return True

        return False

    def play_naive_mem(self, player_number):
        """ Randomly open drawers but avoiding repetitions """
        not_attemped = self.drawer_ids[:]
        for attempt in range(self.max_attempts):
            guess = random.choice(not_attemped)
            not_attemped.remove(guess)

            if self.drawers[guess] == player_number:
                return True

        return False
#C
if __name__ == '__main__':
    main()
