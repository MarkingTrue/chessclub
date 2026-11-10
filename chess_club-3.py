# === Stage 3: Хранилище в памяти ===
# Project: ChessClub
InMemoryPlayerStore

from datetime import date
from typing import Dict, List, Optional

class Player:
    def __init__(self, player_id: str, name: str, rating: int, club: str, join_date: date):
        self.id = player_id
        self.name = name
        self.rating = rating
        self.club = club
        self.join_date = join_date

class InMemoryPlayerStore:
    def __init__(self):
        self._players: Dict[str, Player] = {}

    def add(self, player: Player) -> None:
        if player.id in self._players:
            raise ValueError(f"Player with id {player.id} already exists")
        self._players[player.id] = player

    def get(self, player_id: str) -> Optional[Player]:
        return self._players.get(player_id)

    def list_all(self) -> List[Player]:
        return list(self._players.values())

    def __len__(self) -> int:
        return len(self._players)


def main():
    store = InMemoryPlayerStore()

    alice = Player("p1", "Alice", 1500, "Rookie", date(2024, 1, 15))
    bob = Player("p2", "Bob", 1600, "Rookie", date(2024, 2, 20))
    carol = Player("p3", "Carol", 1700, "Rookie", date(2024, 3, 25))

    store.add(alice)
    store.add(bob)
    store.add(carol)

    print(f"Store has {len(store)} players")

    print("All players:")
    for player in store.list_all():
        print(f"  {player.id}: {player.name} (rating {player.rating})")

    target = store.get("p2")
    if target:
        print(f"Found player: {target.name}")
    else:
        print("Target player not found")

    missing = store.get("p99")
    if missing:
        print(f"Unexpected: {missing.name}")
    else:
        print("Missing player correctly returned None")


if __name__ == "__main__":
    main()
