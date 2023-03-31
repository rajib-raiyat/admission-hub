import json
import uuid

import requests as requests
from flask import Flask, render_template, request, redirect

from database import session
from database.models import University, AdmissionGroup

app = Flask(__name__, template_folder='front-end/templates', static_folder='front-end/assets')


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/university-list")
def university():
    uni = session.query(University).all()

    data = []

    for i in uni:
        temp1 = []
        group = session.query(AdmissionGroup).filter_by(university_id=i.university_id).all()

        for j in group:
            t = {
                'admission_group_id': j.admission_group_id,
                'group_name': j.group_name,
                'exam_datetime': j.exam_datetime,
                'application_fee': j.application_fee,
            }
            temp1.append(t)

        temp = {
            'university_id': i.university_id,
            'university_name': i.university_name,
            'university_intro': i.university_intro,
            'university_image': i.university_image,
            'admission_group': temp1
        }

        data.append(temp)
    return render_template('list_uni.html', data=data)


@app.route("/confirm-form")
def confirm_form():
    data = request.args.get('data')
    print(data)
    return render_template('Form.html')


@app.route("/pay")
def pay():
    data = request.args.get('data')
    data = json.loads(data)

    total_amount = 0

    for i in data:
        amount = session.query(AdmissionGroup).filter_by(admission_group_id=i).first()
        total_amount += amount.application_fee

    payment_data = {
        'currency': 'BDT',
        'shipping_method': 'NO',
        'product_category': 'donation',
        'product_profile': 'general',
        'cus_postcode': 1200,
        'cus_add1': 'Dhaka',
        'cus_city': 'Dhaka',
        'store_id': 'admis6422b090c562a',
        'store_passwd': 'admis6422b090c562a@ssl',
        'success_url': f'http://127.0.0.1:5000/pay-success',
        'fail_url': f'http://127.0.0.1:5000/pay-failed',
        'cancel_url': f'http://127.0.0.1:5000/pay-cancle',
        'tran_id': uuid.uuid4(),
        'cus_name': 'halum',
        'cus_email': 'halum@admin.com',
        'cus_phone': '0155665220',
        'cus_country': 'BDT',
        'product_name': 'Admission Payment',
        'total_amount': str(total_amount)
    }

    payment = requests.post(
        'https://sandbox.sslcommerz.com/gwprocess/v4/api.php',
        data=payment_data
    )

    payment_response = payment.json()
    return redirect(payment_response['redirectGatewayURL'], code=302)


@app.route("/std-login")
def std_login():
    return render_template('LoginStu.html')


@app.route("/uni-login")
def uni_login():
    return render_template('LoginUni.html')
