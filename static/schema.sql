-- Database Schema for PromptOps

-- Templates table
CREATE TABLE IF NOT EXISTS templates (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    template_content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT 1
);

-- Template versions table
CREATE TABLE IF NOT EXISTS template_versions (
    id TEXT PRIMARY KEY,
    template_id TEXT NOT NULL,
    version TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (template_id) REFERENCES templates (id)
);

-- A/B Tests table
CREATE TABLE IF NOT EXISTS ab_tests (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    variant_a_id TEXT,
    variant_b_id TEXT,
    sample_size INTEGER,
    duration_days INTEGER,
    status TEXT DEFAULT 'pending',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Evaluation logs table
CREATE TABLE IF NOT EXISTS evaluation_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    version_id TEXT,
    response TEXT,
    metrics_json TEXT,
    human_score REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Prompts table
CREATE TABLE IF NOT EXISTS prompts (
    id TEXT PRIMARY KEY,
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Optimized prompts table
CREATE TABLE IF NOT EXISTS optimized_prompts (
    id TEXT PRIMARY KEY,
    original_prompt_id TEXT,
    optimized_content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    improvement_score REAL,
    FOREIGN KEY (original_prompt_id) REFERENCES prompts (id)
);

-- User votes table
CREATE TABLE IF NOT EXISTS user_votes (
    id TEXT PRIMARY KEY,
    prompt_id TEXT,
    user_id TEXT,
    score INTEGER CHECK(score >= 1 AND score <= 5),
    comment TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (prompt_id) REFERENCES prompts (id)
);