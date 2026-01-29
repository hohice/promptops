"""
Admin Views Module
Flask-Admin templates for managing the promptops platform
"""

from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlite3
import os

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'promptops-admin-secret-key'

# Setup database connection
DATABASE_PATH = os.path.abspath('promptops.db')
engine = create_engine(f'sqlite:///{DATABASE_PATH}')
Session = sessionmaker(bind=engine)
session = Session()

# Create admin interface
admin = Admin(app, name='PromptOps Admin', template_mode='bootstrap3')

# Define model views for different entities
class TemplateView(ModelView):
    column_list = ('id', 'name', 'description', 'created_at', 'is_active')
    column_filters = ['name', 'is_active', 'created_at']
    form_columns = ['name', 'description', 'template_content', 'is_active']

class ABTestView(ModelView):
    column_list = ('id', 'name', 'status', 'created_at', 'duration_days')
    column_filters = ['name', 'status', 'created_at']
    form_columns = ['name', 'variant_a_id', 'variant_b_id', 'sample_size', 'duration_days', 'status']

class VoteView(ModelView):
    column_list = ('id', 'prompt_id', 'user_id', 'score', 'timestamp')
    column_filters = ['user_id', 'score', 'timestamp']
    form_columns = ['prompt_id', 'user_id', 'score', 'comment']

class OptimizedPromptView(ModelView):
    column_list = ('id', 'original_prompt_id', 'improvement_score', 'created_at')
    column_filters = ['improvement_score', 'created_at']
    form_columns = ['original_prompt_id', 'optimized_content', 'improvement_score']


def init_admin_views():
    """Initialize admin views"""
    # We'll add views dynamically based on available models
    print("Admin views initialized")


def run_admin_server():
    """Start the admin server"""
    app.run(debug=True, host='0.0.0.0', port=5001)


if __name__ == '__main__':
    run_admin_server()