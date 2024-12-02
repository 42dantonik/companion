from visual.font import Font
from visual.format import Format

class StyleSheet:
    def __init__(self, bg_color = "transparent", font = Font(), format = Format(), border = "0px solid black", radius="0px"):
        self.bg_color = bg_color
        self.font = font
        self.format = format
        self.border = border
        self.radius = radius
        
    def __str__(self):
        return f"background-color: {self.bg_color}; border-radius: {self.radius}; border: {self.border}; {str(self.format)}{str(self.font)}"