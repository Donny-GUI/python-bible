float_methods = {
    "float.as_integer_ratio":{
        "args":[""],
        "description":["Return a pair of integers whose ratio is exactly equal to the original float and with a positive denominator. Raises OverflowError on infinities and a ValueError on NaNs."]
        },
    "float.is_integer":{
        "args":[""],
        "description":["Return True if the float instance is finite with integral value, and False otherwise"]
        },
    "float.hex":{
        "args":[""],
        "description":["Return a representation of a floating-point number as a hexadecimal string. For finite floating-point numbers, this representation will always include a leading 0x and a trailing p and exponent."]
        },
    "float.fromhex":[["s"],"Class method to return the float represented by a hexadecimal string s. The string s may have leading and trailing whitespace.Note that float.hex() is an instance method, while float.fromhex() is a class method."],

}
integer_methods = {
    "int.bit_length":[
        [""], 
        "Return the number of bits necessary to represent an integer in binary, excluding the sign and leading zeros"],
    "int.bit_count":[
        [""],
        "Return the number of ones in the binary representation of the absolute value of the integer. This is also known as the population count."],
    "int.to_bytes":[
        ["length", "byteorder", "*", "signed=False"], 
        "Return an array of bytes representing an integer."],
    "from_bytes": [
        ["bytes", "byteorder", "*", "signed=False"],
        "Return the integer represented by the given array of bytes."],
    "as_integer_ratio":[
        ["bytes", "byteorder", "*", "signed=False"],"Return the integer represented by the given array of bytes."]
}
mutable_sequence_types = {
    "objects[i]=x":{"description":["item i of objects replaced by x"], "examples":["example here"]},
    "objects[i:j]=x":{"description":["slice of objects from i to j replaced by the contents of iterable x"], "examples":["example here"]},
    "del objects[i:j]":{"description":["delete items of objects from i to j"], "examples":["example here"]},
    "objects.append(x)":{"description":["add x to the end of the list named objects"], "examples":["example here"]},
    "objects.clear()":{"description":["remove all items from objects"], "examples":["example here"]},
    "objects.copy()":{"description":["create a shallow copy of objects, same as objects[:]"], "examples":["example here"]},
    "objects.extend(x)":{"description":["extends items of objects with the contents of x, or object+=x"], "examples":["example here"]},
    "objects.insert(x,y)":{"description":["insert y at place x in objects"], "examples":["example here"]},
    "objects.pop(i)":{"description":["retrieves the item at i and also remove it from objects, if no i is specified, the next from the order they were put into objects"], "examples":["example here"]},
    "objects.remove(x)":{"description":["remove the first item of objects that is x"], "examples":["example here"]},
    "objects.reverse()":{"description":["reverse the order of objects from its initial orientation"], "examples":["example here"]}
}

list_methods = {
    "list()":{"args":[""],"description":["Lists are mutable sequences, typically used to store collections of homogeneous items (where the precise degree of similarity will vary by application)."]},
    "list_x.sort()":{"args":["*", "key=None", "reverse=False"],"description":["This method sorts the list in place, using only < comparisons between items. Exceptions are not suppressed - if any comparison operations fail, the entire sort operation will fail (and the list will likely be left in a partially modified state).sort() accepts two arguments that can only be passed by keyword (keyword-only arguments):key specifies a function of one argument that is used to extract a comparison key from each list element (for example, key=str.lower). The key corresponding to each item in the list is calculated once and then used for the entire sorting process. The default value of None means that list items are sorted directly without calculating a separate key value.The functools.cmp_to_key() utility is available to convert a 2.x style cmp function to a key function.reverse is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed."]},
    "tuple()":{"args":["iterable"],"description":["Tuples are immutable sequences, typically used to store collections of heterogeneous data (such as the 2-tuples produced by the enumerate() built-in). Tuples are also used for cases where an immutable sequence of homogeneous data is needed (such as allowing storage in a set or dict instance)."]},
    "range()":{"args":["stop", "start", "stop[step]"],"description":["The range type represents an immutable sequence of numbers and is commonly used for looping a specific number of times in for loops."]},
    
    }
string_methods = {
    "string_x.capitalize()":{"args":["iterable"],"description":["Return a copy of the string with its first character capitalized and the rest lowercased."]},
    "string_x.casefold()":{"args":[""],"description":["Return a casefolded copy of the string. Casefolded strings may be used for caseless matching."]},
    "string_x.center()":{"args":["width"],"description":["Return centered in a string of length width."]},
    "string_x.encode()":{"args":["encoding='utf-8'","errors='strict'", ""],"description":["Return an encoded version of the string as a bytes object. Default encoding is 'utf-8'. errors may be given to set a different error handling scheme."]},
    "string_x.count()":{"args":["sub"],"description":["Return the number of non-overlapping occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation."]},
    "string_x.endswith()":{"args":["suffix[x:y]"],"description":["Return True if the string ends with the specified suffix, otherwise return False. suffix can also be a tuple of suffixes to look for. With optional start, test beginning at that position. With optional end, stop comparing at that position."]},
    "string_x.expantabs()":{"args":["tabsize=8"],"description":["Return a copy of the string where all tab characters are replaced by one or more spaces, depending on the current column and the given tab size. Tab positions occur every tabsize characters (default is 8, giving tab positions at columns 0, 8, 16 and so on). To expand the string, the current column is set to zero and the string is examined character by character. If the character is a tab (\t), one or more space characters are inserted in the result until the current column is equal to the next tab position. (The tab character itself is not copied.) If the character is a newline (\n) or return (\r), it is copied and the current column is reset to zero. Any other character is copied unchanged and the current column is incremented by one regardless of how the character is represented when printed."]},

}
