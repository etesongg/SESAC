from flask import Blueprint, request, render_template, url_for
import csv
import math
from functions.read_csv import read_csv
from functions.calc_pages import calc_pages

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
def index():
    page = request.args.get('page', default=1, type=int)
    search_name = request.args.get('name', default ="", type=str).strip() 
    search_gender = request.args.get('gender', default="", type=str)

    per_page = 10

    # csv 파일 읽기
    headers, data = read_csv('user.csv')

    # 검색 결과에 따른 데이터 보여주기
    filter_data = []
    if search_name: 
        if search_gender: 
            for row in data:
                if search_name in row['Name'] and search_gender in row['Gender']: # search_name 값 O, search_gneder 값 O
                    filter_data.append(row)
        else:
            for row in data:
                if search_name in row['Name']: # search_name 값 O, search_gneder 값 x
                    filter_data.append(row)     
    else: 
        if search_gender:
            for row in data:
                if search_gender in row['Gender']: # search_name 값 x, search_gneder 값 O
                    filter_data.append(row)
        else: # search_name 값 x, search_gneder 값 x
            filter_data = data

    # 페이지 계산

    total_pages, page, page_data = calc_pages(filter_data, per_page, page)

    
    return render_template('users.html', headers=headers, page_data=page_data, total_pages=total_pages, search_name=search_name, search_gender=search_gender, url_for=url_for, current_page=page)

@user_bp.route('/user/<id>')
def user_detail(id):
    headers, data = read_csv('user.csv')

    for row in data:
        if row['Id'] == id:
            user_data = row
            break
    return render_template('user_detail.html', user=user_data, headers=headers)