def merge_dicts(dict1, dict2):
    matching_keys = []
    for movie in dict1.keys():
        if movie in dict2:
            matching_keys.append(movie)
            
    return matching_keys


#or

dict1 = {'name': 'bobby', 'topic': 'Python', 'salary': 100}
dict2 = {'name': 'alice', 'salary': 100, 'experience': 5}


common_keys = [key for key in dict1
               if key in dict2]
print(common_keys) # 👉️ ['name', 'salary']

#or

dict1 = {'name': 'bobby', 'topic': 'Python', 'salary': 100}
dict2 = {'name': 'alice', 'salary': 100, 'experience': 5}

common_keys = list(dict1.keys() & dict2.keys())
print(common_keys)  # 👉️ ['salary', 'name']