class Error(Exception):
    """Base class for other exception"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class YearOutOfRangeError:
    pass

class MonthOutOfRangeError:
    pass

class DayOutOfRangeError:
    pass

class ValueOutOfRangeError:
    pass