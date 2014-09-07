from flask import Blueprint, request, g
from answerkiller import loginmanager


admin_bp = Blueprint('Admin', subdomain='admin')