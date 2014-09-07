from flask import Blueprint, request, g
from answerkiller import loginmanager


customer_bp = Blueprint('Customer')