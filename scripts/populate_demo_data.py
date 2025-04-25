import psycopg2
import os

conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME", "teacherai"),
    user=os.getenv("DB_USER", "postgres"),
    password=os.getenv("DB_PASS", "postgres"),
    host=os.getenv("DB_HOST", "localhost"),
    port="5432"
)

cur = conn.cursor()
cur.execute("INSERT INTO submissions (student_id, submission_text, score, feedback) VALUES (%s, %s, %s, %s)", (
    "u987654", "This is a demo document.", 90, "Great structure and arguments."
))
conn.commit()
cur.close()
conn.close()
