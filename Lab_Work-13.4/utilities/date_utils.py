from datetime import datetime

def days_between(date_str1, date_str2, date_format="%Y-%m-%d"):
    """Calculates the absolute number of days between two date strings (YYYY-MM-DD)."""
    d1 = datetime.strptime(date_str1, date_format)
    d2 = datetime.strptime(date_str2, date_format)
    return abs((d2 - d1).days)
