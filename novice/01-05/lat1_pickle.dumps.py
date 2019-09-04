# pickle.dump(obj,file,protocol = None,*,fix_imports = True)
# Python program to illustrate
# pickle.dump()

import pickle
from StringIO import StringIO

class SimpleObject(object):
    def __init__(self, name):
        self.name = name
        l = list(name)
        l.reverse()
        self.name_backwards = ''.join(l)
        return

data = []
data.append(SimpleObject('pickle'))
data.append(SimpleObject('cPickle'))
data.append(SimpleObject('last'))

out_s = StringIO()

for o in data:
    print ('WRITING: %s (%s)' % (o.name_backwards)
    pickle.dump(out_s, o)
    out_s.flush()