# === Stage 5: Удаление и восстановление ===
# Project: ChessClub
from datetime import datetime
from typing import Optional


class Player:
    def __init__(self, name: str, rating: int, club: str, join_date: str):
        self.id = None
        self.name = name
        self.rating = rating
        self.club = club
        self.join_date = join_date
        self.is_deleted = False

    def __repr__(self):
        status = "активен" if not self.is_deleted else "удалён"
        return f"<Player {self.name} ({status})>"


class SoftDeleter:
    def __init__(self, players: list):
        self.players = players

    def delete(self, player_id: int) -> Optional[Player]:
        for player in self.players:
            if player.id == player_id:
                player.is_deleted = True
                return player
        return None

    def restore(self, player_id: int) -> Optional[Player]:
        for player in self.players:
            if player.id == player_id and player.is_deleted:
                player.is_deleted = False
                return player
        return None

    def get_active(self) -> list:
        return [p for p in self.players if not p.is_deleted]

    def get_deleted(self) -> list:
        return [p for p in self.players if p.is_deleted]

    def delete_by_name(self, name: str) -> Optional[Player]:
        for player in self.players:
            if player.name == name:
                player.is_deleted = True
                return player
        return None

    def restore_all(self) -> int:
        count = 0
        for player in self.players:
            if player.is_deleted:
                player.is_deleted = False
                count += 1
        return count


class PlayerStore:
    def __init__(self):
        self._players = []
        self._counter = 0

    def add(self, name: str, rating: int, club: str, join_date: str) -> Player:
        player = Player(name, rating, club, join_date)
        self._counter += 1
        player.id = self._counter
        self._players.append(player)
        return player

    def get(self, player_id: int) -> Optional[Player]:
        for player in self._players:
            if player.id == player_id and not player.is_deleted:
                return player
        return None

    def delete(self, player_id: int) -> bool:
        target = self.get(player_id)
        if target:
            target.is_deleted = True
            return True
        return False

    def restore(self, player_id: int) -> bool:
        target = self.get(player_id)
        if target and target.is_deleted:
            target.is_deleted = False
            return True
        return False

    def list_active(self) -> list:
        return [p for p in self._players if not p.is_deleted]

    def list_deleted(self) -> list:
        return [p for p in self._players if p.is_deleted]

    def count_active(self) -> int:
        return len(self.list_active())
