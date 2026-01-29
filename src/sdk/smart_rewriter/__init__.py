"""
Smart Rewriter Module
Provides prompt optimization and user feedback collection capabilities
"""

from src.skills.generate_optimization import generate_optimization as skill_generate_optimization
from src.skills.collect_votes import collect_votes as skill_collect_votes


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


# Convenience functions
def generate_optimization(original_prompt, context=None, performance_data=None):
    rewriter = SmartRewriter()
    return rewriter.generate_optimization(original_prompt, context, performance_data)


def collect_votes(prompt_id, user_id, score, comment=""):
    rewriter = SmartRewriter()
    return rewriter.collect_votes(prompt_id, user_id, score, comment)