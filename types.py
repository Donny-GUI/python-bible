
_types_= {
"truthy": ["a","b","c"],
"boolean" : ["",""],
"comparison" : [""],
"int":[],
"float":[],
"complex":[],
"bitwise or":[""],
"bitwise exclusive":[""],
"bitwise and":[],
"bitwise left-shift":[],
"bitwise right-shift":[],
"bitwise inverted":[],

}

class SpecialMethod:
    def __init__(self, operates_on, method_name, arguments_, description):
        
        self.arguments = arguments_
        self.description = description
        self.operator=operates_on
        self.name = method_name



        





hash_of_numerical_types = {
    "hash_fraction":{"args":["m","n"], "description":["Compute the hash of a rational number m / n. Assumes m and n are integers, with n positive. Equivalent to hash(fractions.Fraction(m, n))."],"examples":[]},
    "hash_float":{"args":["x"], "description":["Compute the hash of a float x"],"examples":[""]},
    "hash_complex":{"args":["z"], "description":["Compute the hash of a complex number z"],"examples":[""]},
}


iterator_types = {
    "container.__iter__":{"args":[""], "description":["Return an iterator object. The object is required to support the iterator protocol described below. If a container supports different types of iteration, additional methods can be provided to specifically request iterators for those iteration types. (An example of an object supporting multiple forms of iteration would be a tree structure which supports both breadth-first and depth-first traversal.) This method corresponds to the tp_iter slot of the type structure for Python objects in the Python/C API."],"examples":[]},
    "iterator.__iter__":{"args":[""], "description":["Return the iterator object itself. This is required to allow both containers and iterators to be used with the for and in statements. This method corresponds to the tp_iter slot of the type structure for Python objects in the Python/C API."],"examples":[]},
    "iterator.__next__":{"args":[""], "description":["Return the next item from the iterator. If there are no further items, raise the StopIteration exception. This method corresponds to the tp_iternext slot of the type structure for Python objects in the Python/C API."],"examples":[]}
}


sequence_operations = {
    "x in object":{"description":["True if an item of object is equal to x, else false"],"examples":["'arab' in 'parabola' -> True"]},
    "x not in object":{"description":["False if an item of object is equal to x, else true"],"examples":[]},
    "object + x":{"description":["the concatenation of object and x"],"examples":[]},
    "object*i":{"description":["adding object to itself i times"],"examples":[]},
    "object[i]":{"description":["i-th item of object, starting at 0, 1 being next, negative one being last"],"examples":[]},
    "object[a:b]":{"description":["slice of object from a upto b"],"examples":[]},
    "object[a:b:c]":{"description":["slice of object from a upto b upfrom b to c"],"examples":[]},
    "len(object)":{"description":["length of object"],"examples":[]},
    "min(object)":{ "description":["smallest item of object"],"examples":[]},
    "max(object)":{"description":["largest item of object"], "examples":[""]},
    "object.index(x)":{"description":["index of the first occurence of x in object"], "examples":[""]},
    "object.count(x)":{"description":["total count of x in object"], "examples":[""]},
}


