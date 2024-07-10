from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
import os
from src.document_search.search import crawl_directory

def create_index(directory, excluded_dir_names, included_extensions, index_dir):
    if not os.path.exists(index_dir):
        os.makedirs(index_dir)
    
    schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
    idx = create_in(index_dir, schema)
    writer = idx.writer()
    
    for filepath in crawl_directory(directory, excluded_dir_names, included_extensions):
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            writer.add_document(title=os.path.basename(filepath), path=filepath, content=content)
    
    writer.commit()

