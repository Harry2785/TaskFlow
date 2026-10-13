
import sqlite3
import psycopg
from database import DATABASE_URL

# Read existing tasks from SQLite
sqlite_conn = sqlite3.connect("taskflow.db")

try:
    sqlite_cursor = sqlite_conn.cursor()
    sqlite_cursor.execute(
        "SELECT id, name, completed FROM tasks ORDER BY id"
    )
    tasks = sqlite_cursor.fetchall()
finally:
    sqlite_conn.close()

print(f"Found {len(tasks)} tasks in SQLite.")

# Copy tasks into PostgreSQL
with psycopg.connect(DATABASE_URL) as pg_conn:
    with pg_conn.cursor() as pg_cursor:
        for task_id, name, completed in tasks:
            pg_cursor.execute(
                """
                INSERT INTO tasks (id, name, completed)
                VALUES (%s, %s, %s)
                ON CONFLICT (id) DO NOTHING
                """,
                (task_id, name, bool(completed))
            )

        # Ensure future automatically generated IDs work correctly
        pg_cursor.execute("""
            SELECT setval(
                pg_get_serial_sequence('tasks', 'id'),
                COALESCE((SELECT MAX(id) FROM tasks), 1),
                EXISTS (SELECT 1 FROM tasks)
            )
        """)

print("Migration completed!")
