def hash_function(key):
    k=len(key)
    hv=0
    for i in range(k):
        hv=(hv<<5)+hv+ord(key[i])
    hv=hv%10
    return hv

store={}
book=['isbn','author','title','price','subject']
book_dic={'isbn':{1:[],0:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]},
     'author':{1:[],0:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]},
     'title':{1:[],0:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]},
     'price':{1:[],0:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]},
     'subject':{1:[],0:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}}

sale=['uid','no','isbn_no']
sale_dic={'uid':{1:[],0:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]},
     'no':{1:[],0:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]},
     'isbn_no':{1:[],0:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}}

file=open('books.txt','r',encoding='UTF-8')
file1=open('sellRecord.txt','r',encoding='UTF-8')
x=file.read()
x1=file1.read()
x=x.replace('*/','')
x=x.replace('/*','')
x1=x1.replace('*/','')
x1=x1.replace('/*','')
y=x.split('\n')
y1=x1.split('\n')
del y[0]
del y1[0]

i=0
while y[i] != '':
    z=y[i].split('|')
    j=0
    store[z[0]]=z
    for j in range(len(z)):
        a=hash_function(z[j])
        book_dic[book[j]][a].append(z[0])
    i+=1
    
i=0
while y1[i] != '':
    z=y1[i].split('|')
    j=0
    store[z[2]]+=z
    for j in range(len(z)):
        a=hash_function(z[j])
        sale_dic[sale[j]][a].append(z[0])
    i+=1
       
    
for i in book_dic:
    file=open((i+'.txt'),'w',encoding='UTF-8')
    for x in book_dic[i]:
        file.write(str(x)+"：")
        for y in book_dic[i][x]:
            file.write(str(y)+" ")
        file.write("\n")

#print (book_dic)
#print(store)

file.close()

