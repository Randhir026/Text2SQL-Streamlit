from sentence_transformers import SentenceTransformer
import psycopg2

model = SentenceTransformer("all-MiniLM-L6-v2")

conn = psycopg2.connect(
    dbname="vocso",
    user="postgres",
    password="Randhir@1#",
    host="localhost",
    port="5432"
)

cur = conn.cursor()
cur.execute("SELECT id, name FROM products")

for pid, name in cur.fetchall():
    emb = model.encode(name).tolist()
    cur.execute(
        "UPDATE products SET embedding = %s WHERE id = %s",
        (emb, pid)
    )

conn.commit()
cur.close()
conn.close()

print("✅ Embeddings generated")
