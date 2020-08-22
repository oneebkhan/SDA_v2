from tabulate import tabulate
from itertools import zip_longest as it

class Cs:

    # initialising the cs class
    def __init__(self):
        pass

    cs_class = []
    cs_methods = []
    cs_variables = []

    # getting a .cs name from the directory name
    def fCs(self, filename):
        x = filename.rfind("/")
        y = filename.rfind('.cs')
        return filename[(x + 1):(y + 3)]

    # read and get CS classes
    def csClass(self, filename):
        with open(filename) as csc:
            for line in csc:
                if 'class' in line:
                    line = line.strip()
                    if '//' in line:
                        line = line.rpartition('//')[0]
                    elif '/*' in line:
                        line = line.rpartition('/*')[0]

                    if '{' in line:
                        self.cs_class.append(line.rpartition('{')[0])
                    else:
                        self.cs_class.append(line)

                if 'Main' in line:
                    line = line.strip()
                    if '//' in line:
                        line = line.rpartition('//')[0]
                    elif '/*' in line:
                        line = line.rpartition('/*')[0]

                    if '{' in line:
                        self.cs_class.append(line.rpartition('{')[0])
                    else:
                        self.cs_class.append(line)

            csc.close()

    # read and get CS methods
    def csMeth(self, filename):
        with open(filename) as cm:
            for line in cm:
                if ('void' in line or 'private' in line or 'public' in line) and ('(' in line and ')' in line) and (';' not in line):
                    line = line.strip()
                    if '//' in line:
                        line = line.rpartition('//')[0]
                    elif '/*' in line:
                        line = line.rpartition('/*')[0]

                    if '{' in line:
                        self.cs_methods.append(line.rpartition('{')[0])
                    else:
                        self.cs_methods.append(line)
        cm.close()

    # reads and gets CS variables
    def csVar(self, filename):
        with open(filename) as csv:
            temp2 = []
            for line in csv:
                if 'for' in line:
                    None
                elif 'while' in line:
                    None
                elif 'if' in line:
                    None
                elif 'int ' in line and ';' in line:
                    line = line.strip()
                    if '=' in line:
                        line = line.rpartition('=')[0]
                        temp2.append(line)
                    else:
                        line = line.rpartition(';')[0]
                        temp2.append(line)
                elif 'char ' in line and ';' in line:
                    line = line.strip()
                    if '=' in line:
                        line = line.rpartition('=')[0]
                        temp2.append(line)
                    else:
                        line = line.rpartition(';')[0]
                        temp2.append(line)
                elif ('string ' in line or 'String ' in line) and ';' in line:
                    line = line.strip()
                    if '=' in line:
                        line = line.rpartition('=')[0]
                        temp2.append(line)
                    else:
                        line = line.rpartition(';')[0]
                        temp2.append(line)
                elif 'double ' in line and ';' in line:
                    line = line.strip()
                    if '=' in line:
                        line = line.rpartition('=')[0]
                        temp2.append(line)
                    else:
                        line = line.rpartition(';')[0]
                        temp2.append(line)
                elif 'float ' in line and ';' in line:
                    line = line.strip()
                    if '=' in line:
                        line = line.rpartition('=')[0]
                        temp2.append(line)
                    else:
                        line = line.rpartition(';')[0]
                        temp2.append(line)
                elif 'byte ' in line and ';' in line:
                    line = line.strip()
                    if '=' in line:
                        line = line.rpartition('=')[0]
                        temp2.append(line)
                    else:
                        line = line.rpartition(';')[0]
                        temp2.append(line)
                elif 'short ' in line and ';' in line:
                    line = line.strip()
                    if '=' in line:
                        line = line.rpartition('=')[0]
                        temp2.append(line)
                    else:
                        line = line.rpartition(';')[0]
                        temp2.append(line)
                elif 'long ' in line and ';' in line:
                    line = line.strip()
                    if '=' in line:
                        line = line.rpartition('=')[0]
                        temp2.append(line)
                    else:
                        line = line.rpartition(';')[0]
                        temp2.append(line)
                elif ('boolean ' in line or 'bool' in line) and ';' in line:
                    line = line.strip()
                    if '=' in line:
                        line = line.rpartition('=')[0]
                        temp2.append(line)
                    else:
                        line = line.rpartition(';')[0]
                        temp2.append(line)

        csv.close()
        var2 = set(temp2)
        for y in var2:
            self.cs_variables.append(y)

    # print in a tabular format
    def tcs(self, filename):
        c = open("Extractor.txt", "a")  # open a file for appending

        print('\n' + self.fCs(filename))
        c.write(self.fCs(filename) + '\n')  # print name of the file into a text file

        self.csClass(filename)  # function to seperate class
        self.csVar(filename)
        self.csMeth(filename)

        pdtabulate = lambda df: tabulate(df, headers=('Class', 'Methods', 'Variables'), tablefmt='psql')
        print(pdtabulate(it(self.cs_class, self.cs_methods, self.cs_variables)))
        c.write(pdtabulate(it(self.cs_class, self.cs_methods, self.cs_variables)) + '\n\n')

        self.cs_class.clear()
        self.cs_methods.clear()
        self.cs_variables.clear()

        c.close()