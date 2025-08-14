from tqdm.notebook import tqdm
from pinecone import Pinecone

pc = Pinecone(api_key="pcsk_2MDRdN_QG1fjj4Ywh4pHnmcvyoJJ4abak9bmgExHPk4UxEBzzEc9yod4cGXXusY8aRYikM")
index = pc.Index("secret-spots-travel")

