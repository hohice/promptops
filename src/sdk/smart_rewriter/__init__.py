"""
Smart Rewriter Module
Provides prompt optimization and user feedback collection capabilities
"""

from src.skills.generate_optimization import generate_optimization as skill_generate_optimization
from src.skills.collect_votes import collect_votes as skill_collect_votes
import sqlite3


class SmartRewriter:
    def __init__(self):
        """Initialize the Smart Rewriter module"""
        pass

    def generate_optimization(self, original_prompt, context=None, performance_data=None):
        """Generate an optimized version of a prompt"""
        return skill_generate_optimization(original_prompt, context, performance_data)

    def collect_votes(self, prompt_id, user_id, score, comment=""):
        """Collect user feedback and votes on prompt quality"""
        return skill_collect_votes(prompt_id, user_id, score, comment)

    def get_analytics(self):
        """Get optimization analytics and performance metrics"""
        conn = sqlite3.connect('promptops.db')
        cursor = conn.cursor()
        
        # Get statistics about optimized prompts
        cursor.execute("""
            SELECT 
                COUNT(*) as total_optimizations,
                AVG(improvement_score) as avg_improvement,
                MAX(improvement_score) as max_improvement,
                MIN(improvement_score) as min_improvement
            FROM optimized_prompts
        """)
        optimization_stats = cursor.fetchone()
        
        # Get vote statistics
        cursor.execute("""
            SELECT 
                COUNT(*) as total_votes,
                AVG(score) as avg_score,
                MAX(score) as max_score,
                MIN(score) as min_score
            FROM user_votes
        """)
        vote_stats = cursor.fetchone()
        
        # Get prompt statistics
        cursor.execute("""
            SELECT 
                COUNT(*) as total_prompts
            FROM prompts
        """)
        prompt_stats = cursor.fetchone()
        
        conn.close()
        
        analytics = {
            'optimization_metrics': {
                'total_optimizations': optimization_stats[0] if optimization_stats[0] else 0,
                'average_improvement': round(optimization_stats[1], 2) if optimization_stats[1] else 0.0,
                'max_improvement': round(optimization_stats[2], 2) if optimization_stats[2] else 0.0,
                'min_improvement': round(optimization_stats[3], 2) if optimization_stats[3] else 0.0
            },
            'vote_metrics': {
                'total_votes': vote_stats[0] if vote_stats[0] else 0,
                'average_score': round(vote_stats[1], 2) if vote_stats[1] else 0.0,
                'max_score': vote_stats[2] if vote_stats[2] else 0,
                'min_score': vote_stats[3] if vote_stats[3] else 0
            },
            'prompt_metrics': {
                'total_prompts': prompt_stats[0] if prompt_stats[0] else 0
            }
        }
        
        return analytics


# Convenience functions
def generate_optimization(original_prompt, context=None, performance_data=None):
    rewriter = SmartRewriter()
    return rewriter.generate_optimization(original_prompt, context, performance_data)


def collect_votes(prompt_id, user_id, score, comment=""):
    rewriter = SmartRewriter()
    return rewriter.collect_votes(prompt_id, user_id, score, comment)


def get_analytics():
    rewriter = SmartRewriter()
    return rewriter.get_analytics()