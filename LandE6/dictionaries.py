'''
catnames = ['bubbles', 'brownie', 'tuna', 'sherlock']
print(sorted(catnames))
#Output: ['brownie', 'bubbles', 'sherlock', 'tuna']'''

'''#sorting dictionairies using sorted(): by default , Python returns a list which is sorted by key order
catnames_pref = {'bubbles': 1, 'brownie': 4, 'tuna': 2, 'sherlock': 3}
print(sorted(catnames_pref))
#Output: ['brownie', 'bubbles', 'sherlock', 'tuna']'''

catnames_pref = {'bubbles': 1, 'brownie': 4, 'tuna': 2, 'sherlock': 3}
sorted_catnames = sorted(catnames_pref, key=catnames_pref.get, reverse=False)

for name in catnames_pref:
    print(catnames_pref[name], name)
'''Output:
1 bubbles
4 brownie
2 tuna
3 sherlock'''
