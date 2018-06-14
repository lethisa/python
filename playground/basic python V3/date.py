# datetime
import datetime

filename = datetime.datetime.now()

def create_file():
    with open(filename.strftime("%Y-%m-%d-%H-%M") + ".txt", "w") as file:
        file.write("this time")

create_file() 
