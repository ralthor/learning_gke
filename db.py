import psycopg2

conn = None

db_config = {
    'dbname': 'mydatabase',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'postgres_db',
    'port': 5432
}

def connect():
    global conn
    if conn:
        return conn
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS key_value (key varchar(255), value varchar(255));")
    conn.commit()
    cur.close()
    return conn

def store_db(key, value):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO key_value VALUES (%s, %s)", (key, value))
    conn.commit()
    cur.close()

def get_db(key):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT value FROM key_value WHERE key = %s", (key,))
    value = cur.fetchone()
    cur.close()
    return value[0] if value else None