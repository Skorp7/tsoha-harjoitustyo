from db import db
from flask import session


def add(order_type_id, customer_id, delivery_date, clinic_id):
    try:
        sql = "INSERT INTO orders (order_type_id, customer_id, clinic_id, delivery_date, time) VALUES (:order_type_id, :customer_id, :clinic_id, :delivery_date, LOCALTIMESTAMP)"
        db.session.execute(sql, {"order_type_id":order_type_id, "customer_id":customer_id, "clinic_id":clinic_id, "delivery_date":delivery_date})
        db.session.commit()
        return True
    except:
        return False


def add_order_type(product_type, main_materials):
    try:
        sql = "INSERT INTO order_types (product_type, main_materials) VALUES (:product_type, :main_materials)"
        db.session.execute(sql, {"product_type":product_type,"main_materials":main_materials})
        db.session.commit()
        return True
    except:
        return False

def order_type_list():
    try:
        sql = "SELECT id, product_type, main_materials FROM order_types ORDER BY product_type"
        result = db.session.execute(sql)
        order_type_list = result.fetchall()
        return order_type_list
    except:
        return None


def update_delivery_date(new_datetime, order_id):
    try:
        sql = "UPDATE orders SET delivery_date=:delivery_date WHERE id=:id"
        db.session.execute(sql, {"delivery_date":new_datetime,"id":order_id})
        db.session.commit()
        return True
    except:
        return False

def user_status():
    id = session.get("user_id",0)
    sql = "SELECT status FROM users WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    status = result.fetchone()[0]
    return status
    
