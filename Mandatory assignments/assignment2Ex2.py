def make_shirt(size, message):
    #case insensitive, we will accept sizes in lower case
    size_upper = size.upper()
    #quotation_mark = "'"

    if size_upper == "S" or size_upper == "M" or size_upper == "L" or size_upper == "XL":
        #return "I will print a t-shirt in size " + size_upper + " that says " + "'" + message + "'"
        #return f'I will print a t-shirt in size {size_upper} that says {quotation_mark}{message}{quotation_mark}'
        return f'I will print a t-shirt in size {size_upper} that says \'{message}\''
    else:
        return "This t-shirt size is unavailable"


print(make_shirt("S", "KBH"))
print(make_shirt("L", "I love ITU"))
print(make_shirt("XXS", "Amager4Ever"))
print(make_shirt("xl", "I love ITU"))
