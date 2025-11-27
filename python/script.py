# contoh connect dengan postgres python mengunakan psycopg2

import psycopg2
from psycopg2 import sql

def connect_to_postgres(host, database, user, password):
    try:
        # Membuat koneksi ke database PostgreSQL
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        print("Koneksi berhasil")
        return connection
    except Exception as e:
        print(f"Gagal terhubung ke database: {e}")
        return None
    
def close_connection(connection):
    if connection:
        connection.close()
        print("Koneksi ditutup")

if __name__ == "__main__":
    # Ganti dengan informasi koneksi Anda
    host = "localhost"
    database = "training_day_3"
    user = "postgres"
    password = "bewe123"
    conn = connect_to_postgres(host, database, user, password)

    # Lakukan operasi database di sini
    # menampilkan data semua table

    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
            """)
            tables = cursor.fetchall()
            print("Daftar tabel di database:")
            for table in tables:
                print(table[0])
        except Exception as e:
            print(f"Terjadi kesalahan saat mengambil data tabel: {e}")
        finally:
            cursor.close()
            close_connection(conn)
    
    