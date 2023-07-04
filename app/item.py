from flask import Blueprint, request, render_template, url_for
import csv
import math

item_bp = Blueprint('item', __name__)

@item_bp.route('/item/')
def item():
    page = request.args.get('page', default=1, type=int)

    data = []
    per_page = 10
    with open('item.csv', 'r', encoding='utf8') as file:
        csv_data = csv.DictReader(file)
        headers = [header.strip() for header in csv_data.fieldnames]
        for row in csv_data:
            data.append(row)

    total_pages = math.ceil((len(data)) / per_page)
    start_index = per_page * (page -1)
    end_index = start_index + per_page
    page_data = data[start_index:end_index]

    return render_template('item.html', headers=headers, total_pages=total_pages, page_data=page_data, url_for=url_for, current_page=page)

@item_bp.route('/item/<id>')
def item_detail(id):
    with open('item.csv', 'r', encoding='utf8') as file:
        csv_data = csv.DictReader(file)
        headers = [header.strip() for header in csv_data.fieldnames]
        for row in csv_data:
            if row['Id'] == id:
                user_data = row
                break
    
    return render_template('item_detail.html', user=user_data, headers=headers)
