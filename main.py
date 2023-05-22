import datetime
import json
import os
import uuid

import qrcode
import requests as requests
from PIL import Image, ImageOps
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import and_

from database import session
from database.models import University, AdmissionGroup, Applicants, Payment, Result

app = Flask(__name__, template_folder='front-end/templates', static_folder='front-end/assets')


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/university-list/<applicant_id>")
def university(applicant_id):
    applicant = session.query(Applicants).filter_by(applicant_id=applicant_id).first()

    uni = session.query(University).all()

    data = []

    for i in uni:
        temp1 = []
        group = session.query(AdmissionGroup).filter_by(university_id=i.university_id).filter(
            and_(AdmissionGroup.min_req < applicant.hsc_result, AdmissionGroup.hsc_group == applicant.hsc_group)
        ).all()

        for j in group:
            t = {
                'admission_group_id': j.admission_group_id,
                'group_name': j.group_name,
                'exam_datetime': j.exam_datetime,
                'application_fee': j.application_fee,
                'group': j.hsc_group,
                'min': j.min_req
            }
            temp1.append(t)

        if len(temp1):
            temp = {
                'university_id': i.university_id,
                'university_name': i.university_name,
                'university_intro': i.university_intro,
                'university_image': i.university_image,
                'admission_group': temp1
            }

            data.append(temp)

    return render_template('list_uni.html', data=data, applicant_id=applicant_id)


@app.route("/pay")
def pay():
    applicant_id = request.args.get('applicant_id')
    data = request.args.get('data')
    data_loads = json.loads(data)

    total_amount = 0

    for i in data_loads:
        amount = session.query(AdmissionGroup).filter_by(admission_group_id=i).first()
        total_amount += amount.application_fee

    tr = uuid.uuid4()
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
        'success_url': f'http://127.0.0.1:5000/pay-success?tr={tr}&d={",".join(data_loads)}&ap={applicant_id}',
        'fail_url': f'http://127.0.0.1:5000/pay-failed?tr={tr}',
        'cancel_url': f'http://127.0.0.1:5000/pay-cancel?tr={tr}',
        'tran_id': tr,
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

    session.add(Payment(**{
        'transaction_id': tr,
        'applicant_id': applicant_id,
        'student_id': applicant_id,
        'payment_amount': payment_data['total_amount'],
        'payment_status': 'PENDING',
        'payment_time': datetime.datetime.now(),
        'groups': data
    }))

    try:
        session.commit()
    except Exception:
        session.rollback()

    return redirect(payment_response['redirectGatewayURL'], code=302)


@app.route("/std-login")
def std_login():
    return render_template('LoginStu.html')


@app.route("/std-home")
def std_home():
    return render_template('homeStu.html')


@app.route("/uni-login")
def uni_login():
    return render_template('LoginUni.html')


@app.route("/pay-success", methods=['POST', 'GET'])
def pay_success():
    transaction_id = request.args.get('tr')
    data = request.args.get('d')
    ap = request.args.get('ap')

    session.query(Payment).filter_by(
        transaction_id=transaction_id
    ).update(
        {'payment_status': 'DONE'}
    )

    try:
        session.commit()
    except Exception:
        session.rollback()

    for i in data.split(','):
        application = session.query(AdmissionGroup).filter_by(admission_group_id=i).first()
        uni = session.query(University).filter_by(university_id=application.university_id).first()

        session.add(Result(**{
            'exam_id': uuid.uuid4(),
            'applicant_id': ap,
            'admission_group_id': i,
            'university_id': application.university_id,
            'university_name': uni.university_name,
            'exam_name': application.group_name
        }))

        try:
            session.commit()
        except Exception:
            session.rollback()

    return render_template('paySuccess.html')


def make_qr(data, store):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white")

    border_size = 10
    bordered_image = ImageOps.expand(qr_image, border=border_size, fill="black")

    logo_path = "front-end/assets/homepage-logo.PNG"
    logo_image = Image.open(logo_path)

    logo_size = (bordered_image.size[0] // 2, bordered_image.size[1] // 6)
    logo_image = logo_image.resize(logo_size)

    logo_position = (
        (bordered_image.size[0] - logo_image.size[0]) // 2, (bordered_image.size[1] - logo_image.size[1]) // 2)

    bordered_image.paste(logo_image, logo_position)

    os.makedirs(f"front-end/assets/applicant_image", exist_ok=True)
    bordered_image.save(f"front-end/assets/applicant_image/{store}-q.png")


@app.route("/download-admit-card", methods=['GET'])
def dow_admit_card():
    transaction_id = request.args.get('tr')

    group = session.query(Payment).filter_by(transaction_id=transaction_id).first()

    data = []
    for i in json.loads(group.groups):
        g = session.query(AdmissionGroup).filter_by(admission_group_id=i).first()
        u = session.query(University).filter_by(university_id=g.university_id).first()

        temp = {
            'exam_name': f'{u.university_name} ({g.group_name})',
            'exam_date': g.exam_datetime,
            'exam_time': g.exam_time,
            'exam_venue': g.exam_venue
        }
        data.append(temp)

    sorted_data = sorted(data, key=lambda x: datetime.datetime.strptime(x['exam_date'], '%d %B, %Y'))
    applicant = session.query(Applicants).filter_by(applicant_id=group.applicant_id).first()

    data = f"http://127.0.0.1:5000/download-admit-card?tr={transaction_id}"
    make_qr(data=data, store=group.applicant_id)

    return render_template('admit_card.html', data=sorted_data, applicant_name=applicant.name,
                           applicant_id=applicant.applicant_id)


@app.route("/pay-failed", methods=['POST'])
def pay_failed():
    transaction_id = request.args.get('tr')

    session.query(Payment).filter_by(
        transaction_id=transaction_id
    ).update(
        {'payment_status': 'FAILED'}
    )

    try:
        session.commit()
    except Exception:
        session.rollback()

    return render_template('payFailed.html')


@app.route("/confirm-form")
def confirm_form():
    hsc_roll = request.args.get('hscRoll')
    hsc_reg = request.args.get('hscReg')
    hsc_year = request.args.get('hscYear')
    hsc_board = request.args.get('hscBoard')

    get_applicant = session.query(Applicants).filter_by(
        hsc_roll=hsc_roll,
        hsc_reg=hsc_reg,
        hsc_board=hsc_board,
        hsc_year=hsc_year
    ).first()

    if not get_applicant:
        return render_template('common-error.html', error_message='No applicant found')

    if get_applicant.username and get_applicant.password:
        return render_template('common-error.html', error_message='Already have a account please login.')

    return render_template('Form.html', data=get_applicant)


@app.route("/create-user")
def create_user():
    applicant_id = request.args.get('userId')
    username = request.args.get('username')
    password = request.args.get('pass')

    if not username or not password or not applicant_id:
        return render_template('common-error.html', error_message='No username or password found.')

    check_username = session.query(Applicants).filter_by(username=username).first()
    if check_username:
        return render_template('common-error.html', error_message='username already exists!')

    get_applicant = session.query(Applicants).filter_by(
        applicant_id=applicant_id
    ).first()

    if get_applicant.username and get_applicant.password:
        return render_template('common-error.html', error_message='Already have a account please login.')

    session.query(Applicants).filter_by(
        applicant_id=applicant_id
    ).update(
        {'username': username, 'password': password}
    )

    try:
        session.commit()
    except Exception:
        session.rollback()

    return redirect(url_for('university', applicant_id=applicant_id))


@app.route('/res-stu')
def res_stu():
    applicant_id = request.args.get('apid')

    get_applicant = session.query(Applicants).filter_by(
        applicant_id=applicant_id
    ).first()

    if not get_applicant:
        return render_template('common-error.html', error_message='No student found.')

    result = session.query(Result).filter_by(applicant_id=applicant_id).all()

    return render_template(
        'homeStu.html',
        result=result,
        applicant_name=get_applicant.name,
        applicant_id=get_applicant.applicant_id
    )


@app.route("/check-res")
def check_res():
    username = request.args.get('username')
    password = request.args.get('pass')

    if not username or not password:
        return render_template('common-error.html', error_message='No username or password input found.')

    check_username = session.query(Applicants).filter_by(username=username).first()
    if not check_username:
        return render_template('common-error.html', error_message='Username or password wrong.')

    if check_username.password != password:
        return render_template('common-error.html', error_message='Username or password wrong.')

    return redirect(f'http://127.0.0.1:5000/res-stu?apid={check_username.applicant_id}')


@app.route('/upload', methods=['POST'])
def upload_image():
    os.makedirs('front-end/assets/applicant_image', exist_ok=True)

    applicant_id = request.args.get('fn')
    image = request.files['image']

    image.save(f'front-end/assets/applicant_image/{applicant_id}')
    return 'Image uploaded successfully!'
