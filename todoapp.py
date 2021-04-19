import sys



def checking_task(task):
    file = open('file.txt')
    checked = file.readlines()
    
    try: 
        
        if int(task)>len(checked): 
            print("Unable to check: index is out of bound")
        
        else:

            checked[int(task)-1] = f"[x] {checked[int(task)-1]}"
            file = open("file.txt", "w")
            file.writelines(checked)



  
    except ValueError: 
        print("Unable to check: index is not a number")
    




def printing_usage(): 
    print("Command Line Todo application \n" , "============================= \n" , "Command-line arguments: \n" , "-l   Lists all the tasks \n" ,"-a   Adds a new task \n" , "-r   Removes a task \n" , "-c   Completes a task \n")





def listing_task(file_name):
    
    
    try:
        
        with open(file_name,'r') as f:
            
            content = f.readlines()

            file_len = len(content)
            i = 0
            if file_len == 0:
                print("No todos for today!")
            

            
            
            while i < file_len: 
                for word in content: 
                    if (word[0])=="[":
                        print(f"{i+1}-",content[i])
                        i = i+1
                    else:

                        print(f"{i+1}- [ ]",content[i])
                        i =i+1
      



            
           
    except IOError as error: 
        print(error)
        print("Error occurred reading the file")
        sys.exit()
        
def adding_tasks(task): 
    
        
        with open("file.txt",'a') as file:
            file.write(f"{task}\n")
            print("add" + task + "to the list")




def deleting_tasks(task):
    
    try:
        file = open('file.txt', "r")
        lines = file.readlines()
    
        file_len = len(lines) 
        if int(task) > file_len: 
                print("Unable to remove: index is out of bound") 

    
        else: 
            del lines[int(task) - 1]
            new_file = open("file.txt", "w+")
        for line in lines:
            new_file.write(line)
    
    
    
    
    except ValueError: 
        print("Unable to remove: index is not a number")
        print(sys.argv)



if len(sys.argv) == 1: 
        printing_usage()


elif sys.argv[1] == "-l":  
        listing_task("file.txt")


elif len(sys.argv) ==3 and sys.argv[1] == "-a": 
        adding_tasks(sys.argv[2]) 



elif len(sys.argv) ==2 and sys.argv[1] == "-a": 
    print("Unable to add: no task provided")   



elif len(sys.argv) ==3 and sys.argv[1] == "-r": 
        deleting_tasks(sys.argv[2])  



elif len(sys.argv) ==2 and sys.argv[1] == "-r": 
    print("Unable to remove: no index provided") 


elif len(sys.argv) ==3 and sys.argv[1] == "-c": 
    checking_task(sys.argv[2])


elif len(sys.argv) ==2 and sys.argv[1] == "-c": 
    print("Unable to check: no index provided")


else: 
    print(" Unsupported argument")  
    printing_usage()
