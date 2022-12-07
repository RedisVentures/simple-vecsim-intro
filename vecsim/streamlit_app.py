import os
import logging
import numpy as np
import pandas as pd
import streamlit as st

from redis import Redis
from redis.commands.search.query import Query
from utils.embeddings import Embeddings

host = os.getenv("REDIS_HOST", default="redis")
port = os.getenv("REDIS_PORT", default=6379)
pwd = os.getenv("REDIS_PWD", default="")
index_name = "papers"
redis = Redis(host=host, port=port, password=pwd)


@st.cache(allow_output_mutation=True)
def get_embedding_model():
    return Embeddings()

embeddings = get_embedding_model()

st.title("Redis Vector Similarity Search")

with st.expander("About this demo:", expanded=False):
    st.markdown(
    """
    ## Vector Similarity Search

    This demo allows you to search the subset of arXiv scholarly articles with natural language. Under the surface, Redis uses [vector similarity search](https://mlops.community/vector-similarity-search-from-basics-to-production/).
    """
    )

user_query = st.text_input("Query:", "intelligent autonomous vehicles")
logging.info(f"search string: {user_query}")

q = Query("*=>[KNN 10 @vector $vector AS score]")\
    .return_fields("score", "title")\
    .dialect(2)\
    .sort_by("score", True)

query_vector = embeddings.make(user_query).astype(np.float32).tobytes()

res = redis.ft(index_name).search(
    q, query_params={"vector": query_vector})

df = pd.DataFrame([t.__dict__ for t in res.docs])

df["score"] = df["score"].apply(lambda s: 1 - float(s))
df["link"] = df["id"].apply(lambda i: f"https://arxiv.org/pdf/{i.split(':')[1]}")

st.table(df[["title", "score", "link"]])
