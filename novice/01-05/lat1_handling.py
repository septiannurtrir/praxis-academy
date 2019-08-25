# Handling Stateful Objects

class TextReader:"""Print and number lines in a text file."""

def __init__(self, filename):
        self.filename = filename
        self.file = open(filename)
        self.lineno = 0

def readline(self):
        self.lineno += 1
        line = self.file.readline()
        if not line:
            return None
        if line.endswith('\n'):
            line = line[:-1]
        return "%i: %s" % (self.lineno, line)

def __getstate__(self):
        del state['file']
        return state 

def __setstate__(self, state):
        self.__dict__.update(state)
        file = open(self.filename)
        for _ in range(self.lineno):
            file.readline()
        self.file = file

reader = TextReader('Hello')
print(reader.readline())
print(reader.readline())
new_reader = pickle.loads(pickle.dumps(reader))
print(new_reader.readline())