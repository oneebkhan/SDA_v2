from tabulate import tabulate
from itertools import zip_longest as it

class Cpp:

    # initialising the cpp class
    def __init__(self):
        pass

    cpp_class = []
    cpp_methods = []
    cpp_variables = []

    # getting a .cpp name from the directory name
    def fCpp(self, filename):
        x = filename.rfind("/")
        y = filename.rfind('.cpp')
        return filename[(x + 1):(y + 4)]

    # read and get CPP classes
    def cppClass(self, filename):
        with open(filename) as cc:
            for line in cc:
                if 'class' in line:
                    line = line.strip()
                    if '//' in line:
                        line = line.rpartition('//')[0]
                    elif '/*' in line:
                        line = line.rpartition('/*')[0]

                    if ':' in line:
                        line = line.replace(':', 'inherits')

                    if '{' in line:
                        self.cpp_class.append(line.rpartition('{')[0])
                    else:
                        self.cpp_class.append(line)

                if 'int main()' in line:
                    line = line.strip()
                    if '//' in line:
                        line = line.rpartition('//')[0]
                    elif '/*' in line:
                        line = line.rpartition('/*')[0]

                    if '{' in line:
                        self.cpp_class.append(line.rpartition('{')[0])
                    else:
                        self.cpp_class.append(line)
        cc.close()

    # read and get CPP methods
    def cppMeth(self, filename):
        with open(filename) as cm:
            for line in cm:
                if ('void' in line or 'private' in line or 'public' in line) and ('(' in line and ')' in line and ';' not in line):
                    line = line.strip()
                    if '//' in line:
                        line = line.rpartition('//')[0]
                    elif '/*' in line:
                        line = line.rpartition('/*')[0]

                    if '{' in line:
                        self.cpp_methods.append(line.rpartition('{')[0])
                    else:
                        self.cpp_methods.append(line)
        cm.close()

    # reads and gets CPP variables
    def cppVar(self, filename):
        with open(filename) as cv:
            temp1 = []
            for line in cv:
                if 'for' in line:
                    None
                elif 'while' in line:
                    None
                elif 'if' in line:
                    None
                elif ('int ' in line and ';' in line) and ('Print' not in line and 'print' not in line):
                    line = line.strip()
                    if '=' in line:
                        line = line.rpartition('=')[0]
                        temp1.append(line)
                    else:
                        line = line.rpartition(';')[0]
                        temp1.append(line)

                elif 'char ' in line and ';' in line:
                    line = line.strip()
                    if '=' in line:
                        line = line.rpartition('=')[0]
                        temp1.append(line)
                    else:
                        line = line.rpartition(';')[0]
                        temp1.append(line)

                elif ('string ' in line or 'String ' in line) and ';' in line:
                    line = line.strip()
                    if '=' in line:
                        line = line.rpartition('=')[0]
                        temp1.append(line)
                    else:
                        line = line.rpartition(';')[0]
                        temp1.append(line)

                elif 'double ' in line and ';' in line:
                    line = line.strip()
                    if '=' in line:
                        line = line.rpartition('=')[0]
                        temp1.append(line)
                    else:
                        line = line.rpartition(';')[0]
                        temp1.append(line)

                elif 'float ' in line and ';' in line:
                    line = line.strip()
                    if '=' in line:
                        line = line.rpartition('=')[0]
                        temp1.append(line)
                    else:
                        line = line.rpartition(';')[0]
                        temp1.append(line)

                elif 'byte ' in line and ';' in line:
                    line = line.strip()
                    if '=' in line:
                        line = line.rpartition('=')[0]
                        temp1.append(line)
                    else:
                        line = line.rpartition(';')[0]
                        temp1.append(line)

                elif 'short ' in line and ';' in line:
                    line = line.strip()
                    if '=' in line:
                        line = line.rpartition('=')[0]
                        temp1.append(line)
                    else:
                        line = line.rpartition(';')[0]
                        temp1.append(line)

                elif 'long ' in line and ';' in line:
                    line = line.strip()
                    if '=' in line:
                        line = line.rpartition('=')[0]
                        temp1.append(line)
                    else:
                        line = line.rpartition(';')[0]
                        temp1.append(line)

                elif ('boolean ' in line or 'bool' in line) and ';' in line:
                    line = line.strip()
                    if '=' in line:
                        line = line.rpartition('=')[0]
                        temp1.append(line)
                    else:
                        line = line.rpartition(';')[0]
                        temp1.append(line)

        cv.close()
        var1 = set(temp1)
        for x in var1:
            self.cpp_variables.append(x)

    #tabular print statement
    def tcpp(self, filename):
        b = open("Extractor.txt", "a")  # open a file for appending

        print('\n' + self.fCpp(filename))
        b.write(self.fCpp(filename) + '\n')  # print name of the file into a text file

        self.cppClass(filename)  # function to seperate class
        self.cppVar(filename)
        self.cppMeth(filename)

        pdtabulate = lambda df: tabulate(df, headers=(('Class', 'Methods', 'Variables')), tablefmt='psql')
        print(pdtabulate(it(self.cpp_class, self.cpp_methods, self.cpp_variables)))
        b.write(pdtabulate(it(self.cpp_class, self.cpp_methods, self.cpp_variables)) + '\n\n')

        self.cpp_class.clear()
        self.cpp_methods.clear()
        self.cpp_variables.clear()

        b.close()