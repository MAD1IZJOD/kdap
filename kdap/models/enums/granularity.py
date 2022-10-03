from enum import Enum

class Granularity(Enum):
    """Enum for the granularity of the data."""
    DAILY = 'daily'
    MONTHLY = 'monthly'
    YEARLY = 'yearly'