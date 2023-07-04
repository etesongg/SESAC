from flask import Blueprint, request, render_template, url_for
import csv
import math
from functions.read_csv import read_csv

orderitem_bp = Blueprint('orderitem', __name__)

@orderitem_bp.route('/orderitem/')
def orderitem():
    page = request.args.get('page', default=1, type=int)

    per_page = 10

    headers, data = read_csv('orderitem.csv')

    total_pages = math.ceil((len(data)) / per_page)
    start_index = per_page * (page -1)
    end_index = start_index + per_page
    page_data = data[start_index:end_index]

    return render_template('orderitem.html', headers=headers, page_data=page_data, total_pages=total_pages, url_for=url_for, current_page=page)