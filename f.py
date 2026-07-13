from sqlalchemy import create_engine, text

engine = create_engine(
    "mysql+pymysql://root:9211@localhost/cloudgpu_advisor"
)

with engine.connect() as conn:
    result = conn.execute(text("SELECT DATABASE()"))
    print("Current DB:", result.fetchone()[0])

    result = conn.execute(text("SHOW TABLES"))
    print("Tables:")
    for row in result:
        print(row)