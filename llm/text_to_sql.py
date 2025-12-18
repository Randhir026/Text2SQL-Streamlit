def generate_sql(query: str) -> str:
    q = query.lower()

    # ---------------- Employees ----------------
    if "all employees" in q:
        return "SELECT * FROM employees;"

    if "employees in" in q and "department" in q:
        # Extract department name if possible
        if "engineering" in q:
            dept = "Engineering"
        elif "hr" in q:
            dept = "HR"
        elif "sales" in q:
            dept = "Sales"
        else:
            dept = ""
        if dept:
            return f"""
            SELECT e.id, e.name, e.email, e.salary
            FROM employees e
            JOIN departments d ON e.department_id = d.id
            WHERE d.name = '{dept}';
            """
        else:
            return """
            SELECT e.id, e.name, e.email, e.salary, d.name AS department
            FROM employees e
            JOIN departments d ON e.department_id = d.id;
            """

    if "highest salary" in q or "max salary" in q:
        return "SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 1;"

    if "lowest salary" in q or "min salary" in q:
        return "SELECT name, salary FROM employees ORDER BY salary ASC LIMIT 1;"

    if "average salary" in q:
        return "SELECT department_id, AVG(salary) as avg_salary FROM employees GROUP BY department_id;"

    # ---------------- Departments ----------------
    if "all departments" in q or "list departments" in q:
        return "SELECT * FROM departments;"

    # ---------------- Orders ----------------
    if "all orders" in q:
        return "SELECT * FROM orders;"

    if "orders by employee" in q:
        return """
        SELECT o.id, o.customer_name, o.order_total, o.order_date, e.name AS employee_name
        FROM orders o
        JOIN employees e ON o.employee_id = e.id;
        """

    if "orders for customer" in q:
        return "SELECT * FROM orders WHERE customer_name LIKE '%customer%';"

    if "highest order" in q or "largest order" in q:
        return "SELECT * FROM orders ORDER BY order_total DESC LIMIT 1;"

    if "total orders" in q:
        return "SELECT COUNT(*) AS total_orders FROM orders;"

    if "total sales" in q or "total revenue" in q:
        return "SELECT SUM(order_total) AS total_sales FROM orders;"

    # ---------------- Products ----------------
    if "all products" in q:
        return "SELECT * FROM products;"

    if "products above" in q:
        # Example: products above 500
        import re
        match = re.search(r'above (\d+)', q)
        if match:
            price = match.group(1)
            return f"SELECT * FROM products WHERE price > {price};"
        else:
            return "SELECT * FROM products;"

    if "products below" in q:
        match = re.search(r'below (\d+)', q)
        if match:
            price = match.group(1)
            return f"SELECT * FROM products WHERE price < {price};"
        else:
            return "SELECT * FROM products;"

    if "product details" in q or "product info" in q:
        return "SELECT * FROM products;"

    # ---------------- Fallback ----------------
    return "SELECT 'Query not understood';"
