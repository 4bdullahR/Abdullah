class read:
    def __init__(self, name, number, email, numOfBooks):
        self.name = name
        self.email = email
        self.number = number
        self.__numOfBooks = numOfBooks 
        self.__counter = 0  #for indexing
        self.books = []
        self.catg = []  #empty arrays/listes
        self.pages = []

    def getNumOfBooks(self):
        return self.__numOfBooks

    def addBooks(self, name, catg, pages):
            self.books.insert(self.__counter, name)
            self.catg.insert(self.__counter, catg)  #adding elements to the empty list
            self.pages.insert(self.__counter, pages)
            self.__counter += 1

    def getAllPages(self): #all pages an object read
        sum = 0
        for x in self.pages:
            sum += x
        return sum 

    def countHistory(self):
        counter = 0
        for x in self.catg:
            if x.lower() == 'history':
                counter += 1
        return counter

    def countStory(self):
        counter = 0
        for x in self.catg:
            if x.lower() == 'story':
                counter += 1
        return counter
            
    def countScientist(self):
        counter = 0
        for x in self.catg:
            if x.lower() == 'scientist':
                counter += 1
        return counter      

    def countReligious(self):
        counter = 0
        for x in self.catg:
            if x.lower() == 'religious':
                counter += 1
        return counter

    def countLiterature(self):
        counter = 0
        for x in self.catg:
            if x.lower() == 'literature':
                counter += 1
        return counter

    def countOthers(self):
        counter = 0
        for x in self.catg:
            if x.lower() != 'history' and x.lower() != 'story' and x.lower() != 'scientist' and x.lower() != 'religious' and x.lower() != 'literature':
                counter += 1
        return counter


def add_all(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10): #can be used to add all everyones' pages also count everyones' catagories
    return i1+i2+i3+i4+i5+i6+i7+i8+i9+i10

def printMostBooks(name1, books1, name2, books2, name3, books3, name4, books4, name5, books5,
             name6, books6, name7, books7, name8, books8, name9, books9, name10, books10):
    biggest = books1
    BIGGEST = name1

    if biggest < books2:
     biggest = books2
     BIGGEST = name2
    if biggest < books3:
        biggest = books3
        BIGGEST = name3
    if biggest < books4:
     biggest = books4
     BIGGEST = name4
    if biggest < books5:
        biggest = books5
        BIGGEST = name5
    if biggest < books6:
     biggest = books6
     BIGGEST = name6
    if biggest < books7:
        biggest = books7
        BIGGEST = name7
    if biggest < books8:
     biggest = books8
     BIGGEST = name8
    if biggest < books9:
        biggest = books9
        BIGGEST = name9
    if biggest < books10:
     biggest = books10
     BIGGEST = name10
    
    print("The one who read books the most is",BIGGEST,"by", biggest,"books.")  

def printMostCatg(history, story, scientist, religious, literature, other):
    biggest = history
    BIGGEST = 'history'

    if biggest < story:
     biggest = story
     BIGGEST = 'story'
    if biggest < scientist:
        biggest = scientist
        BIGGEST = 'scientist' 
    if biggest < religious:
        biggest = religious
        BIGGEST = 'religious'
    if biggest < literature:
        biggest = literature
        BIGGEST = 'literature'
    if biggest < other:
        biggest = other
        BIGGEST = 'other'
    print("The most catagory was read is",BIGGEST,"by" , biggest,"books.")    

def printMostPages(name1, pages1, name2, pages2, name3, pages3, name4, pages4, name5, pages5,
             name6, pages6, name7, pages7, name8, pages8, name9, pages9, name10, pages10):
    biggest = pages1
    BIGGEST = name1

    if biggest < pages2:
     biggest = pages2
     BIGGEST = name2
    if biggest < pages3:
        biggest = pages3
        BIGGEST = name3
    if biggest < pages4:
     biggest = pages4
     BIGGEST = name4
    if biggest < pages5:
        biggest = pages5
        BIGGEST = name5
    if biggest < pages6:
     biggest = pages6
     BIGGEST = name6
    if biggest < pages7:
        biggest = pages7
        BIGGEST = name7
    if biggest < pages8:
     biggest = pages8
     BIGGEST = name8
    if biggest < pages9:
        biggest = pages9
        BIGGEST = name9
    if biggest < pages10:
     biggest = pages10
     BIGGEST = name10
    
    print("The one who read pages the most is",BIGGEST,"by", biggest,"pages.")  

def printSQ(string, num): # printing a schedule
 
    if len(string) < 7:        # counting how many letters to mange blanks ( \t )
     print(string,"\t\t", num)
    else:
     print(string,"\t", num)

#Taking input from the user
'''
obj1 = read(input('The name? '),input('Phone number? '), input('Email? '), int(input('Number of books he read? ')))
for x in range(obj1.getNumOfBooks()):
    obj1.addBooks(input('Book title? '), input('Its catagory? '), int(input('Its pages? ')))

obj2 = read(input('The name? '),input('Phone number? '), input('Email? '), int(input('Number of books he read? ')))
for x in range(obj2.getNumOfBooks()):
    obj2.addBooks(input('Book title? '), input('Its catagory? '), int(input('Its pages? ')))

obj3 = read(input('The name? '),input('Phone number? '), input('Email? '), int(input('Number of books he read? ')))
for x in range(obj3.getNumOfBooks()):
    obj3.addBooks(input('Book title? '), input('Its catagory? '), int(input('Its pages? ')))

obj4 = read(input('The name? '),input('Phone number? '), input('Email? '), int(input('Number of books he read? ')))
for x in range(obj4.getNumOfBooks()):
    obj4.addBooks(input('Book title? '), input('Its catagory? '), int(input('Its pages? ')))

obj5 = read(input('The name? '),input('Phone number? '), input('Email? '), int(input('Number of books he read? ')))
for x in range(obj5.getNumOfBooks()):
    obj5.addBooks(input('Book title? '), input('Its catagory? '), int(input('Its pages? ')))

obj6 = read(input('The name? '),input('Phone number? '), input('Email? '), int(input('Number of books he read? ')))
for x in range(obj6.getNumOfBooks()):
    obj6.addBooks(input('Book title? '), input('Its catagory? '), int(input('Its pages? ')))

obj7 = read(input('The name? '),input('Phone number? '), input('Email? '), int(input('Number of books he read? ')))
for x in range(obj7.getNumOfBooks()):
    obj7.addBooks(input('Book title? '), input('Its catagory? '), int(input('Its pages? ')))

obj8 = read(input('The name? '),input('Phone number? '), input('Email? '), int(input('Number of books he read? ')))
for x in range(obj8.getNumOfBooks()):
    obj8.addBooks(input('Book title? '), input('Its catagory? '), int(input('Its pages? ')))

obj9 = read(input('The name? '),input('Phone number? '), input('Email? '), int(input('Number of books he read? ')))
for x in range(obj9.getNumOfBooks()):
    obj9.addBooks(input('Book title? '), input('Its catagory? '), int(input('Its pages? ')))

obj10 = read(input('The name? '),input('Phone number? '), input('Email? '), int(input('Number of books he read? ')))
for x in range(obj10.getNumOfBooks()):
    obj10.addBooks(input('Book title? '), input('Its catagory? '), int(input('Its pages? ')))
'''

# this is just for easily test the program
obj1 = read('Abdullah',966,'4b@w.cn',5)
obj1.addBooks('gg','history',100)
obj1.addBooks('gg','history',100)
obj1.addBooks('gg','history',100)
obj1.addBooks('gg','history',100)
obj1.addBooks('gg','history',100)

obj2 = read('Omar',966,'em@w.cn',5)
obj2.addBooks('gg','story',100)
obj2.addBooks('gg','story',100)
obj2.addBooks('gg','story',100)
obj2.addBooks('gg','story',100)
obj2.addBooks('gg','story',100)

obj3 = read('Eyad',966,'em@w.cn',6)
obj3.addBooks('gg','cv',200)
obj3.addBooks('gg','cv',200)
obj3.addBooks('gg','cv',100)
obj3.addBooks('gg','cv',100)
obj3.addBooks('gg','cv',100)
obj3.addBooks('gg','cv',100)

obj4 = read('Saleh',966,'em@w.cn',5)
obj4.addBooks('gg','story',100)
obj4.addBooks('gg','story',100)
obj4.addBooks('gg','story',100)
obj4.addBooks('gg','story',100)
obj4.addBooks('gg','story',100)

obj5 = read('Mohammed',966,'em@w.cn',5)
obj5.addBooks('gg','story',100)
obj5.addBooks('gg','story',100)
obj5.addBooks('gg','story',100)
obj5.addBooks('gg','story',100)
obj5.addBooks('gg','story',100)

obj6 = read('Walled',966,'em@w.cn',5)
obj6.addBooks('gg','story',100)
obj6.addBooks('gg','story',100)
obj6.addBooks('gg','story',100)
obj6.addBooks('gg','story',100)
obj6.addBooks('gg','story',100)

obj7 = read('Rayan',966,'em@w.cn',5)
obj7.addBooks('gg','story',100)
obj7.addBooks('gg','story',100)
obj7.addBooks('gg','story',100)
obj7.addBooks('gg','story',100)
obj7.addBooks('gg','story',100)

obj8 = read('Faisal',966,'em@w.cn',5)
obj8.addBooks('gg','story',100)
obj8.addBooks('gg','story',100)
obj8.addBooks('gg','story',100)
obj8.addBooks('gg','story',100)
obj8.addBooks('gg','story',100)

obj9 = read('Abdulelah',966,'em@w.cn',5)
obj9.addBooks('gg','story',100)
obj9.addBooks('gg','story',100)
obj9.addBooks('gg','story',100)
obj9.addBooks('gg','story',100)
obj9.addBooks('gg','story',100)

obj10 = read('Khalid',966,'em@w.cn',5)
obj10.addBooks('gg','history',100)
obj10.addBooks('gg','history',100)
obj10.addBooks('gg','history',100)
obj10.addBooks('gg','history',100)
obj10.addBooks('gg','history',100)

# declirate and counting all history/story etc... was written.
countAllhistory = add_all(obj1.countHistory(), obj2.countHistory(), obj3.countHistory(), obj4.countHistory(), obj5.countHistory(), 
                          obj6.countHistory(), obj7.countHistory(), obj8.countHistory(), obj9.countHistory(), obj10.countHistory())

countAllstory = add_all(obj1.countStory(), obj2.countStory(), obj3.countStory(), obj4.countStory(), obj5.countStory(), 
                          obj6.countStory(), obj7.countStory(), obj8.countStory(), obj9.countStory(), obj10.countStory())

countAllscientist = add_all(obj1.countScientist(), obj2.countScientist(), obj3.countScientist(), obj4.countScientist(), obj5.countScientist(), 
                          obj6.countScientist(), obj7.countScientist(), obj8.countScientist(), obj9.countScientist(), obj10.countScientist())

countAllreligious = add_all(obj1.countReligious(), obj2.countReligious(), obj3.countReligious(), obj4.countReligious(), obj5.countReligious(), 
                          obj6.countReligious(), obj7.countReligious(), obj8.countReligious(), obj9.countReligious(), obj10.countReligious())

countAllLiterature = add_all(obj1.countLiterature(), obj2.countLiterature(), obj3.countLiterature(), obj4.countLiterature(), obj5.countLiterature(), 
                          obj6.countLiterature(), obj7.countLiterature(), obj8.countLiterature(), obj9.countLiterature(), obj10.countLiterature())

countAllother = add_all(obj1.countOthers(), obj2.countOthers(), obj3.countOthers(), obj4.countOthers(), obj5.countOthers(), 
                          obj6.countOthers(), obj7.countOthers(), obj8.countOthers(), obj9.countOthers(), obj10.countOthers())

# all the following is printing statmentes

print("NAME","\t\t","BOOKS")
printSQ(obj1.name,obj1.getNumOfBooks())
printSQ(obj2.name,obj2.getNumOfBooks())
printSQ(obj3.name,obj3.getNumOfBooks())
printSQ(obj4.name,obj4.getNumOfBooks())
printSQ(obj5.name,obj5.getNumOfBooks())
printSQ(obj6.name,obj6.getNumOfBooks())
printSQ(obj7.name,obj7.getNumOfBooks())
printSQ(obj8.name,obj8.getNumOfBooks())
printSQ(obj9.name,obj9.getNumOfBooks())
printSQ(obj10.name,obj10.getNumOfBooks())

print("")
print("All the group member has read", add_all(obj1.getNumOfBooks(),obj2.getNumOfBooks(),obj3.getNumOfBooks(),
               obj4.getNumOfBooks(), obj5.getNumOfBooks(), obj6.getNumOfBooks(),
               obj7.getNumOfBooks(), obj8.getNumOfBooks(), obj9.getNumOfBooks(),
               obj10.getNumOfBooks()),"books.")
print("")
printMostBooks(obj1.name,obj1.getNumOfBooks(), obj2.name,obj2.getNumOfBooks(), obj3.name,obj3.getNumOfBooks(),
               obj4.name,obj4.getNumOfBooks(), obj5.name,obj5.getNumOfBooks(), obj6.name,obj6.getNumOfBooks(),
               obj7.name,obj7.getNumOfBooks(), obj8.name,obj8.getNumOfBooks(), obj9.name,obj9.getNumOfBooks(),
               obj10.name,obj10.getNumOfBooks())



print("\nCATAGORY \t BOOKS")
printSQ('history', countAllhistory)
printSQ('story', countAllstory)
printSQ('scientist',countAllscientist)
printSQ('religious',countAllreligious)
printSQ('literature',countAllLiterature)
printSQ('other',countAllother)

print("")
printMostCatg(countAllhistory, countAllstory, countAllscientist, countAllreligious, countAllLiterature, countAllother )



print("\nNAME","\t\t","ALL PAGES")
printSQ(obj1.name,obj1.getAllPages())
printSQ(obj2.name,obj2.getAllPages())
printSQ(obj3.name,obj3.getAllPages())
printSQ(obj4.name,obj4.getAllPages())
printSQ(obj5.name,obj5.getAllPages())      # passing
printSQ(obj6.name,obj6.getAllPages())   # name    page
printSQ(obj7.name,obj7.getAllPages())
printSQ(obj8.name,obj8.getAllPages())
printSQ(obj9.name,obj9.getAllPages())
printSQ(obj10.name,obj10.getAllPages())

print("")
printMostPages(obj1.name,obj1.getAllPages(), obj2.name,obj2.getAllPages(), obj3.name,obj3.getAllPages(), 
          obj4.name,obj4.getAllPages(),obj5.name,obj5.getAllPages(), obj6.name,obj6.getAllPages(), 
          obj7.name,obj7.getAllPages(), obj8.name,obj8.getAllPages(), obj9.name,obj9.getAllPages(), 
          obj10.name,obj10.getAllPages())

print("")
print("All the group members have read ",add_all(obj1.getAllPages(), obj2.getAllPages(), obj3.getAllPages(), 
                                                     obj4.getAllPages(), obj5.getAllPages(), obj6.getAllPages(),
                                                    obj7.getAllPages(), obj8.getAllPages(), obj9.getAllPages(),
                                                   obj10.getAllPages()), "pages.\n") 
