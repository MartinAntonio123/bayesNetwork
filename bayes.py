from Tkinter import *
import ttk

smokev = { 'T' : 0.2, 'F' : 0.8}
coldv = { 'T' : 0.02, 'F' : 0.98}
smoke_lungd = { 'T' : {'T' : 0.1009, 'F' : 0.8991}, 'F' : {'T' : 0.001, 'F' : 0.999}}
lungd_sbreath = { 'T' : {'T' : 0.208, 'F' : 0.792}, 'F' : {'T' : 0.01, 'F' : 0.99}}
lungd_chestp = { 'T' : {'T' : 0.208, 'F' : 0.792}, 'F' : {'T' : 0.01, 'F' : 0.99}}
cold_fever = { 'T' : {'T' : 0.307, 'F' : 0.693}, 'F' : {'T' : 0.01, 'F' : 0.99}}
lungd_cold_cough = {'T':{'T':{'T':0.7525,'F':0.2475},'F':{'T':0.505,'F':0.495}},'F':{'T':{'T':0.505,'F':0.495},'F':{'T':0.01,'F':0.99}}}

root = Tk()
root.title("Bayes network")

def get_var(entry, table):
    if entry == "":
        res = []
        for item in table.keys():
            print item
            res.append(table[item])
        return res
    else:
        res = []
        for item in table.keys():
            if item==entry:
                res.append(table[item])
        return res

def get_var_2(entry, entry2, table):
    if entry2 == "":
        if entry == "":
            res = []
            for item in table.keys():
                for item2 in table[item].keys():
                    res.append(table[item][item2])
            return res
        else:
            res = []
            for item in table.keys():
                for item2 in table[item].keys():
                    if item2==entry:
                        res.append(table[item][item2])
            return res
    else:
        if entry == "":
            res = []
            for item in table.keys():
                if item==entry2:
                    for item2 in table[item].keys():
                        res.append(table[item][item2])
            return res
        else:
            res = []
            for item in table:
                if item==entry2:
                    for item2 in table[item].keys():
                        if item2==entry:
                            res.append(table[item][item2])
            return res

def get_var_3(entry, entry2,entry3, table):
    if entry3 == "":
        if entry2 == "":
            if entry == "":
                res = []
                for item in table.keys():
                    for item2 in table[item].keys():
                        for item3 in table[item][item2].keys():
                            res.append(table[item][item2][item3])
                return res
            else:
                res = []
                for item in table.keys():
                    for item2 in table[item].keys():
                        for item3 in table[item][item2].keys():
                            if item3==entry:
                                res.append(table[item][item2][item3])
                return res
        else:
            if entry == "":
                res = []
                for item in table.keys():
                    for item2 in table[item].keys():
                        if item2 == entry2:
                            for item3 in table[item][item2].keys():
                                res.append(table[item][item2][item3])
                return res
            else:
                res = []
                for item in table.keys():
                    for item2 in table[item].keys():
                        if item2 == entry2:
                            for item3 in table[item][item2].keys():
                                if item3 == entry:
                                    res.append(table[item][item2][item3])
                return res
    else:
        if entry2 == "":
            if entry == "":
                res = []
                for item in table.keys():
                    if item == entry3:
                        for item2 in table[item].keys():
                            for item3 in table[item][item2].keys():
                                res.append(table[item][item2][item3])
                return res
            else:
                res = []
                for item in table.keys():
                    if item == entry3:
                        for item2 in table[item].keys():
                            for item3 in table[item][item2].keys():
                                if item3==entry:
                                    res.append(table[item][item2][item3])
                return res
        else:
            if entry == "":
                res = []
                for item in table.keys():
                    if item == entry3:
                        for item2 in table[item].keys():
                            if item2 == entry2:
                                for item3 in table[item][item2].keys():
                                        res.append(table[item][item2][item3])
                return res
            else:
                res = []
                for item in table.keys():
                    if item == entry3:
                        for item2 in table[item].keys():
                            if item2 == entry2:
                                for item3 in table[item][item2].keys():
                                    if item3 == entry:
                                        res.append(table[item][item2][item3])
                return res

def sum_mult7(array1,array2,array3,array4,array5,array6,array7):
    total = 0
    for i in array1:
        for j in array2:
            for k in array3:
                for l in array4:
                    for m in array5:
                        for n in array6:
                            for o in array7:
                                total = total + (i*j*k*l*m*n*o)
    return total

def sum_mult6(array1,array2,array3,array4,array5,array6):
    total = 0
    for i in array1:
        for j in array2:
            for k in array3:
                for l in array4:
                    for m in array5:
                        for n in array6:
                            total = total + (i*j*k*l*m*n)
    return total

def generateProbabilities():
    smoke = get_var(entry_1.get(), smokev)
    lungd = get_var_2(entry_2.get(), entry_1.get(), smoke_lungd)
    sbreath = get_var_2(entry_3.get(), entry_2.get(), lungd_sbreath)
    chestp = get_var_2(entry_4.get(), entry_2.get(), lungd_chestp)
    cough = get_var_3(entry_5.get(), entry_2.get(), entry_6.get(), lungd_cold_cough)
    cold = get_var(entry_6.get(), coldv)
    fever = get_var_2(entry_7.get(), entry_6.get(), cold_fever)

    smoke_true = get_var("T", smokev)
    lungd_true = get_var_2("T", entry_1.get(), smoke_lungd)
    sbreath_true = get_var_2("T", entry_2.get(), lungd_sbreath)
    chestp_true = get_var_2("T", entry_2.get(), lungd_chestp)
    cough_true = get_var_3("T", entry_2.get(), entry_6.get(), lungd_cold_cough)
    cold_true = get_var("T", coldv)
    fever_true = get_var_2("T", entry_6.get(), cold_fever)
    
    print smoke, lungd, sbreath, chestp, cough, cold, fever
    total_smoke = sum_mult7(smoke_true,lungd,sbreath,chestp,cough,cold,fever)/sum_mult6(lungd,sbreath,chestp,cough,cold,fever)
    total_lungd = sum_mult7(smoke,lungd_true,sbreath,chestp,cough,cold,fever)/sum_mult6(smoke,sbreath,chestp,cough,cold,fever)
    total_sbreath = sum_mult7(smoke,lungd,sbreath_true,chestp,cough,cold,fever)/sum_mult6(smoke,lungd,chestp,cough,cold,fever)
    total_chestp = sum_mult7(smoke,lungd,sbreath,chestp_true,cough,cold,fever)/sum_mult6(smoke,lungd,sbreath,cough,cold,fever)
    total_cough = sum_mult7(smoke,lungd,sbreath,chestp,cough_true,cold,fever)/sum_mult6(smoke,lungd,sbreath,chestp,cold,fever)
    total_cold = sum_mult7(smoke,lungd,sbreath,chestp,cough,cold_true,fever)/sum_mult6(smoke,lungd,sbreath,cough,chestp,fever)
    total_fever = sum_mult7(smoke,lungd,sbreath,chestp,cough,cold,fever_true)/sum_mult6(smoke,lungd,sbreath,cough,chestp,cold)
    if entry_1.get() == "":
        entry_1.insert(0,total_smoke)
    if entry_2.get() == "":
        entry_2.insert(0,total_lungd)
    if entry_3.get() == "":
        entry_3.insert(0,total_sbreath)
    if entry_4.get() == "":
        entry_4.insert(0,total_chestp)
    if entry_5.get() == "":
        entry_5.insert(0,total_cough)
    if entry_6.get() == "":
        entry_6.insert(0,total_cold)
    if entry_7.get() == "":
        entry_7.insert(0,total_fever)
    print("---------------")

def clearProb():
    entry_1.delete(0, END)
    entry_2.delete(0, END)
    entry_3.delete(0, END)
    entry_4.delete(0, END)
    entry_5.delete(0, END)
    entry_6.delete(0, END)
    entry_7.delete(0, END)


label_1 = Label(root,text=" Smokes ")
label_2 = Label(root,text=" Lung disease ")
label_3 = Label(root,text=" Shortness of breath ")
label_4 = Label(root, text = " Chest pain ")
label_5 = Label(root, text = " Cough ")
label_6 = Label(root, text = " Cold ")
label_7 = Label(root, text = " Fever ")
label_1.grid(row=0,column=0, padx=10, pady=10)
label_2.grid(row=1,column=0, padx=10, pady=10)
label_3.grid(row=2,column=0, padx=10, pady=10)
label_4.grid(row=3,column=0, padx=10, pady=10)
label_5.grid(row=4,column=0, padx=10, pady=10)
label_6.grid(row=5,column=0, padx=10, pady=10)
label_7.grid(row=6,column=0, padx=10, pady=10)

entry_1=Entry(root)
entry_2=Entry(root)
entry_3=Entry(root)
entry_4=Entry(root)
entry_5=Entry(root)
entry_6=Entry(root)
entry_7=Entry(root)
entry_1.grid(row=0,column=1, padx=10, pady=10)
entry_2.grid(row=1,column=1, padx=10, pady=10)
entry_3.grid(row=2,column=1, padx=10, pady=10)
entry_4.grid(row=3,column=1, padx=10, pady=10)
entry_5.grid(row=4,column=1, padx=10, pady=10)
entry_6.grid(row=5,column=1, padx=10, pady=10)
entry_7.grid(row=6,column=1, padx=10, pady=10)


button_1=Button(root, text="Calculate", command=generateProbabilities)

button_1.grid(row=1,column=2, padx=10, pady=10)

button_2=Button(root, text="Reset", command=clearProb)
button_2.grid(row=3,column=2, padx=10, pady=10)

root.minsize(400,400)
root.mainloop()
