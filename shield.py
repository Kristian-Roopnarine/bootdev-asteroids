class Shield:
    def __init__(self):
        self.type = "shield"
        self.buff_display_name = "S"
        self.default_val = 3
        self.width = 0
        self.color = "yellow"

    def modify_stats(self, val=None):
        if val is None:
            return self.default_val
        return val
