import re

file_toWrite1 = open("../data/1order-environment-taskplan.txt", 'w')

order_list = ["Make a cereal", "Make some cereal", "Give me a cereal for breakfast", "Please Give me some cereal",
         "Let's make cereal", "Make a cereal for me", "Give me something to eat like cereal",
              "please give me something to eat with milk", "Hey, give me cereal", "Can you make cereal for me?"]


bowl = ["bowl", "blue bowl", "yellow bowl", "green bowl", "red bowl", "pink bowl", "purple bowl"]
cereal = [" ", "cereal", "corn flake cereal", "special k cereal", "frosted flakes cereal", "chocolate chex cereal"]
milk = [" ", "milk", "fresh milk", "chocolate milk", "strawberry milk", "banana milk"]

object_list = []
task_list = []
object_task_list=[]
for i in range(1,len(bowl)+1):  # for b in bowl:
    for j in range(1,len(cereal)+1):
        for k in range(1,len(milk)+1):
            if j == 1:
                if k == 1:
                    object = bowl[i-1]
                    object_list.append(object)
                    task = "Mission Impossible."
                    task_list.append(task)
                    object_task = object + '\t' + task +'\n'
                    object_task_list.append(object_task)
                    object_task = task + '\t' + object + '\n'
                    object_task_list.append(object_task)
                else:
                    object = bowl[i - 1] + " , " + milk[k - 1]
                    object_list.append(object)
                    task = milk[k - 1] + " grasp " + milk[k - 1] + " " + milk[k - 1] + " move " + bowl[i - 1] + " " + milk[
                        k - 1] + " pour " + bowl[i - 1] + " " + milk[k - 1] + " locate " + milk[k - 1] + " " + milk[
                               k - 1] + " release " + milk[k - 1]
                    task_list.append(task)
                    object_task = object + '\t' + task + '\n'
                    object_task_list.append(object_task)
                    object_task = task + '\t' + object + '\n'
                    object_task_list.append(object_task)
            else:
                if k == 1:
                    object = bowl[i-1] + " , " + cereal[j-1]
                    object_list.append(object)
                    task = cereal[k - 1]+" grasp "+cereal[k - 1]+ " "+cereal[k - 1]+" move "+bowl[i - 1] + " " + cereal[
                        k - 1] + " pour " + bowl[i - 1] + " " + cereal[k - 1] + " locate " + cereal[k - 1] + " " + cereal[
                               k - 1] + " release " + cereal[k - 1]
                    task_list.append(task)
                    object_task = object + '\t' + task + '\n'
                    object_task_list.append(object_task)
                    object_task = task + '\t' + object + '\n'
                    object_task_list.append(object_task)
                else:
                    object = bowl[i-1] + " , " + cereal[j-1] + " , " + milk[k-1]
                    object_list.append(object)
                    task = cereal[k - 1]+" grasp "+cereal[k - 1]+ " "+cereal[k - 1]+" move "+bowl[i - 1] + " " + cereal[
                        k - 1] + " pour " + bowl[i - 1] + " " + cereal[k - 1] + " locate " + cereal[k - 1] + " " + cereal[
                               k - 1] + " release " + cereal[k - 1] + " " + milk[k - 1] + " grasp " + milk[k - 1] + " " + milk[k - 1] + \
                                    " move " + bowl[i - 1] + " " + milk[k - 1] + " pour " + bowl[i - 1] + " " + milk[k - 1] + " locate " + milk[k - 1] \
                                        + " " + milk[k - 1] + " release " + milk[k - 1]
                    task_list.append(task)
                    object_task = object + '\t' + task + '\n'
                    object_task_list.append(object_task)
                    object_task = task + '\t' + object + '\n'
                    object_task_list.append(object_task)

print(object_task_list)


for i in range(len(order_list)+1):
    for j in range(len(object_task_list)+1):
        line_tobe_written = order_list[i-1]+'\t'+object_task_list[j-1]
        file_toWrite1.write(line_tobe_written)

file_toWrite1.close()