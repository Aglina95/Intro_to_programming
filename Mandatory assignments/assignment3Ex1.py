# Write your code here :-)
def stores_missing_goods(goods):
    for good in goods:
        for location in goods[good]:
            if goods[good][location] == 0:
                return location + " is missing " + good + "!"

store_goods = {
    'Beer' : {
    'Amager' : 12,
    'Indre By' : 24,
    'Valby' : 1
    },
    'Red Wine' : {
    'Amager' : 0,
    'Indre By' : 176,
    'Valby' : 12
    }
}

print(store_goods['Beer']['Indre By'])
print(store_goods['Beer'].keys())
print(store_goods['Red Wine'].items())
print(len(store_goods['Red Wine'].items()))
print(stores_missing_goods(store_goods))
