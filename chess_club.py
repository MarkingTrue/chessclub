# === Stage 1: Каркас модуля ===
# Project: ChessClub
from dataclasses import dataclass, field
from datetime import date
from typing import List


@dataclass
class Player:
    name: str
    rating: int
    club: str
    joined: date = field(default_factory=date)


def make_demo_players() -> List[Player]:
    return [
        Player("Анна", 1500, "Клуб Дракона", date(2022, 5, 12)),
        Player("Борис", 1680, "Клуб Дракона", date(2021, 9, 3)),
        Player("Виктор", 1420, "Клуб Лиса", date(2023, 1, 20)),
        Player("Галина", 1750, "Клуб Лиса", date(2020, 6, 30)),
    ]


def main() -> None:
    players = make_demo_players()
    print("Добро пожаловать в ChessClub!")
    print(f"Демо-список игроков: {len(players)}")
    for player in players:
        print(f"  {player.name} (рейтинг {player.rating}, "
              f"клуб {player.club}, с {player.joined.isoformat()})")


if __name__ == "__main__":
    main()
