import os
import shutil

def create():
    path = raw_input("enter the path where u want to create a file: ") # location of file
    try:
        os.chdir(path) # changing directory  
    except OSError: ## error handling in case of that directory does nit exist
        print "No such directory"
    else:
        name = raw_input("give a name to a file:") # to give a name to a file 
        if name not in os.listdir(path): # to check if the name is unique
            open(name, "w") # creating file by opening it in write mode
            print "DONE SUCCESFULLY!!!"
        else:
            print "there is a file in this directory with the same name"
##############################################################################

def delete():
    path = raw_input("enter the location:") # location of file
    try:
        os.chdir(path) # going to that directory 
    except OSError: ## error handling in case of that directory does not exist
        print "No such directory"
    else:
        filename = raw_input("enter filename u want to delete:") # entering the name of file
        if filename in os.listdir(path):
            os.remove(filename) # removing file
            print "DONE SUCCESFULLY!!!"
        else: # error handling if the file does not exist
            print "No such file"

############################################################################

def rename():

    path = raw_input("enter the location:") # location of file
    try:
        os.chdir(path) # going to that directory
    except OSError: ## error handling in case of that directory does not exist
        print "No such directory"
    else:
        filename = raw_input("enter filename u want to change:") # current filename
        if filename in os.listdir(path):
            new = raw_input("enter new filename:") # new filename
            if new not in os.listdir(path):
                os.rename(filename, new) # renaming the file
                print "DONE SUCCESFULLY!!!"
            else:
                print "there is a file in this directory with the same name"
        else: # error handling if the file does not exist
            print "No such file"

############################################################################

def copy():
    source = raw_input("enter the location of file u want to copy:") # location of file
    try:
        os.chdir(source) # going to that directory
    except OSError: ## error handling in case of that directory does not exist
        print "No such directory"
    else:
        filename = raw_input("enter the name of file u want to copy:") # entering filename
        if filename in os.listdir(source):
            dest = raw_input("Enter the destination/destination and filename/filename:") # location of the copied file 
            try:
                shutil.copy(filename, dest) # copying the file to its new location
                print "DONE SUCCESFULLY!!!"
            except shutil.Error: # error handling in case the directry is not changed and the new name is not given
                print "You are trying to copy the file in the same directory but without giving a name"
            except IOError: # error handling if directory does not exist
                print "No such directory"
        else:
            print "No such file"

############################################################################

def move():
    source = raw_input("enter the location of file u want to move:")# location of file 
    try:
        os.chdir(source) # going to that directory
        
    except OSError: # error handling in case that dorectory does not exist
        print "No such directory"
    else:
        filename = raw_input("enter the name of file:") # entering the name of the file 
        dest = raw_input("enter the directory u want to move to:") # the new location of the file
        
        try:
            shutil.move(filename, dest) # moving file 
            print "DONE SUCCESFULLY!!!"
        except IOError: # error handling if the directory or the file does not exist 
            print "No such file or directory"
        
#############################################################################

def append():
    source = raw_input("enter the location of text file:") # location of text file 
    try:
        os.chdir(source) # going to that location
    except OSError: # error handling if the directory does not exist 
        print "No such directory"
    else:
        filename = raw_input("Enter the name of textfile:") # entering name of the textfile 
        try:
            file = open(filename, "r+") # opening that file in read+ mode. read+ mode allows the user append to the textfile  
        except IOError: # error handling if the fil e does not exist 
            print "There is no such file in the directory"
        else:
            str = raw_input("type what u want to append to the textfile:") # entering words or sentences that user wants to add to the text file
            file.write(str) # writing to a textfile
            file.close() # closing a textfile
            print "DONE SUCCESFULLY!!!"

#############################################################################

def insert_to_spec_pos():
    source = raw_input("Enter a location of filename:") # location of text file
    try:
        os.chdir(source)# going to that location
    except OSError:# error handling if the directory does not exist 
        print "No such directory"
    else:
        txt = raw_input("enter name of txt file:") # name of textfile
        try:
            file = open(txt, "r+")# opening textfile in read+ mode 
        except IOError: # error handling if the file does not exist 
            print "No such file in the directory"
        else:
            str = raw_input("add text:") # text addition by user 
            position = input("insert position with an integer:") # desired postion where the user wants to make an addition 
            if type(position) == int: # to check if the position is integer or not
                start = file.read(position) # taking the first part of textfile until specified postion
                file.seek(position, 0) # changing cursor place to the specified position
                end = file.read() # taing the second part of textfile which is after specified position
                file.close() # closing file 
                file = open(txt, "w") # opening the file again in write mode. write mode delete the content of textfile and we rewrite the text file  
                file.write(start) # writing the first part of textfile
                file.write(" "+str+" ") # writing addition by user to the textfile
                file.write(end) # second part of textfile 
                file.close() # closing textfile
                print "DONE SUCCESFULLY!!!"
            else:
                print "position should be specified with an integer"

###################################################################

def remove_content_of_textfile():
    source = raw_input("enter the location of text file:") # location of textfile
    try:
        os.chdir(source) # going to that directory
    except OSError: #error handling  if the directory does not exist
        print "No such directory"
    else:
        filename = raw_input("Enter the name of textfile:") # enetring the name of file
        if filename in os.listdir(source): # to check if the file is in the directory
            open(filename, 'w') # opening the textfile in write mode so the content of textfile will be deleted
            print "DONE SUCCESFULLY!!!"
        else:
            print "No such file in directory"

#####################################################################

def show_content_per_page():
    source = raw_input("Enter the location of text file:") # location of text file
    try:
        os.chdir(source) # going to that directory
    except OSError: # error handling if the directory does not exist
        print "No such directory"
    else:
        file = raw_input("enter the name of textfile:") # entering the name of textfile
        try:
            txt = open(file, "r") # opening the file in read mode
        except IOError: # error handling if the file does not exist
            print "No such file in the directory"
        else:
            page = input("specify the number of lines per page with an integer:") # specifying the number of lines per page  
            if type(page) == int: # to check if the page is an integer 
                list = [] # this list will contain the lines of textfile
                for i in txt:
                    list.append(i.splitlines()) # adding lines of textfile to the list
                index = 0 # we start from 0 index it means the first line of textfile 
                decision = "yes" # default value of decision which will help the user when he decides to continue reading lines or not 
                while decision == "yes": # if the decision is yes the next commands will be executed 
                    for i in range(page): # page is the number of lines per page specified by the user, so this loop will iterate "page" times
                        if index<len(list): # index has to be less than lenght of the list 
                            var = str(list[index][0])  # var is the line in the textfile according to  the index number  
                            print var # printing that line  
                            index+=1 # increasing counter so that we pass to the next line in the textfile
                    if index == len(list): # if the index is equal to the length of the list it means that line is the last line in the textfile
                        print "it is the last line"
                        break
                    decision = raw_input("type yes if you want to continue, if not type something else:") # the decision whether the user wants to continue reading or not
            else:
                print "page shpuld be specified with an integer"
###################################################################
def pofm():

    x= raw_input("Available operations:\n1)create()\n2)delete()\n3)rename()\n4)copy()\n5)move()\n6)append()\n7)insert_to_spec_pos()\n8)remove_content_of_textfile()\n9)show_content_per_page()\nTo use any operation type corresponding number\nIf you want to get a help for any of the operations shown above type corresponding number and slash help,i.e(1/help):")

    if x=="1":
        create()
        y=raw_input("Do you want to continue (yes) or (no):")
        if y == "yes":
            pofm()
        else:
            print "See you later :)"

    if x== "1/help":
        print("With this function you can easily create a file in any directory by entering directory and file name. You cannot create the second file with the same name in the same directory")
        y=raw_input("Do you want to continue (yes) or (no):")
        if y == "yes":
            pofm()
        else:
            print "See you later :)"
    if x=="2":
        delete()
        y=raw_input("Do you want to continue (yes) or (no):")
        if y == "yes":
            pofm()
        else:
            print "See you later :)"
    if x== "2/help":
        print("You can use this operation to delete any file in any directory")
        y=raw_input("Do you want to continue (yes) or (no):")
        if y == "yes":
            pofm()
        else:
            print "See you later :)"
    if x=="3":
        rename()
        y=raw_input("Do you want to continue (yes) or (no):")
        if y == "yes":
            pofm()
        else:
            print "See you later :)"

    if x== "3/help":
        print("Choose this operation to rename a file in a chosen directory.")
        y=raw_input("Do you want to continue (yes) or (no):")
        if y == "yes":
            pofm()
        else:
            print "See you later :)"
    if x=="4":
        copy()
        y=raw_input("Do you want to continue (yes) or (no):")
        if y == "yes":
            pofm()
        else:
            print "See you later :)"

    if x== "4/help":
        print("With this function you can create a copy of chosen file either in the same directory but with different name or in the other directory with the same name or a different one.\nTo create in the same directory you only need to enter filename,\nto create in the other directory you can either give path or path with filename.")
        y=raw_input("Do you want to continue (yes) or (no):")
        if y == "yes":
            pofm()
        else:
            print "See you later :)"

    if x=="5":
        move()
        y=raw_input("Do you want to continue (yes) or (no):")
        if y == "yes":
            pofm()
        else:
            print "See you later :)"

    if x== "5/help":
        print("You can change a location of file with this function. But if you give just filename when the program wants a destination from you, it will not change directory and the name of file will be changed.\nYou need to give path to move a file!")
        y=raw_input("Do you want to continue (yes) or (no):")
        if y == "yes":
            pofm()
        else:
            print "See you later :)"

    if x=="6":
        append()
        y=raw_input("Do you want to continue (yes) or (no):")
        if y == "yes":
            pofm()
        else:
            print "See you later :)"

    if x== "6/help":
        print("To append a text to the end of any text file, you just need to give location and name of that file")
        y=raw_input("Do you want to continue (yes) or (no):")
        if y == "yes":
            pofm()
        else:
            print "See you later :)"

    if x=="7":
        insert_to_spec_pos()
        y=raw_input("Do you want to continue (yes) or (no):")
        if y == "yes":
            pofm()
        else:
            print "See you later :)"

    if x== "7/help":
        print("Let's say you want to add text to the text file for example after first 15 characters, not to the beginning or the end. This function will do it for you. You need to enter the location, the name of text file and the the number of characters that you want to insert after.")
        y=raw_input("Do you want to continue (yes) or (no):")
        if y == "yes":
            pofm()
        else:
            print "See you later :)"

    if x=="8":
        remove_content_of_textfile()
        y=raw_input("Do you want to continue (yes) or (no):")
        if y == "yes":
            pofm()
        else:
            print "See you later :)"

    if x== "8/help":
        print("Enter the location and the name of text file and delete whatever in it.")
        y=raw_input("Do you want to continue (yes) or (no):")
        if y == "yes":
            pofm()
        else:
            print "See you later :)"

    if x=="9":
        show_content_per_page()
        y=raw_input("Do you want to continue (yes) or (no):")
        if y == "yes":
            pofm()
        else:
            print "See you later :)"

    if x== "9/help":
        print("You can divide text file into pages by defining line count per page and to vies that text file page by page")
        y=raw_input("Do you want to continue (yes) or (no):")
        if y == "yes":
            pofm()
        else:
            print "See you later :)"
pofm()
