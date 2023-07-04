from flask import Blueprint, request, render_template, url_for
import csv
import math

store_bp = Blueprint('store', __name__)

@store_bp.route('/store/')
def store():
    page = request.args.get('page',default=1, type=int)

    data = []
    per_page = 10
    with open('store.csv', 'r', encoding='utf8') as file:
        csv_data = csv.DictReader(file)
        headers = [header.strip() for header in csv_data.fieldnames]
        for row in csv_data:
            data.append(row)    

    total_pages = math.ceil((len(data) / per_page)) 
    start_index = per_page * (page -1)
    end_index = start_index + per_page
    page_data = data[start_index:end_index]

    return render_template('store.html', headers=headers, page_data=page_data, total_pages=total_pages, url_for=url_for, current_page=page)

@store_bp.route('/store/<id>')
def user_detail(id):
    with open('store.csv', 'r', encoding='utf8') as file:
        csv_data = csv.DictReader(file)
        headers = [header.strip() for header in csv_data.fieldnames]
        for row in csv_data:
            if row['Id'] == id:
                user_data = row
                break
    return render_template('store_detail.html', user=user_data, headers=headers)