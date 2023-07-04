from flask import Blueprint, request, render_template, url_for
import csv
import math
from functions.read_csv import read_csv

store_bp = Blueprint('store', __name__)

@store_bp.route('/store/')
def store():
    page = request.args.get('page',default=1, type=int)

    per_page = 10

    headers, data = read_csv('store.csv')
    
    total_pages = math.ceil((len(data) / per_page)) 
    start_index = per_page * (page -1)
    end_index = start_index + per_page
    page_data = data[start_index:end_index]

    return render_template('store.html', headers=headers, page_data=page_data, total_pages=total_pages, url_for=url_for, current_page=page)

@store_bp.route('/store/<id>')
def user_detail(id):
    headers, data = read_csv('store.csv')

    for row in data:
        if row['Id'] == id:
            user_data = row
            break
    return render_template('store_detail.html', user=user_data, headers=headers)