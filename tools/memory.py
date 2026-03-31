class Memory:
    def __init__(self):
        self.store = {}

    def remember(self, key: str, value: str):
        self.store[key] = value
        return f"Remembered: {key} → {value}"

    def recall(self, key: str):
        return self.store.get(key, "Nothing remembered for that key.")
