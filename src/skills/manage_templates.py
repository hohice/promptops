import sqlite3
from datetime import datetime
import uuid

def manage_templates(action, template_data=None, template_id=None):
    conn = sqlite3.connect('promptops.db')
    cursor = conn.cursor()
    
    if action == "create":
        template_id = str(uuid.uuid4())
        cursor.execute("""
            INSERT INTO templates (id, name, description, template_content, created_at, updated_at, is_active)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            template_id,
            template_data['name'],
            template_data['description'],
            template_data['content'],
            datetime.now(),
            datetime.now(),
            True
        ))
        conn.commit()
        return {"success": True, "template_id": template_id}
        
    elif action == "get":
        cursor.execute("SELECT * FROM templates WHERE id = ?", (template_id,))
        result = cursor.fetchone()
        if result:
            return {
                "id": result[0],
                "name": result[1],
                "description": result[2],
                "content": result[3],
                "created_at": result[4],
                "updated_at": result[5],
                "is_active": result[6]
            }
        return None
        
    elif action == "update":
        cursor.execute("""
            UPDATE templates 
            SET name=?, description=?, template_content=?, updated_at=?
            WHERE id=?
        """, (
            template_data['name'],
            template_data['description'],
            template_data['content'],
            datetime.now(),
            template_id
        ))
        conn.commit()
        return {"success": True}
        
    elif action == "delete":
        cursor.execute("DELETE FROM templates WHERE id=?", (template_id,))
        conn.commit()
        return {"success": True}
        
    elif action == "list":
        cursor.execute("SELECT * FROM templates")
        results = cursor.fetchall()
        return [
            {
                "id": row[0],
                "name": row[1],
                "description": row[2],
                "content": row[3],
                "created_at": row[4],
                "updated_at": row[5],
                "is_active": row[6]
            } for row in results
        ]
    
    conn.close()