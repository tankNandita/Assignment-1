import csv

product_list = ['MILK','BREAD','BISCUIT','CORNFLAKES','TEA','BOURNVITA','JAM','MAGGI','COFFEE','SUGAR','FLOUR','OIL','HONEY','COFFY']

def analyseFile(csv_file, min_support):
    global product_list
    with open(csv_file, 'r') as csvFile:
        csvReader = csv.reader(csvFile)
        next(csvReader)

        compare2list = []
        
        for i in range(0, len(product_list)):
            for j in range(0, len(product_list)):
                if [i, j] in compare2list or [j, i] in compare2list:
                    None
                else:
                    if i!=j:
                        compare2list.append([i, j])
        print(compare2list)

        for i in range(0, len(compare2list)):
            compare2list[i].append(0)
        
        for line in csvReader:
            i = 0
            for products in compare2list:
                if product_list[products[0]] in line and product_list[products[1]] in line:
                    compare2list[i][2] += 1
                i+=1

        for [product1, product2, count] in compare2list:
            print(product_list[product1]," & ",product_list[product2]," : ",count)

        print("====================================\nAFTER POPPING\n====================================")
        
        toBePopped = []
        for3numbers = []

        for i in range(0, len(compare2list)):
            if(compare2list[i][2] < min_support):
                toBePopped.append(i)
            else:
                if not compare2list[i][0] in for3numbers:
                    for3numbers.append(compare2list[i][0])
                elif not compare2list[i][1] in for3numbers:
                    for3numbers.append(compare2list[i][1])
                print(product_list[compare2list[i][0]]," & ",product_list[compare2list[i][1]]," : ",compare2list[i][2])

        for3numbers.sort()
        compare3list = []
        
        for index1 in for3numbers:
            for index2 in for3numbers:
                for index3 in for3numbers:
                    if index1 != index2 and index2 != index3 and index3 != index1:
                        if [index1, index2, index3] in compare3list or [index1, index3, index2] in compare3list or [index2, index1, index3] in compare3list or [index2, index3, index1] in compare3list or [index3, index2, index1] in compare3list or [index3, index2, index1] in compare3list:
                            None
                        else:
                            compare3list.append([index1, index2, index3])
        print("====================================\n3 ITEMS\n====================================")

        for i in range(0, len(compare3list)):
            compare3list[i].append(0)

        csvFile.seek(0)
        csvReader = csv.reader(csvFile)
        
        for line in csvReader:
            i = 0
            for products in compare3list:
                if product_list[products[0]] in line and product_list[products[1]] in line and product_list[products[2]] in line:
                        compare3list[i][3] += 1
                i+=1

        for [product1, product2, product3, count] in compare3list:
            print(product_list[product1]," & ",product_list[product2]," & ",product_list[product3]," : ",count)

        print("====================================\nAFTER POPPING\n====================================")
        
        toBePopped = []

        for i in range(0, len(compare3list)):
            if(compare3list[i][3] < min_support):
                toBePopped.append(i)
            else:
                print(product_list[compare3list[i][0]]," & ",product_list[compare3list[i][1]]," & ",product_list[compare3list[i][2]]," : ",compare3list[i][3])
    
print("LIST OF AVAILABLE PRODUCTS:")
print(product_list)

min_support = int(input("Enter Min Support: "));

data = analyseFile('GroceryStoreDataSet.csv', min_support)
