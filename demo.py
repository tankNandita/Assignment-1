import csv

def createLeague(csv_file,str_1,str_2):
    count = 0
    lines = 0
    c_str_1 = 0
    c_str_2 = 0
    with open(csv_file, 'r') as csvFile:
        csvReader = csv.reader(csvFile)
        next(csvReader)

        for line in csvReader:
            lines += 1 
            #print(line[0])
            i = line[0].split(",")
            #print(i)
            if str_1 in i:
                c_str_1 += 1
                if str_2 in i:
                    count += 1
                    print(i , count)
            if str_2 in i:
                c_str_2 += 1
    if (count != 0):
        support = count / lines
        confidence = count / c_str_1
        lift_ratio = (count/c_str_1)/(c_str_2/lines)
        print("support = [ ",support," ], confidence = [ ",confidence," ], lift ratio= [ ",lift_ratio," ]")
    else:
        print("no match found")
    return

product_list=['MILK','BREAD','BISCUIT','CORNFLAKES','TEA','BOURNVITA','JAM','MAGGI','COFFEE','COCK','SUGAR']
print('enter product from list')
print(product_list)
st_1 = input("1. enter product name: ")
st_2 = input("2. enter product name: ")
data = createLeague('GroceryStoreDataSet.csv', st_1, st_2)
