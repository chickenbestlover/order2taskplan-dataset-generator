import re
import random
file_toWrite = open("../data/order-environment-taskplan5.txt", 'w')

sprinkle_object = ["pepper", "salt", "sugar"]

squeeze_object = ["ketchup", "mayonnaise"]

pour_object = ["coffee", "water"]
pour_milk = ["milk", "fresh milk", "chocolate milk",
             "strawberry milk", "banana milk"]
pour_softdrink = ["soda", "coke", "coke", "cola", "cocacola", "sprite",
                  "mountain dew", "fanta", "pepsi"]
pour_juice = ["juice", "orange juice", "apple juice", "grape juice", "kiwi juice"]
pour_sauce = ["soy sauce", "chili sauce", "hot sauce", "barbecue sauce", "wine sauce"]

# make the color container set
container_list = [""]
container = ["bowl", "bottle", "cup", "sprinkler", "sauce container"]
color = ["", "blue", "yellow", "green", "green", "red", "pink", "purple"]

for i in range(0, len(container)):
    for j in range(0, len(color)):
        if j == 0:
            color_container = container[i]
            container_list.append(color_container)
        else:
            color_container = color[j] + " " + container[i]
            container_list.append(color_container)


# make the situational behaviour
order_default = ["Give me ", "Give me some ", "Give me the ", "Please give me ", "Please give me some ", "Please give me the ",
                 "I want ", "I want some ", "I want the ", "I need ", "I need some ", "I need the ",
                 "Can I get ", "Can I get some ", "Can I get the ", "Can you give me ", "Can you give me some ", "Can you give me the "]
order_list = []
situation_list = []
behavior_list = []
order_situation_behavior_list = []

# Sprinkle_object
for i in range(0, len(order_default)):
    for j in range(0, len(sprinkle_object)):
        for k in range(0, len(container_list)):
            if k == 0:
                order = order_default[i] + sprinkle_object[j]
                order_list.append(order)
                situation = sprinkle_object[j]
                situation_list.append(situation)
                behavior = "Mission impossible"
                behavior_list.append(behavior)
                order_situation_behavior = order + '\t' + situation + '\t' + behavior
                order_situation_behavior_list.append(order_situation_behavior)
            else:
                order = order_default[i] + sprinkle_object[j]
                order_list.append(order)
                situation = container_list[k] + " , " + sprinkle_object[j]
                situation_rev = sprinkle_object[j] + " , " + container_list[k]
                situation_list.append(situation)
                behavior = sprinkle_object[j] + " grasp " + sprinkle_object[j] + " " + \
                           sprinkle_object[j] + " sprinkle " + container_list[k] + " " + \
                           sprinkle_object[j] + " locate " + sprinkle_object[j] + " " + \
                           sprinkle_object[j] + " release " + sprinkle_object[j]
                behavior_list.append(behavior)
                order_situation_behavior = order + '\t' + situation + '\t' + behavior
                order_situation_behavior_list.append(order_situation_behavior)
                order_situation_behavior = order + '\t' + situation_rev + '\t' + behavior
                order_situation_behavior_list.append(order_situation_behavior)
# Squeeze object

for i in range(0, len(order_default)):
    for j in range(0, len(squeeze_object)):
        for k in range(0, len(container_list)):
            if k == 0:
                order = order_default[i] + squeeze_object[j]
                order_list.append(order)
                situation = squeeze_object[j]
                situation_list.append(situation)
                behavior = "Mission impossible"
                behavior_list.append(behavior)
                order_situation_behavior = order + '\t' + situation + '\t' + behavior
                order_situation_behavior_list.append(order_situation_behavior)
            else:
                order = order_default[i] + squeeze_object[j]
                order_list.append(order)
                situation = container_list[k] + " , " + squeeze_object[j]
                situation_rev = squeeze_object[j] + " , " + container_list[k]
                situation_list.append(situation)
                behavior = squeeze_object[j] + " grasp " + squeeze_object[j] + " " + \
                           squeeze_object[j] + " squeeze " + container_list[k] + " " + \
                           squeeze_object[j] + " locate " + squeeze_object[j] + " " + \
                           squeeze_object[j] + " release " + squeeze_object[j]
                behavior_list.append(behavior)
                order_situation_behavior = order + '\t' + situation + '\t' + behavior
                order_situation_behavior_list.append(order_situation_behavior)
                order_situation_behavior = order + '\t' + situation_rev + '\t' + behavior
                order_situation_behavior_list.append(order_situation_behavior)

# Pour object

for i in range(0, len(order_default)):
    for j in range(0, len(pour_object)):
        for k in range(0, len(container_list)):
            if k == 0:
                order = order_default[i] + pour_object[j]
                order_list.append(order)
                situation = pour_object[j]
                situation_list.append(situation)
                behavior = "Mission impossible"
                behavior_list.append(behavior)
                order_situation_behavior = order + '\t' + situation + '\t' + behavior
                order_situation_behavior_list.append(order_situation_behavior)
            else:
                order = order_default[i] + pour_object[j]
                order_list.append(order)
                situation = container_list[k] + " , " + pour_object[j]
                situation_rev = pour_object[j] + " , " + container_list[k]
                situation_list.append(situation)
                behavior = pour_object[j] + " grasp " + pour_object[j] + " " + \
                           pour_object[j] + " pour " + container_list[k] + " " + \
                           pour_object[j] + " locate " + pour_object[j] + " " + \
                           pour_object[j] + " release " + pour_object[j]
                behavior_list.append(behavior)
                order_situation_behavior = order + '\t' + situation + '\t' + behavior
                order_situation_behavior_list.append(order_situation_behavior)
                order_situation_behavior = order + '\t' + situation_rev + '\t' + behavior
                order_situation_behavior_list.append(order_situation_behavior)

# Pour milk
for i in range(0, len(order_default)):
    for j in range(0, len(pour_milk)):
        for k in range(0, len(container_list)):
            if k == 0:
                order = order_default[i] + pour_milk[j]
                order_list.append(order)
                situation = pour_milk[j]
                situation_list.append(situation)
                behavior = "Mission impossible"
                behavior_list.append(behavior)
                order_situation_behavior = order + '\t' + situation + '\t' + behavior
                order_situation_behavior_list.append(order_situation_behavior)
            else:
                order = order_default[i] + pour_milk[j]
                order_list.append(order)
                situation = container_list[k] + " , " + pour_milk[j]
                situation_rev = pour_milk[j] + " , " + container_list[k]
                situation_list.append(situation)
                behavior = pour_milk[j] + " grasp " + pour_milk[j] + " " + \
                           pour_milk[j] + " pour " + container_list[k] + " " + \
                           pour_milk[j] + " locate " + pour_milk[j] + " " + \
                           pour_milk[j] + " release " + pour_milk[j]
                behavior_list.append(behavior)
                order_situation_behavior = order + '\t' + situation + '\t' + behavior
                order_situation_behavior_list.append(order_situation_behavior)
                order_situation_behavior = order + '\t' + situation_rev + '\t' + behavior
                order_situation_behavior_list.append(order_situation_behavior)

# Pour soft drink

for i in range(0, len(order_default)):
    for j in range(0, len(pour_softdrink)):
        for k in range(0, len(container_list)):
            if k == 0:
                order = order_default[i] + pour_softdrink[j]
                order_list.append(order)
                situation = pour_softdrink[j]
                situation_list.append(situation)
                behavior = "Mission impossible"
                behavior_list.append(behavior)
                order_situation_behavior = order + '\t' + situation + '\t' + behavior
                order_situation_behavior_list.append(order_situation_behavior)
            else:
                order = order_default[i] + pour_softdrink[j]
                order_list.append(order)
                situation = container_list[k] + " , " + pour_softdrink[j]
                situation_rev = pour_softdrink[j] + " , " + container_list[k]
                situation_list.append(situation)
                behavior = pour_softdrink[j] + " grasp " + pour_softdrink[j] + " " + \
                           pour_softdrink[j] + " pour " + container_list[k] + " " + \
                           pour_softdrink[j] + " locate " + pour_softdrink[j] + " " + \
                           pour_softdrink[j] + " release " + pour_softdrink[j]
                behavior_list.append(behavior)
                order_situation_behavior = order + '\t' + situation + '\t' + behavior
                order_situation_behavior_list.append(order_situation_behavior)
                order_situation_behavior = order + '\t' + situation_rev + '\t' + behavior
                order_situation_behavior_list.append(order_situation_behavior)

# Pour juice

for i in range(0, len(order_default)):
    for j in range(0, len(pour_juice)):
        for k in range(0, len(container_list)):
            if k == 0:
                order = order_default[i] + pour_juice[j]
                order_list.append(order)
                situation = pour_juice[j]
                situation_list.append(situation)
                behavior = "Mission impossible"
                behavior_list.append(behavior)
                order_situation_behavior = order + '\t' + situation + '\t' + behavior
                order_situation_behavior_list.append(order_situation_behavior)
            else:
                order = order_default[i] + pour_juice[j]
                order_list.append(order)
                situation = container_list[k] + " , " + pour_juice[j]
                situation_rev = pour_juice[j] + " , " + container_list[k]
                situation_list.append(situation)
                behavior = pour_juice[j] + " grasp " + pour_juice[j] + " " + \
                           pour_juice[j] + " pour " + container_list[k] + " " + \
                           pour_juice[j] + " locate " + pour_juice[j] + " " + \
                           pour_juice[j] + " release " + pour_juice[j]
                behavior_list.append(behavior)
                order_situation_behavior = order + '\t' + situation + '\t' + behavior
                order_situation_behavior_list.append(order_situation_behavior)
                order_situation_behavior = order + '\t' + situation_rev + '\t' + behavior
                order_situation_behavior_list.append(order_situation_behavior)

# Pour sauce

for i in range(0, len(order_default)):
    for j in range(0, len(pour_sauce)):
        for k in range(0, len(container_list)):
            if k == 0:
                order = order_default[i] + pour_sauce[j]
                order_list.append(order)
                situation = pour_sauce[j]
                situation_list.append(situation)
                behavior = "Mission impossible"
                behavior_list.append(behavior)
                order_situation_behavior = order + '\t' + situation + '\t' + behavior
                order_situation_behavior_list.append(order_situation_behavior)
            else:
                order = order_default[i] + pour_sauce[j]
                order_list.append(order)
                situation = container_list[k] + " , " + pour_sauce[j]
                situation_rev = pour_sauce[j] + " , " + container_list[k]
                situation_list.append(situation)
                behavior = pour_sauce[j] + " grasp " + pour_sauce[j] + " " + \
                           pour_sauce[j] + " pour " + container_list[k] + " " + \
                           pour_sauce[j] + " locate " + pour_sauce[j] + " " + \
                           pour_sauce[j] + " release " + pour_sauce[j]
                behavior_list.append(behavior)
                order_situation_behavior = order + '\t' + situation + '\t' + behavior
                order_situation_behavior_list.append(order_situation_behavior)
                order_situation_behavior = order + '\t' + situation_rev + '\t' + behavior
                order_situation_behavior_list.append(order_situation_behavior)

'''
for i in range(0, len(order_situation_behavior_list)):
    file_toWrite.write(order_situation_behavior_list[i] + '\n')
'''

pairs_sampled = random.sample(order_situation_behavior_list,10000)

for pair in pairs_sampled:
    file_toWrite.write(pair+'\n')

file_toWrite.close()