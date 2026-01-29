import sqlite3
from datetime import datetime
import uuid

def collect_votes(prompt_id, user_id, score, comment=""):
    conn = sqlite3.connect('promptops.db')
    cursor = conn.cursor()
    
    vote_id = str(uuid.uuid4())
    cursor.execute("""
        INSERT INTO user_votes (id, prompt_id, user_id, score, comment, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        vote_id,
        prompt_id,
        user_id,
        score,
        comment,
        datetime.now()
    ))
    
    conn.commit()
    conn.close()
    
    return {"success": True, "vote_id": vote_id}