import numpy as np
def rearange(Pn, length, idx):
    file = open("temp.txt","r")
    Crn_1 = file.readline()
    Crn_1 = Crn_1.replace("'","")
    Crn_1 = Crn_1.replace("[","")
    Crn_1 = Crn_1.replace("]","")
    Crn_1 = Crn_1.split(",")
    file.close()
    Crn = Pn
    lnth = len(Crn_1)
    print("Pn = "+str(Pn))
    print("Crn_1 = "+str(Crn_1))
    if(len(Crn_1)>len(Pn)):
        Crn_1[len(Crn_1)-1] = ""
        lnth = lnth - 1
    if (len(Pn)>len(Crn_1)):
        Crn_1.extend('0 0')
    if (idx != 0):
        Crn = Crn_1
        for i in range(lnth):
            Thr = 100000
            Pn_copy = Pn
            Crn_1_split = Crn_1[i].split()
            for j in range(length):
                Pn_split = Pn[j].split()
                dif = np.sqrt(np.square(int(float(Pn_split[0]))-int(float(Crn_1_split[0]))) + np.square(int(float(Pn_split[1]))-int(float(Crn_1_split[1]))))
                #print("dif ="+str(dif))
                #print("unupadted Thr = "+str(Thr))
                if (  dif < Thr ):
                    Crn[i] = Pn[j]
                    #Pn[j] = '100000 100000', this is a really bad idea don't do this please
                    Thr = dif
                    #print("Thr updated = "+str(Thr))
            Pn = Pn_copy          
    file = open("temp.txt", "w")
    L = str(Crn)
    file.writelines(L)
    print("Crn = "+str(Crn))
    return Crn