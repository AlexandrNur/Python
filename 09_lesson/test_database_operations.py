from database_operations import DatabaseOperations
from sqlalchemy import create_engine, text
import pytest


# Конфигурация подключения к базе данных
db_connection_string = "postgresql://postgres:999@localhost:5432/postgres"
db_operations = DatabaseOperations(db_connection_string)


@pytest.fixture(scope='function')
def connection():
    """Создает соединение для каждого теста."""
    engine = create_engine(db_connection_string)
    connection = engine.connect()
    transaction = connection.begin()
    yield connection
    transaction.rollback()  # Откат транзакции после теста
    connection.close()


def test_insert_student(connection):
    """Тест на добавление нового студента."""
    db_operations.add_student(99999, "Beginner", "group", 1)

    # Проверка, что запись добавлена
    sql_select = text("SELECT * FROM student WHERE user_id = :user_id")
    result = connection.execute(sql_select, {"user_id": 99999}).fetchone()
    assert result is not None
    assert result[1] == 'Beginner'  # Предполагаем, что вторая колонка - "level".
    assert result[2] == 'group'     # Третья колонка - "education_form".
    assert result[3] == 1           # Четвертая колонка - "subject_id".


def test_update_student(connection):
    """Тест на обновление формы обучения студента."""
    db_operations.update_student(99999, "group")

    # Проверка обновления
    sql_select = text("SELECT * FROM student WHERE user_id = :user_id")
    result = connection.execute(sql_select, {"user_id": 99999}).fetchone()
    assert result[2] == 'group'  # Проверка колонки "education_form".


def test_delete_student(connection):
    """Тест на удаление студента."""
    # Добавляем тестового студента заранее
    db_operations.delete_student(99999)

    # Проверка удаления
    sql_select = text("SELECT * FROM student WHERE user_id = :user_id")
    result = connection.execute(sql_select, {"user_id": 99999}).fetchone()
    assert result is None
