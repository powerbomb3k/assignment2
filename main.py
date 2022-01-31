file = open('example1.txt', 'r')



#created a list for coordinates
co_ordiantes = []
#a for loop for inputing the co_ordinates into a list
for i in file:
    co_ordiantes.append(i.strip())
#print(co_ordiantes)
file.close()


for j in co_ordiantes:
    # origin acts as the base of the graph
    origin=[0,0]
    for i in j:
        if i == 'N':
            origin[1]+=1
        elif i == 'E':
            origin[0]+=1
        elif i == 'S':
            origin[1]-=1
        elif i == 'W':
            origin[0]-=1
    print(origin)



