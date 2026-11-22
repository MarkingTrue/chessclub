# === Stage 9: Поиск по нескольким словам ===
# Project: ChessClub
from datetime import date


class Player:
    def __init__(self, name, rating, club, joined):
        self.name = name
        self.rating = rating
        self.club = club
        self.joined = joined


class SearchQuery:
    def __init__(self, terms):
        self.positive = [t for t in terms if t and not t.startswith("-")]
        self.negations = [t[1:] for t in terms if t and t.startswith("-")]


def _tokenize(value):
    return [t.lower() for t in value.replace(",", " ").split()]


def _matches(value, tokens):
    if not tokens:
        return True
    return all(token in _tokenize(value) for token in tokens)


def _matches_all(value, tokens):
    if not tokens:
        return True
    return any(token in _tokenize(value) for token in tokens)


def search_players(players, query=None):
    if query is None:
        query = SearchQuery([])

    results = []
    for player in players:
        if _matches_all(player.name, query.positive):
            if _matches_all(player.club, query.positive):
                if _matches(player.rating, query.positive):
                    if _matches_all(player.joined, query.positive):
                        if not _matches_any(player.name, query.negations):
                            if not _matches_any(player.club, query.negations):
                                if not _matches(player.rating, query.negations):
                                    if not _matches_any(player.joined, query.negations):
                                        results.append(player)

    return results


if __name__ == "__main__":
    members = [
        Player("Анна Иванова", 1500, "Москва", date(2020, 1, 15)),
        Player("Борис Смирнов", 1850, "Санкт-Петербург", date(2019, 6, 3)),
        Player("Виктор Орлов", 1200, "Екатеринбург", date(2021, 11, 20)),
        Player("Дарья Кузнецова", 1650, "Москва", date(2018, 3, 10)),
    ]

    found = search_players(members, ["Москва", "1500"])
    print("Найдено по Москве и 1500:", len(found))

    excluded = search_players(members, ["Санкт-Петербург", "-Санкт-Петербург"])
    print("После исключения:", len(excluded))

    only = search_players(members, ["Иванов", "-Санкт-Петербург"])
    print("Только Иванов, не СПб:", [p.name for p in only])

    simple = search_players(members, ["1800"])
    print("По рейтингу 1800:", [p.name for p in simple])
