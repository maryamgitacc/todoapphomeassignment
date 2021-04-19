Requirements that you should have on your system.

 Python 3 (tested on Python 3.8.6 64-bit)
 Tested on Windows 10 (should work on all OSs)
 Only Python 3 built-in modules were used

If you have various python versions installed replace the python command with the executable name that you usually use in Python 3.

TODOAPP is a command-line interface application which uses command line switches to achieve it's functionality. 

At first you should run the application with the python todoapp.py -l command
expected: if we have some tasks in file.txt then app print your task


as you can see here :

1-[] Walk the dog

2-[] Buy milk

3-[] Do homework


Or if we don't have any task the application should print "No todos for today " since you have not added any task yet.

Second you have to run the application with the python todoapp.py -a "Feed the monkey" command
expected: the application will add feed the monkey to file.txt and print "add feed the monkey to the list"
or if run the application with the python todoapp.py -a print " Unable to add: no task provided" since you  have not added any tasks yet.


In next step you should run the application with the python todoapp.py -r task number command
expected: Then the app should remove the specific task from the file.txt
for example :python todoapp.py -r 1
then the app remove the first task from the file.

Then run the application with the python todoapp.py -r command
expected: the application print "Unable to remove: no index provided"


Next step is to run the application with the python todoapp.py -r any number command
if any number is higher than tasks number
expected: the app will print "Unable to remove: index is out of bound"

Then we run the application with the python todoapp.py -r a word command
expected: the app print "Unable to remove: index is not a number"

After that run the application with the python todoapp.py -c task number command
expected: Then the application should check the specific task from the file.txt

And then run the application with the python todoapp.py -c task number command
expected: Then the app should remove the specific task from the file.txt
for example :python todoapp.py -c 1
then the application remove the first task from the file

And again run the application with the python todoapp.py -c command
expected: the application print "Unable to remove: no index provided"


Here we run the application with the python todoapp.py -c any number command
if any number is higher than tasks number 
expected: the application print "Unable to remove: index is out of bound"

And finally we run the application with the python todoapp.py -c a word command
expected: the application print "Unable to remove: index is not a number" 


Generally ToDo App is simple and awesome app to organize our tasks with very easy to use interface.ToDo can help us to make list of our tasks.



To sum up :
 Start the application without any command line switch to show help
 -l to list the tasks
 -a  to add a new task
 -r  to remove a task
 -c  to complete a task