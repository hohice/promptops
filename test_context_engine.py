"""
Test script specifically for Context Engine Module
"""

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

from src.main import initialize_database
from src.sdk.context_engine import ContextEngine, create_template, list_templates, optimize_templates


def test_context_engine():
    print("Testing Context Engine Module...")
    
    # Initialize database
    initialize_database()
    print("✓ Database initialized")
    
    # Test Context Engine
    context_engine = ContextEngine()
    print("✓ Context Engine initialized")
    
    # Create a test template
    result = create_template(
        name="Test Context Template",
        description="A test context template for validation",
        content="This is a context template with {variable} that needs optimization."
    )
    print(f"✓ Template created: {result}")
    
    # List templates
    templates = list_templates()
    print(f"✓ Templates listed: {len(templates)} found")
    
    # Test context template optimization
    if templates:
        template_ids = [templates[0]['id']]  # Use the first template ID
        optimization_results = optimize_templates(
            template_ids=template_ids,
            context={
                "purpose": "context optimization",
                "target_audience": "developers",
                "style_guide": "professional tone"
            }
        )
        print(f"✓ Context template optimization completed: {len(optimization_results)} optimizations")
        for result in optimization_results:
            print(f"  - Template {result['template_id']}: {result['optimization_result']['improvement_score']} improvement score")
    
    # Test context optimization without specifying template IDs (should optimize all active templates)
    all_optimization_results = optimize_templates(context={
        "purpose": "context optimization",
        "target_audience": "developers"
    })
    print(f"✓ Context optimization for all active templates: {len(all_optimization_results)} optimizations")
    
    print("\nContext Engine Module tests completed successfully!")


if __name__ == "__main__":
    test_context_engine()