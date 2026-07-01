TEXT_COLUMN_ALIASES = (
    "tweet",
    "text",
    "full_text",
    "content",
    "body",
    "message",
)


def detect_text_column(columns):
    normalized_columns = {str(column).strip().lower(): column for column in columns}

    for alias in TEXT_COLUMN_ALIASES:
        if alias in normalized_columns:
            return normalized_columns[alias]

    return None
