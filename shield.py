class Shield:
    can_spawn = True
    max_spawn = 2
    current_spawn = 0

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

    def update_spawn_stuff(self):
        pass

    def inc_current_spawn(self, val):
        Shield.current_spawn += val
        if Shield.current_spawn >= Shield.max_spawn:
            self.update_can_spawn(False)
        else:
            self.update_can_spawn(True)

    def update_can_spawn(self, val):
        Shield.can_spawn = val

    def is_spawnable():
        return Shield.can_spawn
