# === Stage 10: Теги ===
# Project: ChessClub
import re
from datetime import date


class PlayerTag:
    """Теги игрока: хранилище, добавление, удаление и поиск."""

    def __init__(self, name):
        self.name = name.strip()
        if not self.name:
            raise ValueError("Тег не может быть пустым")
        self.name = re.sub(r"\s+", " ", self.name).strip()

    @property
    def key(self):
        return self.name.lower()

    def __eq__(self, other):
        return isinstance(other, PlayerTag) and self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"PlayerTag({self.name!r})"


class PlayerTags:
    """Коллекция тегов для одного игрока."""

    def __init__(self):
        self._tags = set()

    def add(self, tag):
        tag = PlayerTag(tag)
        self._tags.add(tag)
        return tag

    def remove(self, tag):
        tag = PlayerTag(tag)
        return self._tags.discard(tag)

    def has(self, tag):
        tag = PlayerTag(tag)
        return tag in self._tags

    def search(self, tag):
        return PlayerTag(tag) in self._tags

    def __contains__(self, tag):
        return self.has(tag)

    def __iter__(self):
        return iter(self._tags)

    def __len__(self):
        return len(self._tags)

    def __repr__(self):
        return f"PlayerTags({sorted(self._tags, key=str)!r})"


def split_tags(text):
    """Разбить строку тегов на отдельные PlayerTag."""
    tags = []
    for part in re.findall(r"[^,\s]+", text):
        if part.startswith("#"):
            part = part[1:]
        tags.append(PlayerTag(part))
    return tags


def merge_tags(*tag_lists):
    """Объединить несколько списков тегов в PlayerTags."""
    merged = PlayerTags()
    for tags in tag_lists:
        for tag in tags:
            merged.add(tag)
    return merged
