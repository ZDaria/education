
class DumpDiff:
    """
    This class provides info about diff.
    Market name - in some cases we can load not one particular market,
        but all markets. As well as validation can be applied to one specific
        market.
    Instrument - were the diff was wound.
    Diff action - possible values in diff_action field are:
        - CHANGED
        - REMOVED
        - ADDED
    Field - applicable only for CHANGED diff action.
        Describes field where change was found.
    Old and new value - the same as field are applicable only to
        CHANGED diff action.
    """
    def __init__(self, *row):
        self.market_name = row[0]
        self.instrument = row[1]
        self.diff_action = row[2]
        self.field = row[3]
        self.old_value = row[4]
        self.new_value = row[5]
