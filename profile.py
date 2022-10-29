
class ObjectProfile:
    
    def __init__(self,name:str):
        
        self.popularity = 0
        self.utility = 0
        self.name = name
        self.description = ""
        self.difficulty = 0
        self.relatedTerms = []
    
    def setDescription(self, message:str):

        self.description = message
    
    def rename(self, name:str):

        self.name = name
    
    def describe(self):

        return self.description
    

    def getRating(self, which:str):
        
        match which[0]:
            case "p":
                return self.popularity
            case "u":
                return self.utility
            case "d":
                return self.difficulty

    def setRating(self, which:str, rating:int):

        match which[0]:
            case "p":
                self.popularity = rating
            case "u":
                self.utility = rating
            case "d":
                self.utility = rating

    def related(self):

        return self.relatedTerms
    
    def relate(self, term):

        self.relatedTerms.append(term)

    def unrelate(self, term):

        for index, x in enumerate(self.relatedTerms):
            if x == term:
                self.relatedTerms.remove(self.relatedTerms[index])

class Profiles:
    def __init__(self, nametype):
        self.name=nametype
        self.profile = {}
    
    def add(self, name, description:str, popularity=1, difficulty=1, utility=1, terms=[]):
        if name is None:return
        if not isinstance(popularity, int):return
        if not isinstance(utility,int):return
        if not isinstance(difficulty, int):return
        profile = ObjectProfile(name=name, 
                                description=description, 
                                popularity=popularity,
                                difficulty=difficulty, 
                                utility=utility)
        self.profile[profile.name] = profile
    
    