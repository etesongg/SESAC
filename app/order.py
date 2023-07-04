from flask import Blueprint, request, render_template, url_for
import csv
import math

order_bp = Blueprint('order', __name__)

@order_bp.route('/order/')
def order():
    page = request.args.get('page', default=1, type=int)

    data = []
    per_page = 10
    with open('order.csv', 'r', encoding='utf8') as file:
        csv_data = csv.DictReader(file)
        headers = [header.strip() for header in csv_data.fieldnames]
        for row in csv_data:
            data.append(row)

    total_pages = math.ceil((len(data)) / per_page)
    start_index = per_page * (page -1)
    end_index = start_index + per_page
    page_data = data[start_index:end_index]

    return render_template('order.html', headers=headers, page_data=page_data, total_pages=total_pages, url_for=url_for, current_page=page)