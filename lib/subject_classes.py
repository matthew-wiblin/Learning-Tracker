#These classes define and control the subjects table in the database

class Subject:
    def __init__(self, id, subject_name, user_id):
        self.id = id
        self.subject_name = subject_name
        self.user_id = user_id
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
        
    def __repr__(self):
        return f"Subject({self.id}, {self.subject_name}, {self.user_id})"


class SubjectRepository:
    def __init__(self, connection):
        self.connection = connection

    def find_by_id(self, id):
        rows = self.connection.execute('SELECT * FROM subjects WHERE id = %s', [id])
        if rows:
            row = rows[0]
            return Subject(row['id'], row['subject_name'], row['user_id'])
        else:
            raise Exception("Subject not found!")

    def all(self):
        rows = self.connection.execute('SELECT * FROM subjects')
        subject_list = []
        for row in rows:
            current_subject = Subject(row['id'], row['subject_name'], row['user_id'])
            subject_list.append(current_subject)
        return subject_list
    
    def create(self, subject):
        rows = self.connection.execute(
            'INSERT INTO subjects (subject_name, user_id) VALUES (%s, %s) RETURNING id',
                                [subject.subject_name, subject.user_id])
        subject_id = rows[0]['id']
        return subject_id

    def update(self, subject):
        self.connection.execute(
            'UPDATE subjects SET subject_name = %s WHERE id = %s',
                                [subject.subject_name, subject.id])
        return subject.id

    def delete(self, id):
        self.connection.execute(
            'DELETE FROM subjects WHERE id = %s', [id]
        )