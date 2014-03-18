import os

def listing(target):
    #Create our list for later returns
    files=[]
    #For all the stuff in our target
    for dirname, dirnames, filenames in os.walk(target):
        ## print path to all subdirectories first - commented out because it's not needed
        ## in our specific project
        # for subdirname in dirnames:
        #     print(os.path.join(dirname, subdirname))

        # print path to all filenames, and append this to our list
        for filename in filenames:
            files.append(os.path.join(dirname, filename))
            ## Print function below if anyone ever wants the lonely sod
            # print(os.path.join(dirname, filename))
    #Send back our list for usage
    return(files)