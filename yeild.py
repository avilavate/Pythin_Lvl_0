
#Implenting yield

def get_lines(f):
    for line in f:
        yield line

def read_file():
    try:
        f= open("./student.txt","r")
        for line in get_lines(f):
            print(line)
    except Exception:
        print("Couldnt read file")






read_file()