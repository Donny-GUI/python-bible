import difflib


python_keywords = {
        'await':
        [
            "await for the execute of an object", "⭐⭐","⭐⭐⭐","⭐⭐⭐"
        ],
        'import':
        [
            "import keyword is used to import modules into the current namespace" , "⭐","⭐⭐⭐⭐⭐" ,"⭐⭐⭐⭐⭐"
        ],
        'pass':["pass is a null statement in Python. Nothing happens when it is executed. It is used as a placeholder.", "⭐","⭐⭐","⭐⭐⭐⭐⭐"],
        'None':["None is a special constant in Python that represents the absence of a value or a null value.It is an object of its own datatype, the NoneType. We cannot create multiple None objects but can assign it to variables. These variables will be equal to one another.","⭐","⭐⭐","⭐⭐⭐⭐⭐"],
        'break':["break will end the smallest loop it is in and control flows to the statement immediately below the loop. continue causes to end the current iteration of the loop, but not the whole loop.","⭐","⭐⭐⭐⭐","⭐⭐⭐"],
        'except':["except, raise, try are used with exceptions in Python.Exceptions are basically errors that suggests something went wrong while executing our program. IOError, ValueError, ZeroDivisionError, ImportError, NameError, TypeError etc. are few examples of exception in Python. try...except blocks are used to catch exceptions in Python. We can raise an exception explicitly with the raise keywor","⭐⭐","⭐","⭐⭐⭐⭐⭐"],
        'in':["used to test if a sequence (list, tuple, string etc.) contains a value. It returns True if the value is present, else it returns False","⭐⭐","⭐⭐⭐","⭐⭐⭐"],
        'raise':["except, raise, try are used with exceptions in Python.Exceptions are basically errors that suggests something went wrong while executing our program. IOError, ValueError, ZeroDivisionError, ImportError, NameError, TypeError etc. are few examples of exception in Python. try...except blocks are used to catch exceptions in Python.We can raise an exception explicitly with the raise keyword","⭐⭐⭐","⭐⭐⭐⭐","⭐⭐⭐"],
        'class':["used to define a new user-defined class in Python. Class is a collection of related attributes and methods that try to represent a real-world situation. This idea of putting data and functions together in a class is central to the concept of object-oriented programming (OOP).", "⭐⭐","⭐⭐⭐⭐⭐","⭐⭐⭐"],
        'finally':["finally is used with try…except block to close up resources or file streams.Using finally ensures that the block of code inside it gets executed even if there is an unhandled exception","⭐","⭐⭐⭐","⭐⭐⭐⭐⭐"],
        'is':["used in Python for testing object identity. While the == operator is used to test if two variables are equal or not, is is used to test if the two variables refer to the same object.","⭐⭐","⭐⭐","⭐⭐"],
        'return':["return statement is used inside a function to exit it and return a value.If we do not return a value explicitly, None is returned automatically.","⭐","⭐⭐⭐⭐⭐","⭐⭐⭐⭐⭐"],
        'continue':["break will end the smallest loop it is in and control flows to the statement immediately below the loop. continue causes to end the current iteration of the loop, but not the whole loop.","⭐","⭐⭐","⭐⭐⭐⭐⭐"],
        'for':["Generally we use for when we know the number of times we want to loop.","⭐","⭐⭐⭐⭐","⭐⭐⭐⭐⭐"],
        'lambda':["lambda is used to create an anonymous function (function with no name). It is an inline function that does not contain a return statement. It consists of an expression that is evaluated and returned. ", "⭐⭐⭐","⭐⭐⭐","⭐⭐⭐"],
        'try':["except, raise, try are used with exceptions in Python.Exceptions are basically errors that suggests something went wrong while executing our program. IOError, ValueError, ZeroDivisionError, ImportError, NameError, TypeError etc. are few examples of exception in Python. try...except blocks are used to catch exceptions in Python.We can raise an exception explicitly with the raise keyword", "⭐⭐","⭐⭐⭐","⭐⭐⭐⭐⭐"],
        'as':["as is used to create an alias while importing a module. It means giving a different name (user-defined) to a module while importing it.","⭐⭐","⭐⭐","⭐⭐⭐⭐"],
        'def':["used to define a user-defined function.","⭐","⭐⭐⭐⭐⭐","⭐⭐⭐⭐⭐"],
        'from':["from…import is used to import specific attributes or functions into the current namespace.","⭐","⭐⭐⭐⭐⭐","⭐⭐⭐⭐⭐"],
        'nonlocal':["nonlocal is used to declare that a variable inside a nested function (function inside a function) is not local to it, meaning it lies in the outer inclosing function. If we need to modify the value of a non-local variable inside a nested function, then we must declare it with nonlocal","⭐⭐","⭐","⭐"],
        'while':["while is used for looping in Python.The statements inside a while loop continue to execute until the condition for the while loop evaluates to False or a break statement is encountered.","⭐","⭐⭐⭐⭐","⭐⭐⭐"],
        'assert':[" for debugging purposes.While programming, sometimes we wish to know the internal state or check if our assumptions are true. assert helps us do this and find bugs more conveniently. assert is followed by a condition.","⭐⭐⭐⭐","⭐⭐","⭐"],
        'del':["used to delete the reference to an object. Everything is object in Python. We can delete a variable reference using del","⭐","⭐","⭐⭐"],
        'global':["global is used to declare that a variable inside the function is global (outside the function).If we need to read the value of a global variable, it is not necessary to define it as global. This is understood.If we need to modify the value of a global variable inside a function, then we must declare it with global. Otherwise, a local variable with that name is created.Following example will help us clarify this.","⭐⭐","⭐","⭐"],
        'not':["not operator is used to invert the truth value. ", "⭐","⭐⭐","⭐⭐⭐"],
        'with':["with statement is used to wrap the execution of a block of code within methods defined by the context manager.Context manager is a class that implements __enter__ and __exit__ methods. Use of with statement ensures that the __exit__ method is called at the end of the nested block. This concept is similar to the use of try…finally block","⭐⭐","⭐⭐⭐⭐","⭐⭐⭐⭐⭐"],
        'async':["The async and await keywords are provided by the asyncio library in Python. They are used to write concurrent code in Python","⭐⭐⭐","⭐⭐⭐⭐","⭐⭐⭐"],
        'elif ':[" used for conditional branching or decision making.","⭐","⭐⭐⭐","⭐⭐⭐⭐⭐"],
        'if':[" used for conditional branching or decision making.","⭐","⭐⭐⭐⭐","⭐⭐⭐⭐⭐"],
        'yield':['used inside a function like a return statement. But yield returns a generator. Generator is an iterator that generates one item at a time. A large list of values will take up a lot of memory. Generators are useful in this situation as it generates only one value at a time instead of storing all the values in memory',"⭐⭐⭐","⭐⭐⭐","⭐⭐⭐"],
        "match":["Control flow used to match a variable to its possible outcomes, psuedo-replacement for if-elif-else, this keyword pairs with case. Often cases are 'guarded' with if statements","⭐⭐","⭐⭐⭐⭐","⭐⭐⭐"],
        "case":["Control flow that pairs with the match keyword, represents a case in which the match is.", "⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐" ]
}




class RatedObject:
    def __init__(self, rating:int, max_rating=5):
        if rating > max_rating:
            rating = max_rating
        self.__rating__ = rating
        self.__rate__()
    
    def rate(self, rating:int):
        self.rating = "⭐"*rating

    def __rate__(self):
        self.rating = "⭐"*self.__rating__

class Description:
    def __init__(self,word,words):
        self.word = word
        self.__words__ = words
        self.description = words


class Keyword:

    def __init__(self,name, description=None, utility=1, popularity=1, difficulty=1):
        
        self.name = name
        self.description = description
        self.utility = RatedObject(utility)
        self.popularity = RatedObject(popularity)
        self.difficulty = RatedObject(difficulty)
        
        self.attributes = [self.name, self.description, self.utility.rating, self.popularity.rating, self.difficulty.rating]
    
    def change(self, which, what):

        two_switch = f"{which[0]}{which[1]}"
        match two_switch:
            case "na":self.name = what 
            case "de":self.description = what
            case "ut":self.utility = what
            case "po":self.popularity = what
            case "di":self.difficulty = what
            case _:pass
        
    def get(self, which):

        two_switch = f"{which[0]}{which[1]}"
        match two_switch:
            case "na":return self.name
            case "de":return self.description
            case "ut":return self.utility
            case "po":return self.popularity
            case "di":return self.difficulty
            case _:pass

    def output(self):
        for attr in self.attributes:
            print(attr)
    
class Reference:
    def __init__(self, keyword_dictionary:dict):
        self.__keyword_dict__ = keyword_dictionary
        self.__names__ = keyword_dictionary.items()
        self.keyword = {}
        for name in self.__names__:
            key = name[0]
            values = name[1]
            description = values[0]
            utility = len(values[1])
            popularity = len(values[2])
            difficulty = len(values[3])
            self.keyword[f"{key}"] = Keyword(name=key,description=description, utility=utility, popularity=popularity, difficulty=difficulty)

reference = Reference(python_keywords)
x = reference.keyword["case"].output()

print(x)