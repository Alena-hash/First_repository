import urllib.parse
from sqlalchemy import create_engine, text

raw_password = "MK1*G7z!Z*@@F}."
safe_password = urllib.parse.quote_plus(raw_password)

db_url = f"postgresql://postgres:{safe_password}@localhost:5432/QA"
engine = create_engine(db_url)


def test_student_adds_subject():
    connection = engine.connect()
    transaction = connection.begin()
    connection.execute(text("INSERT INTO subject (subject_id, subject_title) VALUES (:id, :title)"),
                       {"id": 101, "title": "Автоматизация QA"})
    result = connection.execute(text("SELECT subject_title FROM subject WHERE subject_id = 101"))
    row = result.fetchone()
    assert row is not None, "Предмет не создался!"
    assert row.subject_title == "Автоматизация QA"
    connection.execute(text("DELETE FROM subject WHERE subject_id = 101"))
    transaction.commit()
    connection.close()


def test_student_updates_education_form():
    connection = engine.connect()
    transaction = connection.begin()
    connection.execute(
        text("INSERT INTO student (user_id, level, education_form, subject_id) VALUES (:u_id, :lvl, :form, :s_id)"),
        {"u_id": 777, "lvl": "Junior", "form": "Очная", "s_id": 1}
    )
    connection.execute(
        text("UPDATE student SET education_form = 'Дистанционная' WHERE user_id = 777")
    )
    res = connection.execute(text("SELECT education_form FROM student WHERE user_id = 777"))
    updated_row = res.fetchone()
    assert updated_row is not None
    assert updated_row.education_form == "Дистанционная"
    connection.execute(text("DELETE FROM student WHERE user_id = 777"))
    transaction.commit()
    connection.close()


def test_student_removes_user_account():
    connection = engine.connect()
    transaction = connection.begin()
    connection.execute(
        text("INSERT INTO users (user_id, user_email, subject_id) VALUES (:id, :email, :s_id)"),
        {"id": 999, "email": "test@student.ru", "s_id": 1}
    )
    connection.execute(text("DELETE FROM users WHERE user_id = 999"))
    check = connection.execute(text("SELECT count(*) FROM users WHERE user_id = 999"))
    assert check.scalar() == 0
    transaction.commit()
    connection.close()
