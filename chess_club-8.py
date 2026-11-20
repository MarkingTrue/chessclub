# === Stage 8: Сортировка записей ===
# Project: ChessClub
def sort_players_by_name(players):
    """Сортировка игроков по имени (возрастание / убывание)."""
    return sorted(players, key=lambda p: p["name"], reverse=False)


def sort_players_by_name_desc(players):
    """Сортировка игроков по имени (убывание)."""
    return sorted(players, key=lambda p: p["name"], reverse=True)


def sort_players_by_date(players):
    """Сортировка игроков по дате вступления (возрастание / убывание)."""
    return sorted(players, key=lambda p: p["join_date"], reverse=False)


def sort_players_by_date_desc(players):
    """Сортировка игроков по дате вступления (убывание)."""
    return sorted(players, key=lambda p: p["join_date"], reverse=True)


if __name__ == "__main__":
    sample = [
        {"name": "Иванов", "join_date": "2023-05-01"},
        {"name": "Смирнова", "join_date": "2022-11-15"},
        {"name": "Петров", "join_date": "2023-01-10"},
    ]

    print("По имени (взр):")
    for p in sort_players_by_name(sample):
        print(p["name"], p["join_date"])

    print("По имени (уб):")
    for p in sort_players_by_name_desc(sample):
        print(p["name"], p["join_date"])

    print("По дате (взр):")
    for p in sort_players_by_date(sample):
        print(p["name"], p["join_date"])

    print("По дате (уб):")
    for p in sort_players_by_date_desc(sample):
        print(p["name"], p["join_date"])
