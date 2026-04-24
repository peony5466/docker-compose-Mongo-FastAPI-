from fastapi import FastAPI
import mysql.connector
from pymongo import MongoClient
import os, time

app = FastAPI()

def get_mysql():
    for i in range(10):
        try:
            return mysql.connector.connect(
                host='db_mysql',
                user='root',
                password=os.environ.get('MYSQL_ROOT_PASSWORD'),
                database=os.environ.get('MYSQL_DATABASE')
            )
        except:
            time.sleep(3)
    raise Exception('MySQL indisponible')

def get_mongo():
    return MongoClient(os.environ.get('MONGO_URI'))

@app.get('/posts')
def get_posts():
    client = get_mongo()
    posts = list(client['blog_db'].posts.find({}, {'_id': 0}))
    client.close()
    return posts

@app.get('/users')
def get_users():
    conn = get_mysql()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return users

@app.get('/health')
def health():
    try:
        get_mysql()
        get_mongo()['blog_db'].posts.find_one()
        return {'status': 'OK'}
    except Exception as e:
        return {'status': 'KO', 'error': str(e)}
