#split a string into 2 string
lhs, rhs = "stringof/character".split("/", 1)
#result in lhs = "stringof" and rhs = "character".
#this method only work if we know a certain charracter exit withing a string.
#This method can be use to split a http address. www.google.com/hello
lhs, rhs = "www.google.com/hello".split("/", 1)
#rhs to determine whether to display error message 404 or retrieve file with the name rhs to send back to client.
