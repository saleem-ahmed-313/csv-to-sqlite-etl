import csv
import sqlite3


# --------------------- Extractor ---------------------
class Extractor:
    def __init__(self,file_path):
        self.file_path = file_path

    def extract(self):
        with open(self.file_path,"r") as f:
            reader = csv.DictReader(f)
            data = list(reader)
        return data 

# ----------------------- Transformer ------------------
class Transformer :
    def transform(self,data):
        clean_data = []
        for row in data:
            name = row["name"].strip() if row["name"] else "Unknown"
            age = int(row["age"]) if row["age"].isdigit() else None
            city = row["city"].strip() if row["city"] else "Unknown"

            clean_data.append({"name":name,"age":age,"city":city})
        return clean_data
    

# -------------- Loader ---------------------------
class Loader:
    def __init__(self,db_name="etl_demo.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()
        
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS people(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            city TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def load(self,data):
        query = "INSERT INTO people (name ,age , city) VALUES (?, ?, ?)"
        for row in data:
            self.conn.execute(query,(row["name"],row["age"],row["city"]))
            print(f"Inserted into DB: {row}")
        self.conn.commit()

    def fetch_all(self):
        cursor = self.conn.execute("SELECT * FROM people")
        return cursor.fetchall()
    
    

   

# -------------------- ETL Pipeline ------------------------
class ETLPipeline:
    def __init__(self,extractor,transformer,loader):
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader

    def run(self):
        raw = self.extractor.extract()
        print("\n[Extracted Data]",raw)

        clean = self.transformer.transform(raw)
        print("\n[Transformered Data]",clean)

        self.loader.load(clean)
        print("\n[Database State]",self.loader.fetch_all())

# ------------------------- Run the Pipeline --------------------
if __name__ =="__main__":
    extractor = Extractor("input.csv")
    transformer = Transformer()
    loader = Loader()

    pipeline = ETLPipeline(extractor,transformer,loader)
    pipeline.run()
