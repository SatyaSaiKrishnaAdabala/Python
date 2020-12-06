# data = [
#     "Andromeda - Shrub",
#     "Bellflower - Flower",
#     "China Pink - Flower",
#     "Daffodil - Flower",
#     "Evening Primrose - Flower",
#     "French Marigold - Flower",
#     "Hydrangea - Shrub",
#     "Iris - Flower",
#     "Japanese Camellia - Shrub",
#     "Lavender - Shrub",
#     "Lilac- Shrub",
#     "Magnolia - Shrub",
#     "Peony - Shrub",
#     "Queen Anne's Lace - Flower",
#     "Red Hot Poker - Flower",
#     "Snapdragon - Flower",
#     "Sunflower - Flower",
#     "Tiger Lily - Flower",
#     "Witch Hazel - Shrub",
# ]
#
# flowers = []
# shrubs = []
#
# # write your code here
# for i in range(1,len(data) + 1):
#           if 'Shrub' in data[i-1]:
#                shrubs.append(data[i-1])
#           else:
#               flowers.append(data[i-1])
#
# print(shrubs)
# print(flowers)

# data = [1,3,4,5,7,89,80,87,323,16,670,540,708]
# print(data)
# min_value = 100
# max_value = 1000
# stop = 0
# data = sorted(data)
# print(data)
# for index,value in enumerate(data):
#     print(value)
#     if value >= min_value:
#         stop = index
#         break
# print(stop)
# del(data[:stop])
# print(data)
#
# meals = [['bacon','egg'],['bacon','chicken','spam'],['chicken','egg','spam'],['egg','chicken'],['chicken','spam']]
# for meal in meals:
#         for index in range (0,len(meal) ,1):
#             if meal[index] == "spam":
#                  del meal[index]
#         print(",".join(meal))

list1 = ['9','23','45','678','90909','234','5678','454']
ny = " ".join(list1)
new_list = ny.split()
for i in range(len(new_list)):
     new_list[i] = int(new_list[i])

print(new_list)



