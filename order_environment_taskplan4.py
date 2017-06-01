import re
import random
'''
Scenario: Toast bread
'''
breadList=['bread',
           'white bread',
           'wheat bread',
           'whole grain bread',
           'french bread',
           'croissant',
           'bagel',
           'donut',
           'rolls',
           'hot dog bun',
           ]

plateList=['dish',
          'white dish',
          'blue dish',
          'red dish',
          'green dish',
          'yellow dish',
          'small dish',
          'big dish',
          'plate',
          'white plate',
          'blue plate',
          'red plate',
          'green plate',
          'yellow plate',
          'small plate',
          'big plate',
          ]

kitchenEquipmentList=['toaster',
             'big toaster',
             'small toaster',
             'toaster oven',
             'oven',
             'grill',
             ]

buttonList=['button',
            ]

orderList_general=['toast the bread',
                   'toast bread',
                   'toast some bread',
                   'toast a piece of bread',
                   'make me a toast',
                   'make me some toast',
                   'make me a piece of toast',
                   'get me a toast',
                   'get me some toast',
                   'get me a piece of toast',
                   'please toast the bread',
                   'please toast bread',
                   'please toast some bread',
                   'please toast a piece of bread',
                   'please make me a toast',
                   'please make me some toast',
                   'please make me a piece of toast',
                   'please get me a toast',
                   'please get me some toast',
                   'please get me a piece of toast',
                   'toast the bread please',
                   'toast bread please',
                   'toast some bread please',
                   'toast a piece of bread please',
                   'make me a toast please',
                   'make me some toast please',
                   'make me a piece of toast please',
                   'get me a toast please',
                   'get me some toast please',
                   'get me a piece of toast please',
                   'could you toast the bread ?',
                   'could you toast some bread ?',
                   'could you toast a piece of bread ?',
                   'could you get me some toast ?',
                   'could you get me a toast ?',
                   'could you get me a piece of toast ?',
                   'could you make me some toast ?',
                   'could you make me a toast ?',
                   'could you make me a piece of toast ?',
                   'can you toast the bread ?',
                   'can you toast some bread ?',
                   'can you toast a piece of bread ?',
                   'can you get me some toast ?',
                   'can you get me a toast ?',
                   'can you get me a piece of toast ?',
                   'can you make me some toast ?',
                   'can you make me a toast ?',
                   'can you make me  a piece of toast ?',
                   ]

def permute(xs, low=0):
    if low + 1 >= len(xs):
        yield xs
    else:
        for p in permute(xs, low + 1):
            yield p
        for i in range(low + 1, len(xs)):
            xs[low], xs[i] = xs[i], xs[low]
            for p in permute(xs, low + 1):
                yield p
            xs[low], xs[i] = xs[i], xs[low]


file = open("../data/order-environment-taskplan4.txt", 'w')
pairs = []
i=0

# Case1: Order - General order
#        Objects - a toaster, a bread, a plate

for order in orderList_general:
    for plate in plateList:
        for kitchenEquipment in kitchenEquipmentList:
            for bread in breadList:
                environmentList = []
                for env in permute([bread, plate, kitchenEquipment]):
                    environmentList.append( ' , '.join(env))
                for environment in environmentList:
                    taskplan = bread    + ' grasp '  + bread + ' '+\
                               bread    + ' locate ' + kitchenEquipment +' '+\
                               bread    + ' put '    + kitchenEquipment +' '+\
                               'button' + ' push '   + 'button'+' '+\
                               kitchenEquipment + ' wait '+ kitchenEquipment+' '+\
                               bread    + ' grasp '  + bread +' '+\
                               bread    + ' locate ' + plate +' '+\
                               bread    + ' release '+ bread

                    #print i, order + '\t' + environment + '\t' + taskplan
                    #file.writelines(order + '\t' + environment + '\t' + taskplan)
                    pairs.append(order + '\t' + environment + '\t' + taskplan)
                    i+=1

# Case2: Order - General order
#        Objects - a toaster, many types of bread, a plate
for NUM_BREAD in range(1,4):
    for order in orderList_general:
        for plate in plateList:
            for kitchenEquipment in kitchenEquipmentList:
                breadList_sampled = random.sample(breadList,NUM_BREAD)
                permuteList = []
                for bread in breadList_sampled:
                    permuteList.append(bread)
                environmentList = []
                permuteList.append(plate)
                permuteList.append(kitchenEquipment)
                for env in permute(permuteList):
                    environmentList.append( ' , '.join(env))


                for environment in environmentList:
                    bread = random.choice(breadList_sampled)
                    taskplan = bread    + ' grasp '  + bread + ' '+\
                               bread    + ' locate ' + kitchenEquipment +' '+\
                               bread    + ' put '    + kitchenEquipment +' '+\
                               'button' + ' push '   + 'button'+' '+\
                               kitchenEquipment + ' wait '+ kitchenEquipment+' '+\
                               bread    + ' grasp '  + bread +' '+\
                               bread    + ' locate ' + plate +' '+\
                               bread    + ' release '+ bread

                    #print i, order + '\t' + environment + '\t' + taskplan
                    #file.writelines(order + '\t' + environment + '\t' + taskplan)
                    pairs.append(order + '\t' + environment + '\t' + taskplan)
                    i+=1

pairs_sampled = random.sample(pairs,10000)
i=0
for pair in pairs_sampled:
    print i, pair
    file.write(pair+'\n')
    i+=1

file.close()