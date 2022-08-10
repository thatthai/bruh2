print("*** Converting hh.mm.ss to seconds ***")
time = input("Enter hh mm ss : ")
l = time.split()

#covert to second
second = (int(l[0]) * 60 * 60) + (int(l[1]) * 60) + int(l[2])

#case
if int(l[1]) > 59 or int(l[1]) < 0 :
    print("mm(" + str(l[1]) + ") is invalid!")
elif int(l[2]) > 59 :
    print("ss(" + str(l[2]) + ") is invalid!")
else :
    #hh:mm:ss = ...... seconds
    #print("%02d : %02d : %02d" + " = " + '{:,}'.format(second) + " seconds" %(int(l[0]),int(l[1]),int(l[2])))
    print("%02d:%02d:%02d" % (int(l[0]),int(l[1]),int(l[2])), end = " = ")
    print('{:,}'.format(second) +  " seconds")