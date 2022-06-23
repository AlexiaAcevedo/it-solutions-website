from mysqlconnection import connectToMySQL

class Candidate:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.opening_id = data['opening_id']



    @classmethod
    def save(cls, data):
        query = 'INSERT INTO candidates ( first_name, last_name, email, opening_id ) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(opening_id)s );'
        results = connectToMySQL('data_piper').query_db(query, data)
        return results
