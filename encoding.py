from tqdm.notebook import tqdm
import numpy as np
import pandas as pd
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document as langChainDocument


with open("Secret Spots Travel Dataset.txt", "r") as f:
  data = f.read()

data[:100]



raw_database = langChainDocument(page_content=data)

MARKDOWN_SEPARATORS = [
    "\n#{1,6} ",
    "```\n",
    "\n\\*\\*\\*+\n",
    "\n---+\n",
    "\n___+\n",
    "\n\n",
    "\n",
    " ",
    "",
]



text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100,
    add_start_index=True,
    strip_whitespace=True,
    separators=MARKDOWN_SEPARATORS,
)

docs_processed = text_splitter.split_documents([raw_database])

upsert_data = []

for i, entry in tqdm(enumerate(docs_processed)):
    text = entry.page_content
    vector = embedding_model.embed_query(text)
    upsert_data.append(
        {
            "id": "vec{}".format(i),
            "values": vector,
            "metadata": {"text": text}
        }
    )

index.upsert(
    vectors=upsert_data,
    namespace= "ns1"
)



