def is_safe_sql(sql: str) -> bool:
    blocked = ["DROP", "DELETE", "TRUNCATE", "ALTER"]
    sql_upper = sql.upper()
    return not any(word in sql_upper for word in blocked)
