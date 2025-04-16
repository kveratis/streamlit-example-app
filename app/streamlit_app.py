import streamlit as st
import pandas as pd
import mysql.connector
import os

UPLOAD_FOLDER = "/app/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Connect to MySQL
def get_db_connection():
    return mysql.connector.connect(
        host="mysql_db",
        user="root",
        password="password",
        database="test_db"
    )

# Display Data
def fetch_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test_table")
    rows = cursor.fetchall()
    conn.close()
    return pd.DataFrame(rows, columns=["ID", "Name", "Age"])

# Save the uploaded file
def write_file(uploaded_file):
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

# Insert Data into MySQL Table
def insert_data(df):
    conn = get_db_connection()
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute(
            "INSERT INTO test_table (name, age) VALUES (%s, %s)", 
            (row['Name'], row['Age'])
        )

    conn.commit()
    conn.close()

# Streamlit UI
st.title("MySQL Streamlit App")

if st.button("Load Data"):
    df = fetch_data()
    st.write(df)

uploaded_file = st.file_uploader("Upload a file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    if "Name" in df.columns and "Age" in df.columns:
        file_path = write_file(uploaded_file)
        st.success(f"File saved to {file_path}")
        insert_data(df)
        st.success("Data inserted successfully!")

        st.write("Uploaded Data:")
        st.write(df)
    else:
        st.error("CSV must contain 'Name' and 'Age' columns.")
  