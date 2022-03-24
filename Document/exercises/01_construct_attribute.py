from docarray import Document

######### id

# construct a Document with id 'j_1024'
d = Document(id="j_1024")
assert d.id == 'j_1024'

# id can have arbitrary data type, it is better to keep it as strings

######### main attributes
# construct a Document with text 'hello, jina'
d = Document(text="hello, jina")
assert d.text == 'hello, jina'

# construct a Document with a tensor [1, 2, 3]
d = Document(tensor=[1,2,3])
assert d.tensor == [1, 2, 3]

# construct a Document with blob b`123`
# reminder: blob = raw binary content of this document
d = Document(blob=b'hello, jina')
assert d.blob == b'hello, jina' 

# construct a Document with text 'hello, jina' and a blob [1, 2, 3]
"""
[CANNOT DO THIS!]
Answer: no, you can NOT do this, `text`, `blob` and `buffer` are mutually exclusive. A Document can have only one of them at the same time

d = Document(
    text='hello, jina',
    blob=[1,2,3]
)
"""
# assert d.text == 'hello, jina' and d.blob.shape == [1, 2, 3]

# construct a Document with tags={'name': 'jina', 'age': 2}
"""My notes:
this is a cool way you can use jinas ability to handle "unknown attributes"..namely, that if you try to construct a Jina document with an attribute that it doesn't have built in (tensor, blob, text, etc..) then it will automatically be "caught" in to the .tags attributes"""
d = Document(name="jina", age=2)
assert d.tags['name'] == 'jina'
assert d.tags['age'] == 2

######### Just messing around below. :)

from pydantic import BaseModel
from typing import Optional, List


class DoIWork(BaseModel):
    name: Optional[str] = "jina"
    age: Optional[int] = 2

pydantic_obj = DoIWork(name="jina", age=2)
d = Document(**pydantic_obj.dict())
assert d.tags['age'] == 2
