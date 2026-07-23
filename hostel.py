from database import get_connection

def save_entry(name):
    conn = get_connection()
    cursor = conn.cursor()

    sql = "INSERT INTO entry_logs(student_name, status) VALUES(%s, %s)"
    values = (name, "Access Granted")

    cursor.execute(sql, values)
    conn.commit()

    cursor.close()
    conn.close()