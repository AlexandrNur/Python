import pytest
from sqlalchemy import create_engine, text

# Конфигурация подключения к базе данных
db_connection_string = "postgresql://postgres:999@localhost:5432/postgres"
db = create_engine(db_connection_string)


@pytest.fixture(scope='function')
def connection():
    """Создает соединение для каждого теста."""
    connection = db.connect()
    transaction = connection.begin()
    yield connection
    transaction.commit()
    connection.close()


def test_insert_student(connection):
    """Тест на добавление нового студента."""
    sql_insert = text("INSERT INTO student(\"user_id\", \"level\", \"education_form\", \"subject_id\") VALUES (:user_id, :level, :education_form, :subject_id)")
    connection.execute(sql_insert, {"user_id": "123", "level": "Beginner", "education_form": "group", "subject_id": "1"})

    # Проверка, что запись добавлена
    sql_select = text("SELECT * FROM student WHERE user_id = :user_id")
    result = connection.execute(sql_select, {"user_id": "123", "level": "Beginner", "education_form": "group", "subject_id": "1"}).fetchone()
    assert result is not None


def test_update_student(connection):
    """Тест на обновление имени студента."""
    sql_update = text("UPDATE student SET education_form = :new_form WHERE user_id = :user_id")
    connection.execute(sql_update, {"new_form": 'personal', "user_id": 123})

    # Проверка обновления
    sql_select = text("SELECT * FROM student WHERE education_form = :new_form")
    result = connection.execute(sql_select, {"new_form": "personal"}).fetchone()
    assert result is not None


def test_delete_student(connection):
    """Тест на удаление студента."""
    sql_delete = text("DELETE FROM student WHERE user_id = :user_id")
    connection.execute(sql_delete, {"user_id": 123})

    # Проверка удаления
    sql_select = text("SELECT * FROM student WHERE user_id = :user_id")
    result = connection.execute(sql_select, {"user_id": "123"}).fetchone()
    assert result is None
