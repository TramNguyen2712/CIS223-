class EnglishRuler(object):
    def __init__(self, num_inches, major_length):
        self._num_inches = num_inches
        self._major_length = major_length

    def draw_line(self, tick_length, tick_label=''):
        """Helper function to draw dashes at each tick"""
        line = "-" * tick_length
        if tick_label:
            line += " " + tick_label
        print(line)

    def draw_interval(self, center_length):
        """Draw the interior of the English Ruler"""
        if center_length > 0:
            self.draw_interval(center_length-1)
            self.draw_line(center_length)
            self.draw_interval(center_length-1)

    def draw_ruler(self):
        """Actual drawing staring with label 0"""
        self.draw_line(self._major_length, "0")
        for j in range(1, self._num_inches + 1):
            self.draw_interval(self._major_length - 1)   # a recursive function
            self.draw_line(self._major_length, str(j))

if __name__ == "__main__":
    ruler = EnglishRuler(2, 3)
    #ruler.draw_ruler()

    ruler2 = EnglishRuler(12, 6)
    ruler2.draw_ruler()

