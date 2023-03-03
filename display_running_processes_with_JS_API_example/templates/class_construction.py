
class Tag:
    def __init__(self, open, close, lookfor_):
        self.open = open
        self.close = close
        self.lookfor_ = lookfor_
        
class JS_CSS(Tag):
    def __init__(self, open, close, lookfor_):
        super().__init__(open, close, lookfor_)
        self.paths = []
        self.code = ""
        
    def pather(self, path):
        self.paths.append(path)

    def return_paths(self):
        string = ''
        return ["\n".join(i) for i in self.paths]

    def read_file_(self, file):
        with open(file, 'r', errors="replace") as f:
            return f.read()
            
    def construction(self):
        string = f"{self.open}"
        for file in self.paths:
            string = str(string + self.read_file_(file) + "\n")
        self.code = str(string + f"{self.close}" + self.lookfor_)

class Html:
    def __init__(self):
        self.code = []

    def add_line(self, line):
        self.code.append(line)

    def join_lines(self):
        self.code = str("\n".join(self.code))


    

if __name__ == '__main__':
    js = JS_CSS('\n<script>\n', "\n</script>\n", r"</body>")
    js.pather('nadjgklkjasdfgksdlf')
    js.construction(["1.txt", "1.txt"])
    print(js.open)
    print(js.open)
    print(js.return_paths)

