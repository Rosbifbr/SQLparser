#parser de pseudococo para sql made by rodrigao gostosao
inps= open("insert.txt", "r")
outs= open("output.sql", 'w+')
f1 = inps.readlines()
for x in f1:
    if 'referencia' in x:
        if not('referencia' in f1[f1.index(x)+1]):
            outs.write("FOREIGN KEY (" + x[:x.find('referencia')] + ') REFERENCES' + x[x.find('referencia')+10:len(x)-1] + '\n')
            outs.write(");\n")
        else:
            outs.write("FOREIGN KEY (" + x[:x.find('referencia')] + ') REFERENCES' + x[x.find('referencia')+10:len(x)-1] + ',\n')
    elif '(' in x:
        outs.write("CREATE TABLE " + x[0:x.find('(')] + '\n')
        outs.write("( \n") #Create Table Header
        
        pos=x.find('(') #Prints mentioned columns of types not null, last one and normal. Also closes parenthesis.
        while pos != -1:
            column = x[pos+1:x.find(',', pos+1)]
            if '*' in column and ')' in column:
                newcoll = x[pos+1:x.find(')', pos)]
                newcoll = newcoll.replace('*','')
                outs.write(newcoll + ' DATATYPE NOT NULL')
            
            elif '*' in column:
                newcoll = x[pos+1:x.find(',', pos+1)]
                newcoll = newcoll.replace('*','')
                outs.write(newcoll + ' DATATYPE NOT NULL,\n')
            
            elif ')' in column:
                if not ('referencia' in f1[f1.index(x)+1]):
                    outs.write(x[pos+1:x.find(')')] + ' DATATYPE\n')
                else:
                    outs.write(x[pos+1:x.find(')')] + ' DATATYPE,\n')
            else:
                outs.write(x[pos+1:x.find(',', pos+1)] + ' DATATYPE,\n')
            pos=x.find(',', pos+1) #prints column with DATATYPE to be replaced by actual datatype
        if not('referencia' in f1[f1.index(x)+1]):
            outs.write("\n);\n")
print("Done!")
        