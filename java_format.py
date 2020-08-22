from tabulate import tabulate
from itertools import zip_longest as it

class Java:

    # initialising a java class
    def __init__(self):
        pass

    java_class = []
    java_methods = []
    java_variables = []

    # getting a .java name from the directory name
    def fjava(self, filename):
        x = filename.rfind("/")
        y = filename.rfind('.java')
        return filename[(x + 1):(y + 5)]

    # reads and gets JAVA classes
    def javaClass(self, filename):
        with open(filename) as jc:
            for line in jc:
                if 'class' in line:
                    line = line.strip()
                    if '//' in line:
                        line = line.rpartition('//')[0]
                    elif '/*' in line:
                        line = line.rpartition('/*')[0]

                    if '{' in line:
                        self.java_class.append(line.rpartition('{')[0])
                    else:
                        self.java_class.append(line)

                if 'extends' in line:
                    line = line.strip()
                    if '//' in line:
                        line = line.rpartition('//')[0]
                    elif '/*' in line:
                        line = line.rpartition('/*')[0]

                    if '{' in line:
                        self.java_class.append(line.rpartition('{')[0])
                    else:
                        self.java_class.append(line)

                if 'main' in line:
                    line = line.strip()
                    if '//' in line:
                        line = line.rpartition('//')[0]
                    elif '/*' in line:
                        line = line.rpartition('/*')[0]

                    if '{' in line:
                        self.java_class.append(line.rpartition('{')[0])
                    else:
                        self.java_class.append(line)

                if 'interface' in line:
                    line = line.strip()
                    if '//' in line:
                        line = line.rpartition('//')[0]
                    elif '/*' in line:
                        line = line.rpartition('/*')[0]

                    if '{' in line:
                        self.java_class.append(line.rpartition('{')[0])
                    else:
                        self.java_class.append(line)

                if 'implements' in line:
                    line = line.strip()
                    if '//' in line:
                        line = line.rpartition('//')[0]
                    elif '/*' in line:
                        line = line.rpartition('/*')[0]

                    if '{' in line:
                        self.java_class.append(line.rpartition('{')[0])
                    else:
                        self.java_class.append(line)
        jc.close()

    # reads and gets JAVA methods
    def javaMeth(self, filename):
        with open(filename) as jm:
            for line in jm:

                if ('void' in line or 'private' in line or 'public' in line) and '(' in line and ')' in line and ';' not in line:
                    line = line.strip()

                    if '//' in line:
                        line = line.rpartition('//')[0]
                    elif '/*' in line:
                        line = line.rpartition('/*')[0]

                    if '{' in line:
                        self.java_methods.append(line.rpartition('{')[0])
                    else:
                        self.java_methods.append(line)
        jm.close()

    # reads and gets JAVA variables
    def javaVar(self, filename):
        with open(filename) as jv:
            temp = []
            for line in jv:
                if 'for' in line:
                    None
                elif 'while' in line:
                    None
                elif 'if' in line:
                    None
                elif (('int ' in line and ';' in line) or (
                        'int[' in line)) and 'Print' not in line and 'print' not in line:
                    line = line.strip()
                    if '=' in line:
                        line = line.rpartition('=')[0]
                        temp.append(line)
                    else:
                        line = line.rpartition(';')[0]
                        temp.append(line)
                elif 'char ' in line and ';' in line:
                    line = line.strip()
                    if '=' in line:
                        line = line.rpartition('=')[0]
                        temp.append(line)
                    else:
                        line = line.rpartition(';')[0]
                        temp.append(line)
                elif ('string ' in line or 'String ' in line) and ';' in line:
                    line = line.strip()
                    if '=' in line:
                        line = line.rpartition('=')[0]
                        temp.append(line)
                    else:
                        line = line.rpartition(';')[0]
                        temp.append(line)
                elif 'double ' in line and ';' in line:
                    line = line.strip()
                    if '=' in line:
                        line = line.rpartition('=')[0]
                        temp.append(line)
                    else:
                        line = line.rpartition(';')[0]
                        temp.append(line)
                elif 'float ' in line and ';' in line:
                    line = line.strip()
                    if '=' in line:
                        line = line.rpartition('=')[0]
                        temp.append(line)
                    else:
                        line = line.rpartition(';')[0]
                        temp.append(line)
                elif 'byte ' in line and ';' in line:
                    line = line.strip()
                    if '=' in line:
                        line = line.rpartition('=')[0]
                        temp.append(line)
                    else:
                        line = line.rpartition(';')[0]
                        temp.append(line)
                elif 'short ' in line and ';' in line:
                    line = line.strip()
                    if '=' in line:
                        line = line.rpartition('=')[0]
                        temp.append(line)
                    else:
                        line = line.rpartition(';')[0]
                        temp.append(line)
                elif 'long ' in line and ';' in line:
                    line = line.strip()
                    if '=' in line:
                        line = line.rpartition('=')[0]
                        temp.append(line)
                    else:
                        line = line.rpartition(';')[0]
                        temp.append(line)
                elif ('boolean ' in line or 'bool' in line) and ';' in line:
                    line = line.strip()
                    if '=' in line:
                        line = line.rpartition('=')[0]
                        temp.append(line)
                    else:
                        line = line.rpartition(';')[0]
                        temp.append(line)

        jv.close()
        var = set(temp)
        for elem in var:
            self.java_variables.append(elem)

    # Tabular print statement
    def tjava(self, filename):
        a = open("Extractor.txt", "a")  # open a file for appending

        print('\n' + self.fjava(filename))
        a.write(self.fjava(filename) + '\n')  # print name of the file into a text file

        self.javaClass(filename)  # function to separate class
        self.javaMeth(filename)
        self.javaVar(filename)

        pdtabulate = lambda df: tabulate(df, headers=('Class', 'Methods', 'Variables'), tablefmt='psql')
        print(pdtabulate(it(self.java_class, self.java_methods, self.java_variables)))
        a.write(pdtabulate(it(self.java_class, self.java_methods, self.java_variables)) + '\n\n')
        # print table data in a text file

        self.java_class.clear()
        self.java_methods.clear()
        self.java_variables.clear()

        a.close()
