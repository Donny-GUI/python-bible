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