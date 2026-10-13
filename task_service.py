
from database import DATABASE_URL
import psycopg


def add_task(task):
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO tasks (name, completed)
                VALUES (%s, FALSE)
                RETURNING id
                """,
                (task,)
            )
            task_id = cursor.fetchone()[0]

    return task_id


def get_tasks():
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT id, name, completed FROM tasks ORDER BY id"
            )
            return cursor.fetchall()


def get_task(task_id):
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT id, name, completed FROM tasks WHERE id = %s",
                (task_id,)
            )
            return cursor.fetchone()


def delete_task(task_id):
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "DELETE FROM tasks WHERE id = %s",
                (task_id,)
            )


def complete_task(task_id):
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE tasks SET completed = TRUE WHERE id = %s",
                (task_id,)
            )
