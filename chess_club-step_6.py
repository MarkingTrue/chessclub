# === Stage 6: Связанная сущность ===
# Project: ChessClub
from datetime import date


class Party:
    def __init__(self, player_id, player_name, result):
        self.player_id = player_id
        self.player_name = player_name
        self.result = result
        self.date = date.today()

    def __repr__(self):
        return f"Party(player_id={self.player_id}, result={self.result}, date={self.date})"


class PartyManager:
    def __init__(self):
        self.parties = []
        self.id_counter = 1

    def add_party(self, player_id, player_name, result):
        party = Party(player_id, player_name, result)
        party.id = self.id_counter
        self.id_counter += 1
        self.parties.append(party)
        return party

    def get_party(self, party_id):
        for party in self.parties:
            if party.id == party_id:
                return party
        return None

    def list_parties(self):
        return list(self.parties)


def demonstrate_party_creation():
    manager = PartyManager()

    white_result = manager.add_party(
        player_id=1,
        player_name="Алексей Иванов",
        result="1-0",
    )
    black_result = manager.add_party(
        player_id=2,
        player_name="Мария Петрова",
        result="0-1",
    )

    print("Добавлена партия:")
    print(white_result)

    print("Добавлена партия:")
    print(black_result)

    print("Все партии:")
    for party in manager.list_parties():
        print(f"  #{party.id}: {party.player_name} ({party.player_id}) -> {party.result}, {party.date}")

    found = manager.get_party(white_result.id)
    print("Поиск партии по id:")
    print(found)


if __name__ == "__main__":
    demonstrate_party_creation()
