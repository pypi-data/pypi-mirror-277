def sqlEng():
    import argparse
    import mysql.connector
    from LLM_Text_to_SQL import TextToSQL 
 
    db_config = {
        print("host:"): input("localhost"),
        print("user:"): input("your_username"),
        print("password:"): input("your_password"),
        print("database:"): input("your_database"),
    }

    #NLP English Query
    english_instruction = input("Input Your English Instruction Here: ")
    def execute_query(query, db_config):
        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            for row in results:
                print(row)
        except mysql.connector.Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

    def main():
        parser = argparse.ArgumentParser(description="Execute SQL queries via CLI")
        parser.add_argument("query", help="SQL query to execute")
        args = parser.parse_args()

        # Initialize English-based Query Writer
        converter = TextToSQL()
        sql_query = converter.convert(english_instruction)

        execute_query(sql_query, db_config)

    if __name__ == "__main__":
        main()

    return
