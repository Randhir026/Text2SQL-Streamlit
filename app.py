import streamlit as st
import psycopg2
from sentence_transformers import SentenceTransformer
from llm.text_to_sql import generate_sql
from utils.sql_validator import is_safe_sql

st.title("🔍 Natural Language Database Search")

embedder = SentenceTransformer("all-MiniLM-L6-v2")

conn = psycopg2.connect(
    dbname="vocso",
    user="postgres",
    password="Randhir@1#",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

query = st.text_input("Ask a question (e.g. products similar to mouse)")

if st.button("Search") and query:
    if "similar" in query.lower():
        vector = embedder.encode(query).tolist()
        cur.execute(
            "SELECT name, price FROM products ORDER BY embedding <-> %s LIMIT 3",
            (vector,)
        )
        st.table(cur.fetchall())
    else:
        sql = generate_sql(query)
        st.code(sql, language="sql")
        if is_safe_sql(sql):
            cur.execute(sql)
            st.table(cur.fetchall())
        else:
            st.error("Unsafe SQL detected")

cur.close()
conn.close()
