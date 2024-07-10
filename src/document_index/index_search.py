from whoosh.index import open_dir
from whoosh.qparser import QueryParser

def search_index(query_str, index_dir):
    idx = open_dir(index_dir)
    parser = QueryParser("content", schema=idx.schema)
    
    with idx.searcher() as searcher:
        query = parser.parse(query_str)
        results = searcher.search(query, limit=None)
        return [(result['title'], result['path']) for result in results]
