class Format:
    def __init__(self, padding = "3px 3px 3px 3px", margin = "3px 3px 3px 3px"):
        self.padding = padding
        self.margin = margin

    def __str__(self):
        return f"padding: {self.padding}; margin: {self.margin};"