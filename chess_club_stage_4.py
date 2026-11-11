# === Stage 4: Редактирование записей ===
# Project: ChessClub
from datetime import date


ALLOWED_PLAYER_FIELDS = ("name", "rating", "club", "joined_date")


class PlayerEditError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


def validate_update_fields(player, fields):
    errors = []
    if not isinstance(fields, (list, tuple, set)):
        errors.append("fields должен быть списком, кортежем или множеством")
    unknown = set(fields) - ALLOWED_PLAYER_FIELDS
    if unknown:
        errors.append(f"Недопустимые поля: {sorted(unknown)}")
    if not errors:
        return fields
    raise PlayerEditError("; ".join(errors))


def validate_new_value(player, field, value):
    errors = []
    if field == "name":
        if not isinstance(value, str) or not value.strip():
            errors.append("name должен быть непустой строкой")
    elif field == "rating":
        if not isinstance(value, int) or value < 0:
            errors.append("rating должен быть неотрицательным целым числом")
    elif field == "club":
        if not isinstance(value, str) or not value.strip():
            errors.append("club должен быть непустой строкой")
    elif field == "joined_date":
        if not isinstance(value, date):
            errors.append("joined_date должен быть объектом типа date")
    return errors


def edit_player(player, fields, values):
    if not isinstance(player, dict):
        raise PlayerEditError("игрок должен быть словарём")
    if player.get("id") is None:
        raise PlayerEditError("у игрока отсутствует идентификатор")

    fields = validate_update_fields(player, fields)
    if not isinstance(values, dict):
        raise PlayerEditError("values должен быть словарём")

    updated_values = {}
    for field in fields:
        if field not in values:
            raise PlayerEditError(f"отсутствует новое значение для поля {field}")
        new_value = values[field]
        value_errors = validate_new_value(player, field, new_value)
        if value_errors:
            raise PlayerEditError(f"поле {field}: " + "; ".join(value_errors))
        updated_values[field] = new_value

    for field, new_value in updated_values.items():
        player[field] = new_value

    return player
