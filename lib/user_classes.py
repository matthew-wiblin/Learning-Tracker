#These classes define and control the user table in the database

class User:
    def __init__(self, id, email_address, username, password):
        self.id = id
        self.email_address = email_address
        self.username = username
        self.password = password
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
        
    def __repr__(self):
        return f"User({self.id}, {self.email_address}, {self.username}, {self.password})"


class UserRepository:
    def __init__(self, connection):
        self.connection = connection #Initialise with a database connection
        self.users = []

    def find_by_id(self, id):
        rows = self.connection.execute('SELECT * FROM users WHERE id = %s',[id])
        if rows:
            row = rows[0]
            return User(row['id'], row['email_address'], row['username'], row['password'])
        else:
            raise Exception("User not found!")

    def all(self):
        rows = self.connection.execute('SELECT * FROM users')
        user_list = []
        for row in rows:
            current_user = User(row['id'], row['email_address'], row['username'], row['password'])
            user_list.append(current_user)
        return user_list
    
    def create(self, user):
        rows = self.connection.execute(
            'INSERT INTO users (email_address, username, password) Values(%s, %s, %s) RETURNING id',
                                [user.email_address, user.username, user.password])
        user_id = (rows[0])['id']
        return user_id

    def update(self, user):
        self.connection.execute(
            'UPDATE users SET email_address = %s, username = %s, password = %s WHERE id = %s',
                                [user.email_address, user.username, user.password, user.id])
        return user.id

    def delete(self, id):
        self.connection.execute(
            'DELETE FROM users WHERE id = %s', [id]
        )