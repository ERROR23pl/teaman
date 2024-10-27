from datetime import datetime


def serialize_datetime(obj):
    """
    Custom serializer for datetime objects.
    Converts datetime objects to ISO 8601 string format for JSON compatibility.
    """
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

def deserialize_datetime(datetime_str):
    """
    Custom deserializer for ISO 8601 formatted strings to datetime objects.
    """
    try:
        return datetime.fromisoformat(datetime_str)
    except ValueError:
        raise ValueError(f"Invalid datetime format: {datetime_str}")