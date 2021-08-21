from http import HTTPStatus
from flask import Blueprint, Response, request, render_template, url_for
from database.connect_db import connect 

products = Blueprint("products", __name__, url_prefix="/products")
shopCar = Blueprint("shopcar", __name__, url_prefix="/shopcar")

PRODUCTS_TITLE = "<h1> Products </h1>"
RESPONSE_BODY = {"message": "", "data": [], "errors": [], "metadata": []}

@products.route("/", methods=["GET"])
def show_product():
    conexion = connect()
    conexion.close()
    return PRODUCTS_TITLE, HTTPStatus.OK