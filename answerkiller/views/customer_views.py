from flask import Blueprint, request, g
from answerkiller import login_manager


customer_bp = Blueprint('Customer')