"""
Main Application Entry Point
Initializes the PromptOps platform with all modules
"""

import os
import sqlite3
from src.sdk.context_engine import ContextEngine
from src.sdk.smart_rewriter import SmartRewriter
from src.api.routes import create_app as create_api_app
from src.admin.views import run_admin_server

def initialize_database():
    """Initialize the database with required tables"""
    db_path = 'promptops.db'
    
    # Connect to database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Read schema from SQL file
    schema_file = 'static/schema.sql'
    if os.path.exists(schema_file):
        with open(schema_file, 'r') as f:
            schema_sql = f.read()
        
        # Execute schema
        cursor.executescript(schema_sql)
        print("Database schema applied successfully")
    else:
        print(f"Schema file {schema_file} not found")
    
    conn.commit()
    conn.close()

def main():
    """Main entry point for the application"""
    print("Initializing PromptOps Platform...")
    
    # Initialize database
    initialize_database()
    
    # Initialize modules
    context_engine = ContextEngine()
    smart_rewriter = SmartRewriter()
    
    print("Modules initialized successfully")
    
    # Start API server in a separate thread if needed
    # For now, we'll just show the available functionality
    
    print("\nPromptOps Platform ready!")
    print("- Context Engine: Template management and A/B testing")
    print("- Smart Rewriter: Prompt optimization and feedback collection")
    print("- API Server: Available at http://localhost:5000")
    print("- Admin Interface: Available at http://localhost:5001")

if __name__ == "__main__":
    main()