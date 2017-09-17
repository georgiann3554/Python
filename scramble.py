import random
fhand=open("input.txt")
fin=fhand.read()
fhand2=open("output.txt",'w')

words=fin.split()
listt=[]
punc=[",",".","?","!",";"]

def scramble(i):
    newword=""
    newword2=""
    listt2=[]
    if i[len(i)-1] in punc:
        
        count=(len(i)-3)
    
        while(count is not 0):
           x=random.randrange(1,(len(i)-2))
           if x  not in  listt2:
              newword=newword+i[x]
              listt2.append(x)
              count-=1
           newword2=i[0]+newword+i[len(i)-2]+i[len(i)-1]
    else:
        count=(len(i)-2)
        while(count is not 0):
           x=random.randrange(1,(len(i)-1))
           if x  not in  listt2:
              newword=newword+i[x]
              listt2.append(x)
              count-=1
           newword2=i[0]+newword+i[len(i)-1]

    return newword2
      
print(words)
for i in words:
  
  if(len(i)<=3):
      listt.append(i)
  else:
      scr=scramble(i)
      listt.append(scr)
print(listt)
str1 = ' '.join(listt)
fhand2.write(str1)
fhand2=open("output.txt",'r')

fin2=fhand2.read()
print(fin2)
           
     
  


    
