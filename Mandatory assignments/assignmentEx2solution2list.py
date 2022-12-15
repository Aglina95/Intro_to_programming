size_list = ["S", "M", "L", "XL"]

def make_shirt(size, message):
    #case insensitive, we will accept sizes in lower case
    size_upper = size.upper()


    if size_upper in size_list:
        return f"I will print a t-shirt in size {size_upper} that says '{message}'"
    else:
        return "This t-shirt size is unavailable"


#print(make_shirt("S", "KBH"))
#print(make_shirt("L", "I love ITU"))
#print(make_shirt("XXS", "Amager4Ever"))
#print(make_shirt("xl", "I love ITU"))
