import csv

class Record:
    def __init__(self,row):
        self.__dict__ = row

    def __eq__(self, __value: object) -> bool:
        if (__value.lastname != self.lastname) or \
            (__value.name != self.name) or \
            (__value.patronymic != self.patronymic) or \
            (__value.date_of_birth != self.date_of_birth):
            return False
        return True


class Tree:
    def __init__(self,id) -> None:
        self._id = id
        self.children = []

    @property
    def id(self):
        return self._id
    
    def add_child(self, child: Record):
        if not self.children:
            self.children.append(child)
        else:
            n = 0
            for current_child in self.children:
                if current_child != child:
                    n+=1
            if n == len(self.children):
                self.children.append(child)


    

f_file = csv.DictReader(open('f.csv','r',encoding='utf-8'),delimiter='|')

unic = {}


for row in f_file:
    if not unic.get(row['id']):
        t = Tree(row['id'])
        t.add_child(Record(row))
        unic[row['id']] = t
    else:
        unic[row['id']].add_child(Record(row))

for i in unic.keys():
    print(i,len(unic[i].children))
    write_csv = csv.DictWriter(open(i+'_csv.csv','w',encoding='utf-8',newline=''),unic[i].children[0].__dict__.keys(),delimiter='|')
    write_csv.writeheader()
    for j in unic[i].children:
        write_csv.writerow(j.__dict__)
