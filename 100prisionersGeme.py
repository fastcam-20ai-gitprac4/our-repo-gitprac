import random

def main():
    pass

class PrisionersGame:
    """docstring for PrisionersGame"""
    def __init__(self, num_drawers):
        pass

    def play_optimum(self, player_number):
        """ Open the drawer that matches the player number and then open the drawer
        with the revealed number.
        """
        prev_attempt = player_number
        for attempt in range(self.max_attempts):
            if self.drawers[prev_attempt] == player_number:
                return True
            else:
                prev_attempt = self.drawers[prev_attempt]

        return False

    @classmethod
    def victory(csl, results):
        """Defines a victory of a game: all players won"""
        return all(results)

    approaches = [play_naive, play_naive_mem, play_optimum]

    def play(self, approach):
        """Plays this game and returns a list of booleans with
        True if a player one, False otherwise"""
        return [approach(self, player) for player in self.drawer_ids]

if __name__ == '__main__':
    main()