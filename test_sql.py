import pymysql

try:
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="9211",
        database="cloudgpu_advisor"
    )

    print("Connection Successful!")

    conn.close()

except Exception as e:
    print("Error:")
    print(e)