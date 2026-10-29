import os
import requests
from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
from functools import wraps
from html import escape

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET', 'boYii-fashion-secret-2026-abuja')

PAYSTACK_SECRET_KEY = os.environ.get('PAYSTACK_SECRET_KEY')
PAYSTACK_PUBLIC_KEY = os.environ.get('PAYSTACK_PUBLIC_KEY', 'pk_test_YOUR_KEY_HERE')
ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD')

PRODUCTS = [
    {"id": 1, "name": "Lagos Leather Loafers", "price": 45000, "image": "https://images.unsplash.com/photo-1614252235316-8c857d38bcca?w=500", "desc": "Handcrafted premium leather"},
    {"id": 2, "name": "Abuja Chic Heels", "price": 38000, "image": "https://images.unsplash.com/photo-1543163521-1bf539c55dd2?w=500", "desc": "Elegant evening heels"},
    {"id": 3, "name": "Zuma Rock Sneakers", "price": 52000, "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500", "desc": "Street style comfort"},
    {"id": 4, "name": "Naija Classic Oxfords", "price": 60000, "image": "https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=500", "desc": "Formal office wear"},
    {"id": 5, "name": "Wuse Market Sandals", "price": 25000, "image": "https://images.unsplash.com/photo-1603808033176-935819eb3a34?w=500", "desc": "Casual native style"},
    {"id": 6, "name": "Victory Boots", "price": 68000, "image": "https://images.unsplash.com/photo-1551107696-a4b0c5a0d9a2?w=500", "desc": "Durable & fashionable"},
]
ORDERS = []

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

@app.route('/')
def index():
    cart_count = len(session.get('cart', []))
    return
