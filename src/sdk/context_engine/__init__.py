"""
Context Engine Module
Provides template management and A/B testing capabilities
"""

from src.skills.manage_templates import manage_templates
from src.skills.run_ab_test import run_ab_test


class ContextEngine:
    def __init__(self):
        """Initialize the Context Engine module"""
        pass

    def create_template(self, name, description, content):
        """Create a new context template"""
        template_data = {
            'name': name,
            'description': description,
            'content': content
        }
        return manage_templates('create', template_data)

    def get_template(self, template_id):
        """Retrieve a specific template by ID"""
        return manage_templates('get', template_id=template_id)

    def update_template(self, template_id, name=None, description=None, content=None):
        """Update an existing template"""
        # Get current template data
        current = self.get_template(template_id)
        if not current:
            raise ValueError(f"Template with ID {template_id} not found")

        # Prepare updated data
        template_data = {
            'name': name or current['name'],
            'description': description or current['description'],
            'content': content or current['content']
        }

        return manage_templates('update', template_data, template_id)

    def delete_template(self, template_id):
        """Delete a template by ID"""
        return manage_templates('delete', template_id=template_id)

    def list_templates(self):
        """List all templates"""
        return manage_templates('list')

    def run_ab_test(self, config, variant_a, variant_b):
        """Run an A/B test between two variants"""
        return run_ab_test(config, variant_a, variant_b)


# Convenience functions
def create_template(name, description, content):
    engine = ContextEngine()
    return engine.create_template(name, description, content)


def get_template(template_id):
    engine = ContextEngine()
    return engine.get_template(template_id)


def update_template(template_id, name=None, description=None, content=None):
    engine = ContextEngine()
    return engine.update_template(template_id, name, description, content)


def delete_template(template_id):
    engine = ContextEngine()
    return engine.delete_template(template_id)


def list_templates():
    engine = ContextEngine()
    return engine.list_templates()


def execute_ab_test(config, variant_a, variant_b):
    engine = ContextEngine()
    return engine.run_ab_test(config, variant_a, variant_b)