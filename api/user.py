import os
import psycopg2
import json

def handler(request):
    if request.method != "GET":
        return {
            "statusCode": 405,
            "body": json.dumps({"error": "Method not allowed"})
        }

    try:
        # Vercel automatically provides DATABASE_URL
        conn = psycopg2.connect(os.environ["DATABASE_URL"])
        cur = conn.cursor()

        # Example query
        cur.execute("SELECT id, name, email FROM users LIMIT 1;")
        row = cur.fetchone()

        cur.close()
        conn.close()

        if row:
            user = {
                "id": row[0],
                "name": row[1],
                "email": row[2]
            }
        else:
            user = None

        return {
            "statusCode": 200,
            "body": json.dumps(user)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
