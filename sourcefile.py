class read:
    def __init__(self, name, number, email, # initialize the attributes
                catg1, book1, pages1, catg2, book2, pages2,
               catg3, book3, pages3, catg4, book4, pages4, catg5, book5, pages5):
        self.name = name
        self.__number = number # private attribute
        self.__email = email   # private attribute   

        self.catg1 = catg1
        self.book1 = book1
        self.pages1 = pages1

        self.catg2 = catg2
        self.book2 = book2
        self.pages2 = pages2

        self.catg3 = catg3
        self.book3 = book3
        self.pages3 = pages3

        self.catg4 = catg4
        self.book4 = book4
        self.pages4 = pages4

        self.catg5 = catg5
        self.book5 = book5
        self.pages5 = pages5

    def getNumber(self):
        return self.__number

    def getEmail(self):
        return self.__email

    def __aPersonPages(self): # private method
        return self.pages1 + self.pages2 +self.pages3 +self.pages4 +self.pages5

    def booksPages(self): # getting all pages of all books an object read
         return self.__aPersonPages()  


    def countHistory(self):
        counter = 0
        if(self.catg1.lower() == 'history'):
            counter += 1
        if(self.catg2.lower() == 'history'):
            counter += 1
        if(self.catg3.lower() == 'history'):
            counter += 1
        if(self.catg4.lower() == 'history'):
            counter += 1
        if(self.catg5.lower() == 'history'):
            counter += 1
        return counter

    def countStory(self): 
        counter = 0
        if(self.catg1.lower() == 'story'):
            counter += 1
        if(self.catg2.lower() == 'story'):
            counter += 1
        if(self.catg3.lower() == 'story'):
            counter += 1
        if(self.catg4.lower() == 'story'):
            counter += 1
        if(self.catg5.lower() == 'story'):
            counter += 1
        return counter

    def countScientist(self): 
        counter = 0
        if(self.catg1.lower() == 'scientist'):
            counter += 1
        if(self.catg2.lower() == 'scientist'):
            counter += 1
        if(self.catg3.lower() == 'scientist'):
            counter += 1
        if(self.catg4.lower() == 'scientist'):
            counter += 1
        if(self.catg5.lower() == 'scientist'):
            counter += 1
        return counter

    def countReligious(self): 
        counter = 0
        if(self.catg1.lower() == 'religious'):
            counter += 1
        if(self.catg2.lower() == 'religious'):
            counter += 1
        if(self.catg3.lower() == 'religious'):
            counter += 1
        if(self.catg4.lower() == 'religious'):
            counter += 1
        if(self.catg5.lower() == 'religious'):
            counter += 1
        return counter

    def countLiterature(self): 
        counter = 0
        if(self.catg1.lower() == 'literature'):
            counter += 1
        if(self.catg2.lower() == 'literature'):
            counter += 1
        if(self.catg3.lower() == 'literature'):
            counter += 1
        if(self.catg4.lower() == 'literature'):
            counter += 1
        if(self.catg5.lower() == 'literature'):
            counter += 1
        return counter

    def countOthers(self):
        counter = 0
        if(self.catg1.lower() != 'literature' and self.catg1.lower() != 'religious' and  self.catg1.lower() != 'history' and self.catg1.lower() != 'story' and self.catg1.lower() != 'scientist'):
            counter += 1
        if(self.catg2.lower() != 'literature' and self.catg2.lower() != 'religious' and  self.catg2.lower() != 'history' and self.catg2.lower() != 'story' and self.catg2.lower() != 'scientist'):
            counter += 1
        if(self.catg3.lower() != 'literature' and self.catg3.lower() != 'religious' and  self.catg3.lower() != 'history' and self.catg3.lower() != 'story' and self.catg3.lower() != 'scientist'):
            counter += 1
        if(self.catg4.lower() != 'literature' and self.catg4.lower() != 'religious' and  self.catg4.lower() != 'history' and self.catg4.lower() != 'story' and self.catg4.lower() != 'scientist'):
            counter += 1
        if(self.catg5.lower() != 'literature' and self.catg5.lower() != 'religious' and  self.catg5.lower() != 'history' and self.catg5.lower() != 'story' and self.catg5.lower() != 'scientist'):
            counter += 1
        return counter


                                          
def add_all(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10): # can be used to add all everyones' pages also count everyones' catagories
    list = [i1 , i2 , i3 , i4 , i5 , i6 , i7 , i8 , i9 , i10]
    sum = 0
    for x in list:
        sum += x
    return sum 


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
    print("The most catagory was read is",BIGGEST,"by" , biggest,"books")    


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
    
    print("The one who read pages the most is",BIGGEST,"by", biggest,"pages")  


def printSQ(string, num): # printing a schedule
 
    if len(string) < 7:        # counting how many letters to mange blanks ( \t )
     print(string,"\t\t", num)
    else:
     print(string,"\t", num)



# taking input from the user and 
'''
obj1 = read(input('The name? '),input('Phone number? '), input('Email? '), input('Book 1 catagory? '), input('Book title? '), int(input('Its pages? ')),
           input('Book 2 catagory? '), input('Book title? '), int(input('Its pages? ')), input('Book 3 catagory? '), input('Book title? '), int(input('Its pages? ')),
          input('Book 4 catagory? ') , input('Book title? '), int(input('Its pages? ')), input('Book 5 catagory? '), input('Book title? '), int(input('Its pages? '))) 

obj2 = read(input('The name? '),input('Phone number? '), input('Email? '), input('Book 1 catagory? '), input('Book title? '), int(input('Its pages? ')),
           input('Book 2 catagory? '), input('Book title? '), int(input('Its pages? ')), input('Book 3 catagory? '), input('Book title? '), int(input('Its pages? ')),
          input('Book 4 catagory? ') , input('Book title? '), int(input('Its pages? ')), input('Book 5 catagory? '), input('Book title? '), int(input('Its pages? '))) 

obj3 = read(input('The name? '),input('Phone number? '), input('Email? '), input('Book 1 catagory? '), input('Book title? '), int(input('Its pages? ')),
           input('Book 2 catagory? '), input('Book title? '), int(input('Its pages? ')), input('Book 3 catagory? '), input('Book title? '), int(input('Its pages? ')),
          input('Book 4 catagory? ') , input('Book title? '), int(input('Its pages? ')), input('Book 5 catagory? '), input('Book title? '), int(input('Its pages? '))) 

obj4 = read(input('The name? '),input('Phone number? '), input('Email? '), input('Book 1 catagory? '), input('Book title? '), int(input('Its pages? ')),
           input('Book 2 catagory? '), input('Book title? '), int(input('Its pages? ')), input('Book 3 catagory? '), input('Book title? '), int(input('Its pages? ')),
          input('Book 4 catagory? ') , input('Book title? '), int(input('Its pages? ')), input('Book 5 catagory? '), input('Book title? '), int(input('Its pages? '))) 

obj5 = read(input('The name? '),input('Phone number? '), input('Email? '), input('Book 1 catagory? '), input('Book title? '), int(input('Its pages? ')),
           input('Book 2 catagory? '), input('Book title? '), int(input('Its pages? ')), input('Book 3 catagory? '), input('Book title? '), int(input('Its pages? ')),
          input('Book 4 catagory? ') , input('Book title? '), int(input('Its pages? ')), input('Book 5 catagory? '), input('Book title? '), int(input('Its pages? '))) 

obj6 = read(input('The name? '),input('Phone number? '), input('Email? '), input('Book 1 catagory? '), input('Book title? '), int(input('Its pages? ')),
           input('Book 2 catagory? '), input('Book title? '), int(input('Its pages? ')), input('Book 3 catagory? '), input('Book title? '), int(input('Its pages? ')),
          input('Book 4 catagory? ') , input('Book title? '), int(input('Its pages? ')), input('Book 5 catagory? '), input('Book title? '), int(input('Its pages? '))) 

obj7 = read(input('The name? '),input('Phone number? '), input('Email? '), input('Book 1 catagory? '), input('Book title? '), int(input('Its pages? ')),
           input('Book 2 catagory? '), input('Book title? '), int(input('Its pages? ')), input('Book 3 catagory? '), input('Book title? '), int(input('Its pages? ')),
          input('Book 4 catagory? ') , input('Book title? '), int(input('Its pages? ')), input('Book 5 catagory? '), input('Book title? '), int(input('Its pages? '))) 

obj8 = read(input('The name? '),input('Phone number? '), input('Email? '), input('Book 1 catagory? '), input('Book title? '), int(input('Its pages? ')),
           input('Book 2 catagory? '), input('Book title? '), int(input('Its pages? ')), input('Book 3 catagory? '), input('Book title? '), int(input('Its pages? ')),
          input('Book 4 catagory? ') , input('Book title? '), int(input('Its pages? ')), input('Book 5 catagory? '), input('Book title? '), int(input('Its pages? '))) 

obj9 = read(input('The name? '),input('Phone number? '), input('Email? '), input('Book 1 catagory? '), input('Book title? '), int(input('Its pages? ')),
           input('Book 2 catagory? '), input('Book title? '), int(input('Its pages? ')), input('Book 3 catagory? '), input('Book title? '), int(input('Its pages? ')),
          input('Book 4 catagory? ') , input('Book title? '), int(input('Its pages? ')), input('Book 5 catagory? '), input('Book title? '), int(input('Its pages? '))) 

obj10 = read(input('The name? '),input('Phone number? '), input('Email? '), input('Book 1 catagory? '), input('Book title? '), int(input('Its pages? ')),
           input('Book 2 catagory? '), input('Book title? '), int(input('Its pages? ')), input('Book 3 catagory? '), input('Book title? '), int(input('Its pages? ')),
          input('Book 4 catagory? ') , input('Book title? '), int(input('Its pages? ')), input('Book 5 catagory? '), input('Book title? '), int(input('Its pages? '))) '''



# this is just for easily test the program
obj1 = read('Abdullah',96653, 'Abdullah@com', 'story', 'bdm', 200, 'literature', 'ssc', 250, 'literature', 'ccs', 300, 'story' , 'ahof', 100, 'story', 'ff', 300)

obj2 = read('Abdullrahman',96655, 'Abdullrahman@com', 'story', 'bdm', 100, 'story', 'ssc', 100, 'history', 'ccs', 300, 'literature' , 'ahof', 100, 'story', 'ff', 300)

obj3 = read('Abdullaziz',96664, 'Abdullaziz@com', 'story', 'bdm', 200, 'literature', 'ssc', 250, 'history', 'ccs', 300, 'literature' , 'ahof', 100, 'literature', 'ff', 300)

obj4 = read('Omar',96652, 'Omar@com', 'literature', 'bdm', 200, 'literature', 'ssc', 250, 'literature', 'ccs', 300, 'story' , 'ahof', 100, 'story', 'ff', 300)

obj5 = read('Khalid',96651, 'Khalid@com', 'religious', 'bdm', 200, 'religious', 'ssc', 250, 'religious', 'ccs', 300, 'literature' , 'ahof', 100, 'history', 'ff', 300)

obj6 = read('Saleh',96612, 'Saleh@com', 'scientist', 'bdm', 200, 'scientist', 'ssc', 250, 'literature', 'ccs', 300, 'literature' , 'ahof', 100, 'story', 'ff', 300)

obj7 = read('Mohammed',96622, 'Mohammed@com', 'history', 'bdm', 200, 'scientist', 'ssc', 250, 'literature', 'ccs', 300, 'scientist' , 'ahof', 100, 'story', 'ff', 300)

obj8 = read('Bandar',96612, 'Bader@com', 'literature', 'bdm', 200, 'scientist', 'ssc', 250, 'scientist', 'ccs', 300, 'history' , 'ahof', 100, 'story', 'ff', 300)

obj9 = read('Abdulelah',96629, 'Abdulelah@com', 'history', 'bdm', 200, 'literature', 'ssc', 250, 'history', 'ccs', 300, 'history' , 'ahof', 100, 'story', 'ff', 300)

obj10 = read('Eyad',96699, 'eyad@com', 'Literature', 'bdm', 500, 'literature', 'ssc', 250, 'history', 'ccs', 300, 'cv' , 'ahof', 100, 'cv', 'ff', 300) 



# initialize and counting all history/story etc... was written. *it'll used in last two printing*
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


# ALL THE FOLLOWING ARE PRINTING STATMENTS

print("NAME","\t\t","ALL PAGES")
printSQ(obj1.name,obj1.booksPages())
printSQ(obj2.name,obj2.booksPages())
printSQ(obj3.name,obj3.booksPages())
printSQ(obj4.name,obj4.booksPages())
printSQ(obj5.name,obj5.booksPages())      # passing
printSQ(obj6.name,obj6.booksPages())   # name    page
printSQ(obj7.name,obj7.booksPages())
printSQ(obj8.name,obj8.booksPages())
printSQ(obj9.name,obj9.booksPages())
printSQ(obj10.name,obj10.booksPages())



print("\n\nAll the group members have read ",add_all(obj1.booksPages(), obj2.booksPages(), obj3.booksPages(), 
                                                     obj4.booksPages(), obj5.booksPages(), obj6.booksPages(),
                                                    obj7.booksPages(), obj8.booksPages(), obj9.booksPages(),
                                                   obj10.booksPages()), "pages by 50 books\n")



printMostPages(obj1.name,obj1.booksPages(), obj2.name,obj2.booksPages(), obj3.name,obj3.booksPages(), 
          obj4.name,obj4.booksPages(),obj5.name,obj5.booksPages(), obj6.name,obj6.booksPages(), 
          obj7.name,obj7.booksPages(), obj8.name,obj8.booksPages(), obj9.name,obj9.booksPages(), 
          obj10.name,obj10.booksPages())



print("\n\nCATAGORY \t BOOKS")
printSQ('history', countAllhistory)

printSQ('story', countAllstory)

printSQ('scientist',countAllscientist)

printSQ('religious',countAllreligious)

printSQ('literature',countAllLiterature)

printSQ('other',countAllother)



print("\n")
printMostCatg(countAllhistory, countAllstory, countAllscientist, countAllreligious, countAllLiterature, countAllother )
print("")
