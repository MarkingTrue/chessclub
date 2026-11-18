# === Stage 7: Связи между сущностями ===
# Project: ChessClub
from datetime import date


class Player:
    def __init__(self, name, rating, club, join_date=None):
        self.name = name
        self.rating = rating
        self.club = club
        self.join_date = join_date or date.today()


class Game:
    def __init__(self, player, opponent, result, date):
        self.player = player
        self.opponent = opponent
        self.result = result
        self.date = date

    def player_exists(self):
        return self.player is not None

    def opponent_exists(self):
        return self.opponent is not None


def get_games(player, games):
    return [game for game in games if game.player is player]


def validate_game(player, game):
    if not game.player_exists():
        raise ValueError("Партия не имеет игрока")
    if not game.opponent_exists():
        raise ValueError("Партия не имеет соперника")
    if game.player is None:
        raise ValueError("Соперник не связан с игрой")
    if game.opponent is None:
        raise ValueError("Игрок не связан с игрой")


def main():
    alice = Player("Alice", 1500, "Club A")
    bob = Player("Bob", 1600, "Club B")
    carol = Player("Carol", 1700, "Club A")

    g1 = Game(alice, bob, "1-0", date(2024, 1, 1))
    g2 = Game(alice, carol, "0-1", date(2024, 2, 1))
    g3 = Game(bob, carol, "1-0", date(2024, 3, 1))

    games = [g1, g2, g3]

    alice_games = get_games(alice, games)
    print("Партии Alicе:", len(alice_games))

    for game in alice_games:
        validate_game(alice, game)
        print(game.player.name, "против", game.opponent.name)


if __name__ == "__main__":
    main()
