#############################################################################################################
### CGPA Calculator 
### author : M.himamsu
### Created on 31/01/2019 
### this application helps to estimate the cgpa 
####################################################################################################3




def dgrades():#Dispalys min grade points
    print('group \t points \n');
    print('O \t 9')
    print('A++ \t 8')
    print('A+ \t 7')
    print('A \t 6')
    print('B+ \t 5.5')
    print('B \t 5')
    print('C+ \t 4.5')
    print('C \t 4.1')
    print('D \t 4')
def calc(l):
    sg=float(0)
    cre=0
    for j in range(len(l)):
        cre+=l[j][1]
        sg+=(l[j][1]*l[j][0])
    sg=sg/cre
#    lmm=[]
#    lmm.append(sg)
#    lmm.append(cre)
#    return lmm
    return (sg,cre)
print('Welcome to GPA Calculator')
n=int(input('input the number of semisters that you got results for? and press Enter key \n'))#number of sems
if n>8:
    while 1: 
        print('Invalid Semisters')
    
sem=[] #list of lists that has [cgpa, sem credits]
print("Great!\n")
for i in range(n):
    print('\nWelcome to '+str(i+1)+'th semister')
    pas=int(input('if u have passed all the subjects of '+str(i+1)+'th sem Enter 1 if passed enter 0 if fail in any subject of the sem\n'))
    if pas:#cgpa for passed semisters
        tem=[]
        tem.append(float(input('The Total SGPA of the sem\n')))
        tem.append(int(input('total no of credits of the sem\n')))
        sem.append(tem)
    else:#cgpa calculator for failed semisters
        ns=int(input('Enter number of subjects in the semister?(labs are also considired as subjects)\n'))#number of subjects in a sem
        ls=[]#list of lists that has [marks and credits of a subject]
        for j in range(ns):
            
            tls=[]
            dgrades()
            print('Enter details of '+str(j+1)+'th subject')
            tls.append(float(input('please enter the points according to the grade and if this is the fail subject enter the least grade 4\n ')))
            tls.append(int(input('number of credits for this subject\n')))
            ls.append(tls)
        semf=list(calc(ls))
        sem.append(semf)
        print("\n")
        #print("this semisters Sgpa is "+str(sem[i][0]))
xyz=calc(sem)
print("Your final CGPA for the "+str(n)+" semisters can be minimum of "+str(xyz[0]) )
        
        
        
        
        
        
        
        
