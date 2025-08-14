from tqdm.notebook import tqdm
from pinecone import Pinecone


pc = Pinecone(api_key="API KEY")
index = pc.Index("secret-spots-travel")

