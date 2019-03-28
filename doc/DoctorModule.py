import json
import matplotlib.pyplot as plt
import numpy as np
import os


THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

def openfile(file_name):
    with open(file_name,'r') as f:
        r= json.load(f)
        return r

def count_entry(obj):
    count = len(obj['doc'])
    return count
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

# Insert Node
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the Tree
    # def PrintTree(self):
    #     data= openfile(os.path.join(THIS_FOLDER, 'database.json'))
    #     count=count_entry(data)
    #     if self.left:
    #         self.left.PrintTree()
    #     a=self.data
    #     for i in range(0,count):
    #         if(a== data['doc'][i]['Pr']):
    #             print("Designation:\t",data['doc'][i]['Position']),
    #             print("Name:\t",data['doc'][i]['Name']),
    #     if self.right:
    #         self.right.PrintTree()

# Preorder traversal
# Root -> Left ->Right
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

def plot_graph(mon,tue,wed,thu,fri,sat,sun):
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    y = [mon,tue,wed,thu,fri,sat,sun]
    #tick_label = ['Monday','Tuesday', 'Wednesday' ,'Thursday' ,'Friday' ,'Saturday',' Sunday']
    plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)
    plt.ylim(1,20)
    plt.xlim(1,20)
    plt.xlabel("Days")
    plt.ylabel("Average Patient Count")
    plt.title("Work Schedule")
    # plt.show()

def dept_details(b,count):
    new= openfile(os.path.join(THIS_FOLDER, 'database.json'))
def doc_details(a,count):
    new= openfile(os.path.join(THIS_FOLDER, 'database.json'))
    for i in range(0,count):
        if(i==a):
            ident= new['doc'][i]['ID']
            name= new['doc'][i]['Name']
            qual= new['doc'][i]['Qualification']
            field= new['doc'][i]['Field']
            fee= new['doc'][i]['Fee']
            rank = new['doc'][i]['Rank']
            time=new['doc'][i]['Timing']
            mon=new['doc'][i]['Avg-Mon']
            tue=new['doc'][i]['Avg-Tue']
            wed=new['doc'][i]['Avg-Wed']
            thu=new['doc'][i]['Avg-Thu']
            fri=new['doc'][i]['Avg-Fri']
            sat=new['doc'][i]['Avg-Sat']
            sun=new['doc'][i]['Avg-Sun']
    print(mon,tue,wed,thu,fri,sat,sun)
    print("ID",ident,"\nName",name,"\nQualification",qual,"\nTimings",time,"\nField",field,"\nFee",fee)
    print("\n Work Schedule")
    x = [ 0, 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    y = [0,mon,tue,wed,thu,fri,sat,sun]
    #tick_label = ['Monday','Tuesday', 'Wednesday' ,'Thursday' ,'Friday' ,'Saturday',' Sunday']
    plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)
    plt.ylim(1,15)
    plt.xlim(1,8)
    plt.xlabel("Days")
    plt.ylabel("Average Patient Count")
    plt.title("Work Schedule")
    # plt.show()
    context = {
        "id":ident,
        "name":name,
        "field":field,
        "qualification":qual,
        "rank":rank,
        "timings":time,
        "fee":fee,
    }
    return context





def doc_select(name):
    flag=-1
    new= openfile(os.path.join(THIS_FOLDER, 'database.json'))
    count=count_entry(new)
    context = {}
    # name=input("Enter the name of the Doctor you want to select")
    for i in range(0,count):
        if(new['doc'][i]['Name']==name):
            # print("Doctor Found!")
            pos=i
            flag=0
            context =doc_details(pos,count)
            break

    return context


def dept_select(opt, sec):
     new= openfile(os.path.join(THIS_FOLDER, 'database.json'))
     count=count_entry(new)
    #  print("\n Departments available")
    #  print("\n 1. Board \n 2. Doctors \n 3. Staff \n 4. View Hospital Hierarchy")
    #  opt=int(input())
     sec = int("100"+str(sec))
     print(sec)
     if opt==1:
         dict_board = {}
         k=1
         for i in range(0,count):
             if(new['doc'][i]['Position']=='Board'):
                j=i
                name= new['doc'][j]['Name']
                qual= new['doc'][j]['Qualification']
                des= new['doc'][j]['Designation']
                exp= new['doc'][j]['Experience']
                # print(" Name:\t",name,"\n","Qualifications:\t ",qual,"\n","Designation:\t",des,"\n","Experience:\t",exp,"\n","\n")
                temp = {k: {'name':name, 'qual':qual, 'des':des, 'exp':exp}}
                k+=1
                dict_board.update(temp)
         return dict_board

     elif opt==2:
         print("Code\tDept Name \n  1001\tCardiology \n  1002\tDermatology \n  1003\tGynaecology \n  1004\tOncology \n  1005\tHematology\n  1006\tNeurology\n \n")
         print("Enter the code to number for more information about department")
        #  inpt=int(input())
         dict_doc = {}
         k=1
         for i in range(0,18):
             a=new['doc'][i]['Code']
             if(a==sec):
                 print("reached")
                 name = (new['doc'][i]['Name'])
                 rank = (new['doc'][i]['Rank'])
                 fee = new['doc'][i]['Fee']
                 timing = new['doc'][i]['Timing']
                 dict_doc.update({k:{'name': name, 'rank': rank, 'fee':fee, 'timing':timing}})
                 k+=1
         print(dict_doc)
         return dict_doc

     elif opt==3:
         dict_staff = {}
         k = 1
         for i in range(0,count):
             if(new['doc'][i]['Position']=='Staff'):
                j=i

                name= new['doc'][j]['Name']
                qual= new['doc'][j]['Qualification']
                des= new['doc'][j]['Designation']
                exp= new['doc'][j]['Experience']
                temp = {k: {'name':name, 'qual':qual, 'des':des, 'exp':exp}}
                k+=1
                dict_staff.update(temp)
         return dict_staff


    #  elif opt==4:
    #       root.PrintTree()

     else:
         print("Naaah")




if __name__ == "__main__":
    data= openfile(os.path.join(THIS_FOLDER, 'database.json'))
    count=count_entry(data)
    root = Node(15)
    for i in range(1,count):
        a=data['doc'][i]['Pr']
        root.insert(a)

    #print(root.PreorderTraversal(root))
    print("------------WELCOME TO THE DOCTOR DATABASE------------------")
    while(1):
         print("Please choose your option:")
         print("1. Select A Doctor \n2. Select A Department \n3. Go back to Home")
         opt=int(input())
         if opt==1:
             doc_select()
         elif opt==2:
             dept_select(3, 1)
         elif opt==3:
             exit()
