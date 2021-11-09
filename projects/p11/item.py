class Item:
    
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __str__(self):
        return "Name: {}, Category: {}".format(self.name, self.category)
    