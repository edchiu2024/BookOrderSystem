class Author:

    def __init__(self, name, biography=None ):
        self.name=name
        self.biography=biography

    def get_info(self):
        return f"Author: {self.name}, Bio: {self.biography}"
    
    
