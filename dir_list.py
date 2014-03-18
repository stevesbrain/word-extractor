import os

def listing(target):
    files=[]
    for dirname, dirnames, filenames in os.walk(target):
        # print path to all subdirectories first.
        # for subdirname in dirnames:
        #     print(os.path.join(dirname, subdirname))

        # print path to all filenames.
        for filename in filenames:
            files.append(os.path.join(dirname, filename))
            # print(os.path.join(dirname, filename))
    return(files)