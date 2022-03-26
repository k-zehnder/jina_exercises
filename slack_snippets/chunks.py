from pprint import pprint

import numpy as np

from docarray import Document, DocumentArray

c1 = Document(text='hello', embedding=np.array([1, 2, 3]))
c2 = Document(text='world', embedding=np.array([4, 5, 6]))
d1 = Document(text='hello, world blah blah!', chunks=[c1, c2])
d1.display()

c3 = Document(text='hallo', embedding=np.array([1, 2, 3]))
c4 = Document(text='welt', embedding=np.array([4, 5, 6]))
d2 = Document(text='hallo, welt ja ja!', chunks=[c3, c4])
d2.display()

database = DocumentArray([d1, d2])
database.summary()

for m in database['@c'].find(np.array([1, 2, 3])):
    pprint(m.to_dict(exclude_none=True))

    # use match's parent id to access the original parent
    print(database[m.parent_id])

    # you can also accumulate score from chunk-level back to parent-level
    ...