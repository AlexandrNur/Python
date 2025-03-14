from sqlalchemy import create_engine, text


class DatabaseOperations:
    def __init__(self, db_connection_string):
        self.engine = create_engine(db_connection_string)

    def add_student(self, user_id, level, education_form, subject_id):
        sql_insert = text("INSERT INTO student (user_id, level, education_form, subject_id) VALUES (:user_id, :level, :education_form, :subject_id)")
        with self.engine.connect() as conn:
            conn.execute(sql_insert, {
                "user_id": user_id,
                "level": level,
                "education_form": education_form,
                "subject_id": subject_id
            })
            conn.commit()  # Фиксация транзакции

    def update_student(self, user_id, new_form):
        sql_update = text(
            "UPDATE student SET education_form = :new_form WHERE user_id = :user_id"
        )
        with self.engine.connect() as conn:
            conn.execute(sql_update, {
                "new_form": new_form,
                "user_id": user_id
            })
            conn.commit()  # Фиксация транзакции

    def delete_student(self, user_id):
        sql_delete = text(
            "DELETE FROM student WHERE user_id = :user_id"
        )
        with self.engine.connect() as conn:
            conn.execute(sql_delete, {"user_id": user_id})
            conn.commit()  # Фиксация транзакции
