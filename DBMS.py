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

attribute=['isbn','author','title','price','subject','uid','no','isbn_no']

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
        sale_dic[sale[j]][a].append(z[2])
    i+=1
       
#print(store)


for i in book_dic:
    file=open(('books_'+i+'.txt'),'w',encoding='UTF-8')
    for x in book_dic[i]:
        file.write("Bucket"+str(x)+"：")
        for y in book_dic[i][x]:
            file.write(str(y)+'：'+store[y][book.index(i)]+", ")
        file.write("\n")
    file.close()

for i in sale_dic:
    file=open(('sellRecord_'+i+'.txt'),'w',encoding='UTF-8')
    for x in sale_dic[i]:
        file.write("Bucket"+str(x)+"：")
        #print("Bucket"+str(x)+"：")
        for y in sale_dic[i][x]:
            file.write(str(y)+'：'+store[y][sale.index(i)+5]+", ")
            #print(str(y)+'：'+store[y][sale.index(i)+5]+", ")
        file.write("\n")
    file.close()

while True:
    sql=input('輸入sql語法：');
    sql=sql.strip()
    sql=sql.split(' ')
    input_hash=[]
    hash_ID=[]
    where_ans=''
    where_ans1=''
    where={}
    dis=False
    print (sql)

    if sql[1] == 'DISTINCT':
        del sql[1]
        dis=True
    output_dis=[]
    
    input_select=sql[1]
    input_from=sql[3]

    #處理table
    if len(sql)!=4:
        input_where=sql[5]
        
        input_from=input_from.split(',')
        input_select=input_select.split(',')
        
        for i in range(7,len(sql)):
            if sql[i] == 'AND':
                where_ans1=''
                input_where1=sql[i+1]
                for j in range(i+3,len(sql)):
                    where_ans1+=sql[j]
                    where_ans1+=" "
                break;
            where_ans+=sql[i]
            where_ans+=" "
            where_ans1=where_ans
            input_where1=input_where
            
        where_ans=where_ans.strip()
        where_ans1=where_ans1.strip()
        
        where[input_where]=where_ans
        where[input_where1]=where_ans1
                
        hash_ID=[]
        ID=[]
        
        for y in where:
            if y in book_dic:
                for x in book_dic[y][hash_function(where[y])]:
                    if store[x][attribute.index(y)] == where[y]:
                        hash_ID.append(x)
            if y in sale_dic:
                for x in sale_dic[y][hash_function(where[y])]:
                    if store[x][attribute.index(y)] == where[y]:
                        hash_ID.append(x)

        for x in hash_ID:
            if hash_ID.count(x) > 1:
                ID.append(x)
        
        hash_ID=list(set(ID))
        #print(ID)
        print(hash_ID)
                     
        for y in input_from:
            if y == 'books':
                for x in input_select:
                    if x in book:
                        if dis == True:
                            output_dis.append(x)
                        else:
                            print(x)
                        for a in hash_ID:
                            if dis == True:
                                output_dis.append(store[a][attribute.index(x)])
                            else:
                                print(store[a][attribute.index(x)])
                    
            if y == 'sellRecord':
                for x in input_select:
                    if x in sale:
                        if dis == True:
                            output_dis.append(x)
                        else:
                            print(x)
                        for a in hash_ID:
                            if dis == True:
                                output_dis.append(store[a][attribute.index(x)])
                            else:
                                print(store[a][attribute.index(x)])
                
            
    if len(sql)==4:
        input_from=input_from.split(',')
        input_select=input_select.split(',')
        for y in input_from:
            if y == 'books':
                if input_select[0] == '*':
                    for count in range(5):
                        if dis == True:
                            output_dis.append(book[count])
                        else:
                             print(book[count])
                        for z in store:
                            if dis == True:
                                output_dis.append(store[z][count])
                            else:
                                print (store[z][count])
                else:
                    for a in input_select:
                        if a in book:
                            index=book.index(a)
                            if dis == True:
                                output_dis.append(a)
                            else:
                                print(a)
                            for z in store:
                                if dis == True:
                                    output_dis.append(store[z][index])
                                else:
                                    print(store[z][index])
                                
            if y == 'sellRecord':
                 if input_select[0] == '*':
                     for count in range(3):
                         if dis == True:
                                    output_dis.append(sale[count])
                         else:
                             print(sale[count])
                         for z in store:
                             if len(store[z]) > 5:
                                 if dis == True:
                                     output_dis.append(store[z][count+5])
                                 else:
                                     print(store[z][count+5])
                             if len(store[z]) > 8:
                                 if dis == True:
                                     output_dis.append(store[z][count+8])
                                 else:
                                     print(store[z][count+8])
                 else:
                     for a in input_select:
                         if a in sale:
                             index=sale.index(a)
                             if dis == True:
                                    output_dis.append(a)
                             else:
                                 print (a)
                             for z in store:
                                if len(store[z]) > 5:
                                    if dis == True:
                                        output_dis.append(store[z][index])
                                    else:
                                        print(store[z][index])

    #print(output_dis)
    
    output=list(set(output_dis))

    
    
    output.sort(key=output_dis.index)
    print(output)
    for i in range(len(output)):
        print (output[i])
    
    
        
            
#print (book_dic)


file.close()

