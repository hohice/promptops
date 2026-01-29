import sqlite3
import random
from datetime import datetime
import uuid

def run_ab_test(config, variant_a, variant_b):
    conn = sqlite3.connect('promptops.db')
    cursor = conn.cursor()
    
    # Create test record
    test_id = str(uuid.uuid4())
    cursor.execute("""
        INSERT INTO ab_tests (id, name, variant_a_id, variant_b_id, sample_size, duration_days, status, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        test_id,
        config['name'],
        str(uuid.uuid4()),  # variant_a_id
        str(uuid.uuid4()),  # variant_b_id
        config['sample_size'],
        config['duration_days'],
        'running',
        datetime.now()
    ))
    
    # Simulate A/B test execution
    results = {
        'test_id': test_id,
        'variant_a_performance': random.uniform(0.7, 0.95),
        'variant_b_performance': random.uniform(0.7, 0.95),
        'winner': 'variant_a' if random.random() > 0.5 else 'variant_b',
        'confidence': random.uniform(0.8, 0.99)
    }
    
    conn.commit()
    conn.close()
    
    return results