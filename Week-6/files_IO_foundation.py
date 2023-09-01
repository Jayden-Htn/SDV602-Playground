"""
File I/O in Python using a set of examples

https://www.geeksforgeeks.org/file-handling-python/
"""


def write_lines_to_a_file(pLines, pToFile):
    """
    Opens pToFile if it does not exists it creates it, if it exists wipes it, leaving it empty and ready to write to
    f contains file "resource" or "handle" that is used when working with the file

    Args
       pLines - a list of lines to write to the file. 
                For example pLine=[" Beautiful is better than ugly.\n",
                         "Explicit is better than implicit.\n", 
                         "Simple is better than complex.\n", 
                         "Complex is better than complicated.\n"]

        pToFile the name of the file to write to.

    """
    f=open(pToFile,"w") # open file for writing
    f.writelines(pLines) # write each line in the list to the file
    f.close()


def read_lines_from_a_file_using_a_loop(pFromFile):
    """
    Opens pFromFile , reads it and  returns the lines as a list

    Args 
        pFromFile the name of the file to write to.
    """
    lines = []
    f=open(pFromFile,"r") # open file for reading
    while True:
        line=f.readline() # read a line
        if line=='':break # if the line is empty we are at the end of the file
        lines += [line]
    f.close()
    return lines


def read_lines_from_a_file(pFromFile):
    """
    Opens pFromFile , reads it and  returns the lines as a list

    Args 
         pFromFile the name of the file to write to.
    """
    lines = []
    f=open(pFromFile,"r")
    lines = f.readlines() # read all lines into a list
    f.close()
    return lines


def read_lines_from_a_file_with_exception(pFromFile):
    """
    Opens pFromFile , reads it and  returns the lines as a list.

    Wraps the file output in a try: ... except: ... block , see https://docs.python.org/3/library/exceptions.html
    DO this tutorial for more learning https://docs.python.org/3/tutorial/errors.html 

    Args
        pFromFile the name of the file to read from.

    """
    # best practice is to open the file in a try: ... except: ... block
    try:
        lines = []
        f=open(pFromFile,"r") 
        lines = f.readlines()
        f.close()
    except FileNotFoundError:
        print ("File is not found")

    return lines


def read_with_iterator(pFileName):
    """
    Opens pFileName , reads it and  returns the lines as a list.

    Wraps the file output in a try: ... except: ... block , see https://docs.python.org/3/library/exceptions.html
    DO this tutorial for more learning https://docs.python.org/3/tutorial/errors.html 

    Takes advantage of "f" as an iterator

    Args
       pFileName , name of the file to read from

    """
    try:
       lines = []
       f=open(pFileName,"r")
       # f is an iterator, so we can use it in a for loop
       for line in f :
           lines += [line]

    except FileNotFoundError:
        print ("File is not found")
        return lines
    else:
        f.close()
        return lines


def append_to_file(pFileName, pAppendThese):
    """
    Appends lines in the list pAppendThese to the file pFileName.

    Args
        pFileName the file to append to
        pAppendThese a list of strings to append
    """
    try:
        lines = []
        f = open(pFileName,'a') # open file for appending (adding to the end)
        f.writelines(pAppendThese)
    except FileNotFoundError:
        print ("File is not found")
    else:
        f.close()
        

def using_with_read(pFileName):
    """
    Reads a file into a list one line per list item

    Uses "with" and try catch, with removes need for f.close() "tidy up"

    Args
        pFileName - the name of the file as a string
    """ 
    lines = []
    try:
        # with automatically closes the file when the block ends
        with open(pFileName,'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("File is not found.")
    
    return lines        
     

def make_counter():
    """
    Generates two counter closures
    
    returns 
         increment, current_count
    """
    count = 0

    def increment():
        nonlocal count 
        # nonlocal means the count variable is not local to this function
        # it is in the enclosing scope
        count += 1
    
    def current_count():
        nonlocal count
        return count

    return increment, current_count


def filter_direct_from_read(pFileName, **kwargs):
    """
    Filters a file line by line returning all lines that match a filter
    Uses list comprehension that applies the filter function in its "if" clause

    Args
         pFileName the name of the file
         kwargs
             "skip_header" returns the list from item 1, when set to True, default is to include the first
             "filter" a function takes a string as a parameter and returns true or false. 

    """
    # function has kwargs as a parameter, kwargs is a dictionary
    # kwarg = keyword argument
    # used to pass a variable number of optional arguments to a function

    filter = None
    skip_header = False
    lines =  []
    try:
        with  open(pFileName,'r') as f:
            
            if 'filter' in kwargs: # check if filter is in kwargs
                filter = kwargs["filter"] # get the filter function from kwargs 
                lines = [line for line in f.readlines() if filter(line)] # list comprehension applying the filter function
            else :
                lines =  f.readlines() 
            
            if 'skip_header' in kwargs and kwargs['skip_header'] == True:
                # and is a short circuit operator, if the first condition is false the second is not evaluated
                # so if skip_header is not in kwargs, the second condition is not evaluated and will not throw an error
                lines = lines[1::] # slicing to select all lines from index 1 to the end of the list (skips index 0)

    except FileNotFoundError:
        print("File is not found.")

    return lines


if __name__ == "__main__":
    """ Test code"""
    write_lines_to_a_file(["Beautiful is better than ugly.\n","Explicit is better than implicit.\n", 
                           "Simple is better than complex.\n", "Complex is better than complicated.\n"],
                           "text.txt"
                         )
    # Now check text.txt in the current directory/folder

    #print("Reading the file one line at a time, using a loop.")
    #print(read_lines_from_a_file_using_a_loop("text.txt")) 

    #print("Reading the file into a list one item per line.")
    #print(read_lines_from_a_file("text.txt")) 

    print("Exceptions during File I/O")
    #print(read_lines_from_a_file_with_exception("text.txt"))
    #print(read_with_iterator("text.txt"))

    
    print("Append list to the end of a file")
    append_to_file("text.txt",["Another line. \n","Last Line. \n"])
    # Now check text.txt in the current directory/folder
    
    print("Bringing in with and filter ")
    #print(using_with_read("BadFileName.txt"))
    #print(using_with_read("text.txt"))
    
    print("Filter Direct read ")
    #print(filter_direct_from_read("BadFileName.txt")) # should throw error from Try: Except: block
    print(filter_direct_from_read("text.txt",
                                   filter= lambda x : 'Last' in x)) 
    # passing a lambda function in the kwargs as filter
    # lambda is an anonymous function, it has no name, it is defined in line like JS arrow functions
    # lambda x : 'Last' in x is the same as
    # def filter(x):
    #    return 'Last' in x
    # checks if the str 'Last' is in the string x
    print(filter_direct_from_read("text.txt",
                                   filter= lambda x : 'Last' in x, 
                                   skip_header =True))
    pass