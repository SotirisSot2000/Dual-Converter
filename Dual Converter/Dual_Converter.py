from Parser import parse

def convert(filename):
    c = []
    A = []
    b = []
    Eqin = []
    maxmin = []
    c, A, b, maxmin, Eqin = parse(filename)



def export(oldfilename):
    createNewFile(oldfilename)



def createNewFile(filename):
        noExtensionName = ""
        extension = ""
        index = 0
        while filename[index] != '.':
            noExtensionName += filename[index]
            index += 1
        while index < len(filename):
            extension += filename[index]
            index += 1
        newFileName =  noExtensionName + "Dual" + extension
        file = None
        try:
            if os.path.exists(newFileName):
                os.remove(newFileName)
            file = open(newFileName, "w")
        except FileNotFoundError:
            print("File not found\n")

            system.exit(0)
        except PermissionError:
            print("You have not permission to write in this file\n")

            system.exit(0)
        return file


def main():
    filename = str(input("\nEnter problem file name: "))
    convert(filename)

if __name__ == "__main__":
    main()


