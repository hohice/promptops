"""
API Routes Module
REST API endpoints for the promptops platform
"""

from flask import Flask, request, jsonify
from src.sdk.context_engine import ContextEngine, list_templates, create_template, get_template, update_template, delete_template, execute_ab_test
from src.sdk.smart_rewriter import SmartRewriter, generate_optimization, collect_votes


def create_app():
    app = Flask(__name__)
    
    # Context Engine API routes
    @app.route('/templates', methods=['GET'])
    def get_templates():
        """List all context templates"""
        templates = list_templates()
        return jsonify(templates)

    @app.route('/templates', methods=['POST'])
    def create_new_template():
        """Create a new context template"""
        data = request.json
        result = create_template(
            name=data['name'],
            description=data.get('description', ''),
            content=data['content']
        )
        return jsonify(result)

    @app.route('/templates/<template_id>', methods=['GET'])
    def get_single_template(template_id):
        """Get a specific template"""
        template = get_template(template_id)
        if template:
            return jsonify(template)
        return jsonify({'error': 'Template not found'}), 404

    @app.route('/templates/<template_id>', methods=['PUT'])
    def update_existing_template(template_id):
        """Update an existing template"""
        data = request.json
        result = update_template(
            template_id=template_id,
            name=data.get('name'),
            description=data.get('description'),
            content=data.get('content')
        )
        return jsonify(result)

    @app.route('/templates/<template_id>', methods=['DELETE'])
    def delete_existing_template(template_id):
        """Delete a template"""
        result = delete_template(template_id)
        return jsonify(result)

    @app.route('/ab-test', methods=['POST'])
    def run_ab_test():
        """Run an A/B test on context strategies"""
        data = request.json
        result = execute_ab_test(
            config=data['config'],
            variant_a=data['variant_a'],
            variant_b=data['variant_b']
        )
        return jsonify(result)

    @app.route('/optimize', methods=['POST'])
    def optimize_prompt():
        """Optimize a prompt"""
        data = request.json
        result = generate_optimization(
            original_prompt=data['prompt'],
            context=data.get('context'),
            performance_data=data.get('performance_data')
        )
        return jsonify(result)

    @app.route('/votes', methods=['POST'])
    def submit_vote():
        """Submit a vote on a prompt"""
        data = request.json
        result = collect_votes(
            prompt_id=data['prompt_id'],
            user_id=data['user_id'],
            score=data['score'],
            comment=data.get('comment', '')
        )
        return jsonify(result)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)