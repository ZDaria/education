
class DumpDiff:
    """
    Possible values in diff_action field are:
    - CHANGED
    - REMOVED
    - ADDED
    """
    def __init__(self, *row):
        self.market_name = row[0]
        self.instrument = row[1]
        self.diff_action = row[2]
        self.field = row[3]
        self.old_value = row[4]
        self.new_value = row[5]
