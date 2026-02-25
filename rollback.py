class GameState:
    def __init__(self):
        self.history = []

    def save_state(self, state):
        self.history.append(state)

    def rollback(self):
        if len(self.history) > 1:
            self.history.pop()
            return self.history[-1]
        else:
            print("No previous state to rollback!")
            return None