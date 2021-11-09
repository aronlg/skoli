class Catalog:
    
    def __init__(self, name):
        self.name = name
        self.__collection = []

    def __str__(self):
        return_str = "Catalog {}:".format(self.name)
        for item in self.__collection:
            return_str += '\n\t' + str(item)
        return return_str

    def add(self, item):
        self.__collection.append(item)

    def remove(self, item):
        self.__collection.remove(item)

    def find_item(self, name):
        for item in self.__collection:
            if item.name == name:
                return item
        return None
             
    def clear(self):
        self.__collection = []
    
    def __add__(self, other):
        '''Returns a new catalog consisting of all items from self and other'''
        combined_catalog = Catalog("{}+{}".format(self.name, other.name))
        for item in self.__collection:
            combined_catalog.add(item)
        for item in other.__collection:
            combined_catalog.add(item)
        
        return combined_catalog
