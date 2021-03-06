# Love21
Love21 Charity Class Registration
Welcome to Love 21 Student Registration Software. This document will provide you with information needed for setting up the python executable and running it. 

Please make sure that you have downloaded the latest version of python so that the program will run optimally. The current version of python release at the time of this Love21 Patch is Python 3.9.2. Please visit: https://www.python.org/ to download the latest version of python.

Once Python is installed successfully, please create a local folder on your desktop for easy navigation. Name the folder something short, but easily identifiable for ease of access. Make sure all registration files are correctly named and stored in the same folder as the executable.

Naming Requirements:
master_log.csv
student_log.csv
class_log.csv
weekly_log.csv

Instructions:
1) Make sure you swap out weekly_log with the current version of weekly_log that was updated this week. Delete all previously generated .txt files named as some integer. 
2) Open terminal/commandprompt and navigate using Linux Command Line Commands to the folder storing the executable. 
3) Type: "python love21.py" | This will run the program. You will need to type in one character, 'Y' or 'N' in the case of the master log being written before, i.e. not the first time running the program. 
4) Process the txt files generated with the student log information to inform users of final registration results. 


Required Libraries:
pandas
numpy
os
time
datetime
random

Please use pip install [library-name] to install all neccessary libraries on through the command line before running the executable. 


-----------
Student Log:

student id 	cat(1) 	cat(2)	cat(3)	cat(4)	cat(5)	... 	cat(n)	NumMonth	Tab	


This would be tabulated linearly on the first pass and updated as needed depending on whether we care about attendance in the last 6 or 12 months. 

Master Log: (Date is of the class start date)

date(DD/MM/YY) student id	class id	class name	class type	registered	



Class Log:

classs id	start date	end date	class name 	class type 	quota	enrollment	filled



Weekly Log would be identical to Master Log in terms of columns. 


