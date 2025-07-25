from flask import Blueprint, request, jsonify
from app.db import get_db

api_bp = Blueprint('api', __name__)

@api_bp.route('/users', methods=['GET'])
def get_users():
    db = get_db()
    cursor = db.cursor()
    users = cursor.execute('SELECT * FROM users').fetchall()
    return jsonify([dict(row) for row in users])

@api_bp.route('/users', methods=['POST'])
def post_users():
    db = get_db()
    cursor = db.cursor()
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    db.commit()

    return jsonify({'message': 'User created successfully'}), 201

@api_bp.route('/claim/<int:user_id>', methods=['POST'])
def claim_points(user_id):
    """
    Claim random points
    ---
    parameters:
      - in: path
        name: user_id
        type: integer
        required: true
        description: ID of the user
    responses:
      201:
        description: Points claimed successfully
    """
    db = get_db()
    cursor = db.cursor()

    user = cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    if not user:
        return jsonify({'error': 'User not found'}), 404

    import random
    points = random.randint(1, 100)

    cursor.execute('INSERT INTO claims (user_id, points) VALUES (?, ?)', (user_id, points))
    db.commit()

    return jsonify({'message': f'User {user_id} claimed {points} points'}), 201

@api_bp.route('/history/<int:user_id>', methods=['GET'])
def claim_history(user_id):
    """
    Get claim history
    ---
    parameters:
      - in: path
        name: user_id
        type: integer
        required: true
        description: ID of the user
    responses:
      200:
        description: List of claim history
        schema:
          type: array
          items:
            properties:
              points:
                type: integer
              claimed_at:
                type: string
    """
    db = get_db()
    cursor = db.cursor()

    claims = cursor.execute(
        'SELECT points, claimed_at FROM claims WHERE user_id = ? ORDER BY claimed_at DESC',
        (user_id,)
    ).fetchall()

    return jsonify([dict(row) for row in claims]), 200
