# === Stage 2: Проверка полей ===
# Project: ChessClub
from datetime import date, datetime

VALID_CLUBS = ["Aurora", "Dragon", "Phoenix", "Knight", "Rook", "Bishop", "Queen", "Castle"]


def normalize_name(value):
    text = value.strip()
    if len(text) < 2:
        raise ValueError("Имя игрока должно содержать не менее двух символов")
    cleaned = "".join(ch for ch in text if ch.isalnum() or ch.isspace())
    return cleaned.title()


def normalize_date(value):
    if isinstance(value, date):
        return value
    if isinstance(value, datetime):
        return value.date()
    text = value.strip()
    for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y", "%m.%d.%Y"):
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            continue
    raise ValueError("Дата вступления должна быть указана в формате ГГГГ-ММ-ДД")


def normalize_rating(value):
    if isinstance(value, int):
        return value
    try:
        return int(float(value))
    except (TypeError, ValueError):
        raise ValueError("Рейтинг должен быть целым числом")


def normalize_club(value):
    text = value.strip().title()
    if text not in VALID_CLUBS:
        raise ValueError(f"Неизвестный клуб. Доступные: {', '.join(VALID_CLUBS)}")
    return text


def validate_player(name, rating, club, join_date):
    errors = []
    clean_name = normalize_name(name)
    if len(clean_name) < 2:
        errors.append("Имя игрока должно содержать не менее двух символов")
    if not errors:
        name = clean_name

    clean_rating = normalize_rating(rating)
    if clean_rating < 0:
        errors.append("Рейтинг не может быть отрицательным")
    if clean_rating > 3200:
        errors.append("Рейтинг не может превышать 3200")
    if not errors:
        rating = clean_rating

    clean_club = normalize_club(club)
    if not errors:
        club = clean_club

    clean_date = normalize_date(join_date)
    if clean_date > date.today():
        errors.append("Дата вступления не может быть в будущем")
    if not errors:
        join_date = clean_date

    if errors:
        raise ValueError("\n".join(errors))

    return name, rating, club, join_date
