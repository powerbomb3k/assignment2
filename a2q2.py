#name: Suchetanbir singh bhangu
#NSID: sub412
#student Number: 11299684
#course Number: cmpt 145
#lecture section: 02


file = open('example1.txt', 'r')

#created a list for coordinates
co_ordiantes = []
#a for loop for inputing the co_ordinates into a list
for i in file:
    co_ordiantes.append(i.strip())
#print(co_ordiantes)
file.close()

#this for loop goes through the list
for j in co_ordiantes:
    # origin acts as the base of the graph
    origin=[0,0]
    # This for loop goes through the individual index of the list
    for i in j:
        if i == 'N':
            origin[1]+=1
        elif i == 'E':
            origin[0]+=1
        elif i == 'S':
            origin[1]-=1
        elif i == 'W':
            origin[0]-=1
    #printing the output in co_ordinate form
    print(tuple(origin))



