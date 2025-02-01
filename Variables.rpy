init python:
    class Variables():
        def __init__(self):
            self._points = 0
            self.mistakes = 0

        @property
        def points(self):
            return self._points
        @points.setter
        def points(self, value):
            if value < 0:
                self.mistakes += 1
            self._points += value
        
        def correct_choice(self, is_true):
            if is_true:
                self.points += 5
            else:
                self.points -= 1
          
        @property
        def playerpoints(self):
            return self.points
        
        @playerpoints.setter
        def playerpoints(self, value):  
            self.points = value
            if self.correct_choice:  
                self.points += 5

#        (Wrapper)
#        def correct_choice(self, is_true): 
#            if is_true:
#                self.points += 5
#            else:
#                self.points -= 1

#        @property
#        def playermistakes(self):
#            return self.mistakes
#        
#        @playermistakes.setter
#        def playermistakes(self, value):
#            self.mistakes = value
#            if self.incorrect_choice:  # Added self reference
#                self.mistakes += 1
        
#        @property
#        def mistakeschecker(self):
#            return self.mistakes_check
#        
#        @mistakeschecker.setter
#        def mistakeschecker(self, value):  
#            self.mistakes_check = value
#            if self.mistakes >= 2:
#                self.retry_option = True
#            else:
#                self.retry_option = False


