# === Stage 11: Группировка ===
# Project: ChessClub
from collections import Counter


def group_players_by_rating(players):
    return Counter(player["rating"] for player in players)


def count_per_rating_group(players):
    grouped = group_players_by_rating(players)
    return dict(sorted(grouped.items()))


if __name__ == "__main__":
    sample = [
        {"name": "Anna", "rating": 1500, "club": "Rook", "joined": "2023-01-15"},
        {"name": "Bob", "rating": 1500, "club": "Bishop", "joined": "2022-06-20"},
        {"name": "Carla", "rating": 1800, "club": "Rook", "joined": "2021-11-03"},
        {"name": "Dan", "rating": 1200, "club": "Queen", "joined": "2024-02-28"},
        {"name": "Eve", "rating": 1800, "club": "King", "joined": "2023-07-19"},
    ]

    result = count_per_rating_group(sample)
    for rating, count in result.items():
        print(f"Рейтинг {rating}: {count} игроков")
