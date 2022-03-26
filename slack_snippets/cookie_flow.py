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