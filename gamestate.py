class GameState:
    def __init__(self):
        self.score = 0
        self.PAUSED = False

    def update_score(self, val):
        self.score += val

    def get_score(self):
        text_to_display = f"{self.score}"
        if self.PAUSED:
            text_to_display += " - PAUSED"
        return text_to_display
