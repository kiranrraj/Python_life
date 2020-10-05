class Human:

    def __init__(self, species, loc):
        self.species = species
        self.loc = loc

class Indian(Human):

    def __init__(self, species, location, country, continent="Asia"):
        super().__init__(species, location)
        self.country = country
        self.continent = continent


class Keralite(Indian):

    def __init__(self, species, location, country, state, lang, continent="Asia"):
        super().__init__(species, location, country, continent="Asia")
        self.state = state
        self.lang = lang

    
