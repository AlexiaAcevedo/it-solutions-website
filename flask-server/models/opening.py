from flask import jsonify
from mysqlconnection import connectToMySQL


class Opening:
    def __init__(self, data):
        self.id = data["id"]
        self.client = data["client"]
        self.poc = data["poc"]
        self.email = data["email"]
        self.role = data["role"]
        self.urgency = data["urgency"]
        self.quantity = data["quantity"]
        self.skills_needed = data["skills_needed"]


    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM openings;'
        results = connectToMySQL('data_piper').query_db(query)
        opening = []
        data = {}
        for result in results:
            data = {
                'id': result['id'],
                'client': result['client'],
                'poc': result['poc'],
                'email': result['email'],
                'role': result['role'],
                'urgency': result['urgency'],
                'quantity': result['quantity'],
                'skills_needed': result['skills_needed']
            }
            opening.append(data)
            data = {}
        return jsonify(opening)














