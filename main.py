import duckdb


def main():
    duckdb.sql("SELECT 42").show()


if __name__ == "__main__":
    main()
