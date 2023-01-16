import sqlite3


class Database:
    connection = None

    def __init__(self) -> None:
        pass

    def connect(self) -> sqlite3.Connection | None:
        try:
            self.connection = sqlite3.connect(
                'database.sqlite3', check_same_thread=False)
            print("Database connected")
            return self.connection
        except Exception as e:
            print("Database connection failed", e)
            return None

    def prepareDatabase(self):
        try:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY NOT NULL,
                    name TEXT NOT NULL,
                    content TEXT NOT NULL,
                    createdAt timestamp NOT NULL,
                    updatedAt timestamp NOT NULL
                );
            """)

            self.connection.commit()

            print("Database preparation successful")
        except Exception as e:
            print("Database preparation failed")
            print(e)
            if self.connection:
                self.connection.close()
