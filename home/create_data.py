import os
def Create_data(path) :

    with open( path , "r" ) as file :
        for line in file.readlines() :

            new_line = f"https://{line}"
            yield new_line


    file.close()


