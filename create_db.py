import sqlite3
import pandas as pd

def create_table_from_csv(csv_file, db_file="database.db"):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Load CSV data into pandas DataFrame
    df = pd.read_csv(csv_file)
    
    # Dynamically create a table based on the DataFrame
    table_name = csv_file.split('/')[-1].split('.')[0]
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    
    conn.commit()
    conn.close()
    print(f"Database created from {csv_file}.")

if __name__ == "__main__":
    create_table_from_csv("data/sample_data.csv")
