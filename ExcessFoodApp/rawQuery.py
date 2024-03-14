from django.db import connection

def get_Data(user_id):
    raw_query = """
        SELECT orders.id, orders.order_id, orders.food_id, foods.donor_id, foods.name, orders.user_id FROM orders 
JOIN Foods ON orders.food_id = foods.id
WHERE orders.is_rated = 0 and orders.user_id = %s 
ORDER BY orders.id DESC
    """
 
    with connection.cursor() as cursor:
        cursor.execute(raw_query, [user_id])
        results = cursor.fetchall()
 
    # Convert the results to a list of dictionaries
    columns = [col[0] for col in cursor.description]  # type: ignore
    data = [dict(zip(columns, row)) for row in results]
 
    return data

def get_user_ratings(user_id):  # type: ignore
    raw_query = """
       SELECT ratings.id, ratings.order_id, foods.name AS food_name, foods.image AS image, donors.name AS donor_name, ratings.ratings, ratings.description
       FROM ratings 
       JOIN foods ON ratings.food_id = foods.id 
       JOIN donors ON ratings.donor_id = donors.id
       WHERE ratings.user_id = %s
       ORDER BY ratings.id DESC
    """
 
    with connection.cursor() as cursor:
        cursor.execute(raw_query, [user_id])
        results = cursor.fetchall()
 
    # Convert the results to a list of dictionaries
    columns = [col[0] for col in cursor.description]  # type: ignore
    data = [dict(zip(columns, row)) for row in results]
 
    return data

def get_request_data():
    raw_query = """
SELECT users.name AS user_name, users.contact, requests.food_name, requests.food_type, requests.quantity, requests.date, requests.description FROM requests
JOIN users ON requests.user_id = users.id
WHERE requests.req_type = 1
    """
 
    with connection.cursor() as cursor:
        cursor.execute(raw_query)
        results = cursor.fetchall()
 
    # Convert the results to a list of dictionaries
    columns = [col[0] for col in cursor.description]  # type: ignore
    data = [dict(zip(columns, row)) for row in results]
 
    return data

def get_request_money():
    raw_query = """
SELECT users.name AS user_name, users.contact, requests.food_name, requests.food_type, requests.image, requests.quantity, requests.date, requests.description FROM requests
JOIN users ON requests.user_id = users.id
WHERE requests.req_type = 2
    """
 
    with connection.cursor() as cursor:
        cursor.execute(raw_query)
        results = cursor.fetchall()
 
    # Convert the results to a list of dictionaries
    columns = [col[0] for col in cursor.description]  # type: ignore
    data = [dict(zip(columns, row)) for row in results]
 
    return data

def get_ratings(donor_id):
    print(donor_id)
    raw_query = """
        SELECT ROUND(AVG(ratings.ratings), 1) AS rating, donors.name AS donor_name, donors.id
        FROM ratings
        JOIN foods ON foods.id = ratings.food_id
        JOIN donors ON donors.id = foods.donor_id
        WHERE donors.id = %s
        GROUP BY donors.id, donors.name;
    """

    with connection.cursor() as cursor:
        cursor.execute(raw_query, [donor_id])
        results = cursor.fetchall()

    # Convert the results to a list of dictionaries
    columns = [col[0] for col in cursor.description]  # type: ignore
    data = [dict(zip(columns, row)) for row in results]

    # if not data:
    #     return None  # or return a specific value, or raise an exception

    # rating = data[0]['rating']
    # print(rating)

    return data