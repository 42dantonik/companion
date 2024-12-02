class Font:
    def __init__(self, size = "16px", family = "Arial", color = "black"):
        self.color = color
        self.size = size
        self.family = family
        
    def __str__(self):
        return f"color: {self.color}; font-size: {self.size}; font-family: {self.family};"