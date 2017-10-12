User Manual
1.	Create – with this function, the user can create a file in a directory that he specified. Firstly the user has to enter the location of the file he wants to create: 
  
After the user enters the location or directory, the availability of that directory is checked. If that directory does not exist, then the error explanation comes up and the function starts to run from beginning if the user wants it to do:
 
If the directory is available, then the program asks for the filename which is going to be created:
 
After the name is given, the program checks if there is not any file with the given name in the given directory, if there is any file with the same on that directory again error comes up:
 
If everything is alright with the demands of the program, then the file is created:
        
“DONE SUCCESSFULLY”, this phrase is printed after each successful operation according to the implementation. 
2.	Delete	 - with this function the user can delete a file. For that purpose, according to our implementation and design, the first step is the same, to enter the location of the file.
 
The same cases mentioned in the create function are checked and if all of them are allowable to operate the function, the file is removed from the directory after the user enters the filename:
 
     

3.	Rename – to change the name of the given file, the user should use the feature of this function. As the implementation and design are the same for all of the operations, firstly the user has to show the location of the file:
 
After the program checks the availability of the directory and if there is not any error, then the user is asked for the current filename:
  

If the file is in the directory, then the program asks for the new filename, if not the same error handling process is going to work and the explanation will be shown for the user:
 
If the directory does not include any file with this filename then the file will be renamed, otherwise the error will be shown in the screen:
 
If everything is fine with the requirements of the program then the file will be renamed and “DONE SUCCESFULLY” will be printed.
 

4.	Copy – the initial steps are the same. The user is asked to enter path of the file and the            name of the file if everything works fine then the user will face with this command:
                    
So, the user has three options here; if the user gives only the destination, the copy of the file will be created on that directory with the same name; if the user enters only the filename then the copy of the file will be created in the current directory with this entered name; if the user gives both filename and destination then the copy of the file will be created in that directory with entered name. 
If the directory is the same and user has not entered any filename then error will occur:
 
5.	Move – this function changes the location of the file. After the location and the name of the file are given, the new location is asked from the user:
 
If the path is correct, then the file will be moved to that new location and removed from the previous location. 
6.	Append – the user can append his text to the text file with the help of this function. After the location and the name of the text file are entered by the user, the program tries to open that text file if it is available in the directory, otherwise the error occurs:
 
If the file is available and program succeeds to open it, then the user is asked to enter his text:
 
The user types his text and then these lines or sentences are written to the end of the text file and the program closes that file.
7.	Insert to specific position – the program allows the user to enter his text not only to the end of the file but also to the specific position in the text file, for this purpose like in the previous ones, the user is asked for the location and the name of the text file. If they are alright, then the program opens that text file and asks the user to add his text:
 
After that, the program keeps this text and asks the user to enter his desired position to add that text and this position should be specified with an integer:
 
If the position is integer then the program adds that text written by the user to the text file and closes that file, otherwise the error occurs and explanation is given to the user.
8.	Remove the content of the text file – to remove the content of the text file, the user needs to give the location and the name of the file, then the program tries to open the file in write mode so that the content of the text file will be removed. But to do that the location and the name of the text file have to be exact, otherwise the same errors mentioned above will occur and the appropriate explanations will be described. 
9.	Show the content of a text file, with the ability to pause per page – the user may want to look at the concept of the text file with some pauses. To do that the program asks the user to enter line number per page after the location and the name of the text file are entered:
 
After the “page” value is specified, the content of the text file will be described according to that page value and after each iteration the program asks the user if he wants to read more of text file or he wants to quit. As long as the user wants to read the content of the text file the lines will be printed page by page. After the last line of the text file, the program gives an information about the fact that the user came to the end of the text file:
   
