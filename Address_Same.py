import csv

ls = []
with open('Nature_Com_Art_From(2.14).csv',"r") as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        #print(row)
        ls.append(row)

    #print("\n")
    #print(ls[0][1])
with open('csvTest_final.csv',"w",newline='',encoding="utf-8_sig") as csvfile:
    writer = csv.writer(csvfile)
    i = 0
    for i in range(0,39970):

        if int(ls[i][1]) == 2:
            Title = ls[i][0]
            Num = ls[i][1]
            Source1 = ls[i][2]
            Source2 = ls[i+1][2]
            #ls_New = [Title,Num,Source1,Source2]
            #print(ls_New)
            writer.writerow([Title,Num,Source1,Source2])
            i += 2

        elif int(ls[i][1]) == 3:
            Title = ls[i][0]
            Num = ls[i][1]
            Source1 = ls[i][2]
            Source2 = ls[i+1][2]
            Source3 = ls[i+2][2]
            writer.writerow([Title, Num, Source1, Source2,Source3])
            i += 3

        elif int(ls[i][1]) == 4:
            Title = ls[i][0]
            Num = ls[i][1]
            Source1 = ls[i][2]
            Source2 = ls[i+1][2]
            Source3 = ls[i+2][2]
            Source4 = ls[i+3][2]
            writer.writerow([Title, Num, Source1, Source2,Source3,Source4])
            i += 4

        elif int(ls[i][1]) == 1:
            Title = ls[i][0]
            Num = ls[i][1]
            Source1 = ls[i][2]
            writer.writerow([Title, Num, Source1])
            i += 1