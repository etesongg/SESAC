from flask import Blueprint, request, render_template, url_for
import csv
import math
from functions.read_csv import read_csv

item_bp = Blueprint('item', __name__)

@item_bp.route('/item/')
def item():
    page = request.args.get('page', default=1, type=int)

    per_page = 10

    headers, data = read_csv('item.csv')

    total_pages = math.ceil((len(data)) / per_page)
    start_index = per_page * (page -1)
    end_index = start_index + per_page
    page_data = data[start_index:end_index]

    return render_template('item.html', headers=headers, total_pages=total_pages, page_data=page_data, url_for=url_for, current_page=page)

@item_bp.route('/item/<id>')
def item_detail(id):
    headers, data = read_csv('item.csv')
    for row in data:
        if row['Id'] == id:
            user_data = row
            break
    
    return render_template('item_detail.html', user=user_data, headers=headers)
