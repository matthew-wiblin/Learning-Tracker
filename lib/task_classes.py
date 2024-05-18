#These classes define and control the subjects table in the database

class Task:
    def __init__(self, id, task_name, task_description, completed, subject_id):
        self.id = id
        self.task_name = task_name
        self.task_description = task_description
        self.completed = completed
        self.subject_id = subject_id
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
        
    def __repr__(self):
        return f"Task({self.id}, {self.task_name}, {self.task_description}, {self.completed}, {self.subject_id})"


class TaskRepository:
    def __init__(self, connection):
        self.connection = connection

    def find_by_id(self, id):
        rows = self.connection.execute('SELECT * FROM tasks WHERE id = %s', [id])
        if rows:
            row = rows[0]
            return Task(row['id'], row['task_name'], row['task_description'], row['completed'], row['subject_id'])
        else:
            raise Exception("Task not found!")

    def all(self):
        rows = self.connection.execute('SELECT * FROM tasks')
        task_list = []
        for row in rows:
            current_task = Task(row['id'], row['task_name'], row['task_description'], row['completed'], row['subject_id'])
            task_list.append(current_task)
        return task_list
    
    def create(self, task):
        rows = self.connection.execute(
            'INSERT INTO tasks (task_name, task_description, completed, subject_id) VALUES (%s, %s, %s, %s) RETURNING id',
                                [task.task_name, task.task_description, task.completed, task.subject_id])
        task_id = rows[0]['id']
        return task_id

    def update(self, task):
        self.connection.execute(
            'UPDATE tasks SET task_name = %s, task_description = %s, completed = %s WHERE id = %s',
                                [task.task_name, task.task_description, task.completed, task.id])
        return task.id

    def delete(self, id):
        self.connection.execute(
            'DELETE FROM tasks WHERE id = %s', [id]
        )