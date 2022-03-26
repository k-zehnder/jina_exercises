

Christian Klose  1:29 PM
If I attached each sentence to the document as a chunk. How could i retrieve the document by searching for similar texts (chunks) ?


7 replies
Last reply 9 days agoView thread

Vito  1:42 PM
Hello everyone, maybe it is a very easy question but how do I delete an indexed document, any example?



5 replies
Last reply 9 days agoView thread

Kevin Chan  10:15 AM
Hello everyone, I'm new to Jina.
Can I send an HTTP request payload to the Jina for search images?
Here is my code:
from docarray import DocumentArray
from jina import Client, requests, Flow

@requests(on='/index')
def index(self, docs: DocumentArray, **kwargs):
    self._index.extend(docs)


@requests(on='/search')
def search(self, docs: DocumentArray, **kwargs):
    docs.match(self._index)


f = (
    Flow(cors=True, port_expose=12345, protocol="http")
    .add(uses='docker://image_encoder', name="Encoder")
    .add(uses='docker://simple_indexer', name="Indexer")
)

f.to_docker_compose_yaml()

da = DocumentArray.from_files('/data/images/*.jpg')

with f:
    f.post("/index", inputs=da, show_progress=True)


def print_matches(resp):
    resp.docs.plot_image_sprites()
    for doc in resp.docs:
        for idx, d in enumerate(doc.matches[:3]): 
            print(f'[{idx}]{d.scores["cosine"].value:2f}')

with f:
    c = Client(protocol="http", port=12345) 
    c.post("/search", inputs=da.shuffle[0], on_done=print_matches)
    
    # block
    f.block()