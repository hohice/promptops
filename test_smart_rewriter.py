"""
Test script specifically for Smart Rewriter Module
"""

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

from src.main import initialize_database
from src.sdk.smart_rewriter import SmartRewriter, generate_optimization, collect_votes, get_analytics


def test_smart_rewriter():
    print("Testing Smart Rewriter Module...")
    
    # Initialize database
    initialize_database()
    print("✓ Database initialized")
    
    # Test Smart Rewriter
    smart_rewriter = SmartRewriter()
    print("✓ Smart Rewriter initialized")
    
    # Generate optimization
    optimization_result = generate_optimization(
        original_prompt="Write a compelling product description for a new smartphone.",
        context={"target_audience": "tech enthusiasts", "tone": "professional"},
        performance_data={"previous_score": 0.7}
    )
    print(f"✓ Optimization generated: {optimization_result['improvement_score']} improvement score")
    
    # Collect votes
    vote_result = collect_votes(
        prompt_id=optimization_result['optimization_id'],  # Using optimization ID as prompt ID
        user_id="user123",
        score=4,
        comment="Good improvement, but could be more concise."
    )
    print(f"✓ Vote collected: {vote_result}")
    
    # Get analytics
    analytics = get_analytics()
    print("✓ Analytics retrieved:")
    print(f"  - Total optimizations: {analytics['optimization_metrics']['total_optimizations']}")
    print(f"  - Average improvement: {analytics['optimization_metrics']['average_improvement']}")
    print(f"  - Total votes: {analytics['vote_metrics']['total_votes']}")
    print(f"  - Average score: {analytics['vote_metrics']['average_score']}")
    print(f"  - Total prompts: {analytics['prompt_metrics']['total_prompts']}")
    
    # Test Smart Rewriter instance methods
    instance_result = smart_rewriter.generate_optimization(
        original_prompt="Create a marketing slogan for an eco-friendly cleaning product.",
        context={"focus": "environmental benefits", "style": "catchy"}
    )
    print(f"✓ Instance optimization: {instance_result['improvement_score']} improvement score")
    
    instance_analytics = smart_rewriter.get_analytics()
    print(f"✓ Instance analytics retrieved: {len(instance_analytics)} metric categories")
    
    print("\nSmart Rewriter Module tests completed successfully!")


if __name__ == "__main__":
    test_smart_rewriter()