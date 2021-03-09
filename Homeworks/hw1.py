#list that has even numbers from 0  to 10 (except 10)
list1=[i for i in range(10) if i%2==0]
#list that has odd numbers from 0 to 10 (except 10)
list2=[i for i in range(10) if i%2==1]
#merge of two lists
list1.extend(list2)
#merged lists' values multiplied by 2
list1=[a*2 for a in list1]
for i in range(len(list1)):
    print(type(list1[i]))