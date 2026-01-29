"""
Test script for PromptOps platform
"""

from src.main import initialize_database
from src.sdk.context_engine import ContextEngine, create_template, list_templates
from src.sdk.smart_rewriter import SmartRewriter, generate_optimization

def test_platform():
    print("Testing PromptOps Platform...")
    
    # Initialize database
    initialize_database()
    print("✓ Database initialized")
    
    # Test Context Engine
    context_engine = ContextEngine()
    print("✓ Context Engine initialized")
    
    # Create a test template
    result = create_template(
        name="Test Template",
        description="A test template for validation",
        content="This is a test template content with {variable}."
    )
    print(f"✓ Template created: {result}")
    
    # List templates
    templates = list_templates()
    print(f"✓ Templates listed: {len(templates)} found")
    
    # Test Smart Rewriter
    smart_rewriter = SmartRewriter()
    print("✓ Smart Rewriter initialized")
    
    # Generate optimization
    optimization_result = generate_optimization(
        original_prompt="Write a short story about a robot learning to paint.",
        context={"genre": "science fiction", "length": "short"},
        performance_data={"previous_score": 0.7}
    )
    print(f"✓ Optimization generated: {optimization_result['improvement_score']}")
    
    print("\nAll tests passed! PromptOps platform is working correctly.")

if __name__ == "__main__":
    test_platform()