import random
import string
import uuid
from datetime import timedelta, datetime
from random import randint
from uuid import uuid4

from database import session
from database.models import Applicants, University, AdmissionGroup


def random_with_n_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return str(randint(range_start, range_end))


application_fee = [300, 400, 500, 600, 700, 800, 900]


def random_date():
    start_date = datetime.strptime('1 January, 2023', '%d %B, %Y')
    end_date = datetime.strptime('31 December, 2023', '%d %B, %Y')

    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)


def generate_random_time():
    start_time = datetime.strptime('09:00 AM', '%I:%M %p')
    end_time = datetime.strptime('12:00 PM', '%I:%M %p') - timedelta(hours=1, minutes=30)
    time_diff = end_time - start_time
    random_time = start_time + timedelta(minutes=random.randint(0, int(time_diff.total_seconds() / 60)))
    return random_time.strftime('%I:%M %p') + ' - ' + (random_time + timedelta(hours=1, minutes=30)).strftime(
        '%I:%M %p')


university = [
    {
        'university_id': 'f9606f18-52c2-4664-8f1c-be2db74a9e17',
        'university_name': 'Bangabandhu Sheikh Mujibur Rahman Science and Technology University',
        'university_image': f'../assets/university_image/f9606f18-52c2-4664-8f1c-be2db74a9e17.jpg',
        'university_intro': 'BSMRSTU, known as Bangabandhu Sheikh Mujibur Rahman Science and Technology University, is a public university '
                            'in Gopalganj. The institution was founded in 2001 with an emphasis on education and research in science and '
                            'technology. With numerous active research initiatives and partnerships with other universities and research '
                            'institutions, BSMRSTU maintains a strong focus on research.'
    },
    {
        'university_id': 'cddf733e-6e9c-45af-8553-cc266e6aca2d',
        'university_name': 'University of Dhaka',
        'university_image': f'../assets/university_image/cddf733e-6e9c-45af-8553-cc266e6aca2d.jpg',
        'university_intro': 'Dhaka University is a renowned institution of higher education in South Asia, known for its academic excellence,'
                            'research capabilities, and cultural significance. It offers undergraduate and postgraduate programs in various '
                            'fields of study, including arts, sciences, business, engineering, law, and medicine.'
    },
    {
        'university_id': '6fcb1eb8-946a-41f9-8c98-2f0d8a5f2a3e',
        'university_name': 'University of Rajshahi',
        'university_image': f'../assets/university_image/6fcb1eb8-946a-41f9-8c98-2f0d8a5f2a3e.jpg',
        'university_intro': 'The University of Rajshahi is one of the largest public co-educational research university in Bangladesh situated near '
                            'the northern region. It is known for its active research culture, with several research centers and institutes, and '
                            'has made significant contributions to the advancement of knowledge in various fields.'
    },
    {
        'university_id': '3977ab12-cc17-42ec-83f0-b752802761e5',
        'university_name': 'University of Chittagong',
        'university_image': f'../assets/university_image/3977ab12-cc17-42ec-83f0-b752802761e5.jpg',
        'university_intro': 'Chittagong University is one of the most prestigious and oldest institutions of higher learning in Bangladesh.'
                            'The institution is known for its beautiful campus, academic excellence, research facilities, and contribution '
                            'to the development of higher education in Bangladesh.'
    },
    {
        'university_id': '77d1387c-0654-41a5-beef-9ec77fcb31f4',
        'university_name': 'Jahangirnagar University',
        'university_image': f'../assets/university_image/77d1387c-0654-41a5-beef-9ec77fcb31f4.jpg',
        'university_intro': 'Jahangirnagar University is a prestigious public research university located in Savar, Bangladesh. Established in 1970, '
                            'the university is named after the Mughal Emperor Jahangir. Jahangirnagar University is known for its picturesque campus, '
                            'vibrant student community, and strong commitment to social justice and environmental sustainability.'
    },
    {
        'university_id': '5b7a2ba2-4a4d-44f8-81eb-41003c9fbd58',
        'university_name': 'Khulna University',
        'university_image': f'../assets/university_image/5b7a2ba2-4a4d-44f8-81eb-41003c9fbd58.jpg',
        'university_intro': 'Khulna University is a public university located in Khulna, a southwestern city of Bangladesh. The university offers '
                            'undergraduate and postgraduate programs in various fields of study, including science, engineering, social sciences, and'
                            ' humanities. '
    },
    {
        'university_id': '9855d5ef-16a1-4ed0-b322-0426791efc09',
        'university_name': 'National University',
        'university_image': f'../assets/university_image/9855d5ef-16a1-4ed0-b322-0426791efc09.jpg',
        'university_intro': 'The National University of Bangladesh is a public university of Bangladesh that was established by an Act of Parliament '
                            'as an affiliating University of the country to impart graduate and post-graduate level education to the students through '
                            'its affiliated colleges and professional institutions throughout the country. It is the fourth largest university in the '
                            'world according to enrollment. '
    },
    {
        'university_id': '932477b6-3824-4214-9ca6-951a7ace8d7e',
        'university_name': 'Bangladesh Agricultural University',
        'university_image': f'../assets/university_image/932477b6-3824-4214-9ca6-951a7ace8d7e.jpg',
        'university_intro': 'Bangladesh Agricultural University, also known as BAU, is a public agricultural university located in Mymensingh.'
                            ' Crop science, soil science, animal science, fisheries, and agricultural engineering are a few of the study areas linked to '
                            'agriculture that the institution offers undergraduate and graduate programs in.'
    }
]

admission_group = [
    {
        'admission_group_id': uuid4(),
        'university_id': 'f9606f18-52c2-4664-8f1c-be2db74a9e17',
        'group_name': 'Group-A',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Academia Hall'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': 'f9606f18-52c2-4664-8f1c-be2db74a9e17',
        'group_name': 'Group-B',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Scholar\'s Arena'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': 'f9606f18-52c2-4664-8f1c-be2db74a9e17',
        'group_name': 'Group-C',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Wisdom Auditorium'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': 'f9606f18-52c2-4664-8f1c-be2db74a9e17',
        'group_name': 'Group-D',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Learning Plaza'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': 'cddf733e-6e9c-45af-8553-cc266e6aca2d',
        'group_name': 'Group-A',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Intellect Center'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': 'cddf733e-6e9c-45af-8553-cc266e6aca2d',
        'group_name': 'Group-B',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Success Hall'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': 'cddf733e-6e9c-45af-8553-cc266e6aca2d',
        'group_name': 'Group-C',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Knowledge Dome'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': 'cddf733e-6e9c-45af-8553-cc266e6aca2d',
        'group_name': 'Group-D',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Achievement Pavilion'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '6fcb1eb8-946a-41f9-8c98-2f0d8a5f2a3e',
        'group_name': 'Group-A',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Education Hub'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '6fcb1eb8-946a-41f9-8c98-2f0d8a5f2a3e',
        'group_name': 'Group-B',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Excellence Hall'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '6fcb1eb8-946a-41f9-8c98-2f0d8a5f2a3e',
        'group_name': 'Group-C',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Discovery Auditorium'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '6fcb1eb8-946a-41f9-8c98-2f0d8a5f2a3e',
        'group_name': 'Group-D',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Innovation Pavilion'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '3977ab12-cc17-42ec-83f0-b752802761e5',
        'group_name': 'Group-A',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Brilliance Center'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '3977ab12-cc17-42ec-83f0-b752802761e5',
        'group_name': 'Group-B',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Think Tank Hall'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '3977ab12-cc17-42ec-83f0-b752802761e5',
        'group_name': 'Group-C',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Genius Arena'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '3977ab12-cc17-42ec-83f0-b752802761e5',
        'group_name': 'Group-D',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Achievement Pavilion'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '77d1387c-0654-41a5-beef-9ec77fcb31f4',
        'group_name': 'Group-A',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Academia Hall'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '77d1387c-0654-41a5-beef-9ec77fcb31f4',
        'group_name': 'Group-B',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Scholar\'s Arena'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '77d1387c-0654-41a5-beef-9ec77fcb31f4',
        'group_name': 'Group-C',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Wisdom Auditorium'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '77d1387c-0654-41a5-beef-9ec77fcb31f4',
        'group_name': 'Group-D',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Learning Plaza'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '5b7a2ba2-4a4d-44f8-81eb-41003c9fbd58',
        'group_name': 'Group-A',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Intellect Center'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '5b7a2ba2-4a4d-44f8-81eb-41003c9fbd58',
        'group_name': 'Group-B',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Success Hall'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '5b7a2ba2-4a4d-44f8-81eb-41003c9fbd58',
        'group_name': 'Group-C',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Knowledge Dome'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '5b7a2ba2-4a4d-44f8-81eb-41003c9fbd58',
        'group_name': 'Group-D',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Achievement Pavilion'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '9855d5ef-16a1-4ed0-b322-0426791efc09',
        'group_name': 'Group-A',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Education Hub'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '9855d5ef-16a1-4ed0-b322-0426791efc09',
        'group_name': 'Group-B',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Excellence Hall'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '9855d5ef-16a1-4ed0-b322-0426791efc09',
        'group_name': 'Group-C',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Discovery Auditorium'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '9855d5ef-16a1-4ed0-b322-0426791efc09',
        'group_name': 'Group-D',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Innovation Pavilion'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '932477b6-3824-4214-9ca6-951a7ace8d7e',
        'group_name': 'Group-A',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Brilliance Center'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '932477b6-3824-4214-9ca6-951a7ace8d7e',
        'group_name': 'Group-B',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Think Tank Hall'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '932477b6-3824-4214-9ca6-951a7ace8d7e',
        'group_name': 'Group-C',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Genius Arena'
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '932477b6-3824-4214-9ca6-951a7ace8d7e',
        'group_name': 'Group-D',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'exam_time': generate_random_time(),
        'application_fee': random.choice(application_fee),
        'min_req': round(random.uniform(2.50, 5.00), 2),
        'hsc_group': random.choice(['Science', 'Commerce', 'Arts']),
        'exam_venue': 'Knowledge Dome'
    }
]

payment = []

application = []

exam = []


def generate_random_students(num_students):
    students = []

    college_names = [
        'Dhaka College',
        'Dhaka Imperial College',
        'Rajuk Uttara Model College',
        'Notre Dame College',
        'Adamjee Cantonment College',
        'Dhaka Residential Model College',
        'Birshreshtha Munshi Abdur Rouf College',
        'Dhaka City College',
        'Ideal College',
        'Dhaka Commerce College',
        'B A F Shaheen College Dhaka',
        'Milestone College',
        'Cantonment English School and College',
        'National Ideal College',
        'Mymensingh Zilla School',
        'Carmichael College',
        'Kabi Nazrul Government College',
        'Chittagong College',
        'Feni Government College'
    ]
    email_domains = [
        'gmail.com',
        'yahoo.com',
        'hotmail.com',
        'outlook.com',
        'icloud.com',
        'aol.com',
        'protonmail.com',
        'mail.com',
        'zoho.com',
        'yandex.com'
    ]

    for i in range(num_students):
        names = ["Ahmed Rahman", "Zaid Ali", "Omar Hussain", "Aariz Ahmed", "Ibrahim Khan", "Ayaan Rahman", "Zayan Ali",
                 "Rayan Hussain", "Rahim Islam", "Yusuf Ahmed", "Hamza Khan", "Imran Hossain", "Ayan Rahman",
                 "Farhan Ali", "Armaan Hussain", "Shahid Islam", "Faisal Ahmed", "Nabil Khan", "Kamran Hossain",
                 "Riyad Rahman"]
        father_names = ["Mohammed Rahman", "Abdul Ali", "Ismail Hussain", "Nasir Ahmed", "Khalid Khan", "Salim Rahman",
                        "Shahid Ali", "Rizwan Hussain", "Akram Islam", "Younus Ahmed", "Tariq Khan", "Zahir Hossain",
                        "Nasim Rahman", "Feroz Ali", "Arshad Hussain", "Anwar Islam", "Javed Ahmed", "Imtiaz Khan",
                        "Ashraf Hossain", "Abdullah Rahman"]
        mother_names = ["Sadia Rahman", "Nadia Ali", "Aisha Hussain", "Fariha Ahmed", "Samina Khan", "Sara Rahman",
                        "Ayesha Ali", "Rukhsana Hussain", "Nasima Islam", "Yasmin Ahmed", "Shabana Khan",
                        "Farida Hossain", "Razia Rahman", "Nargis Ali", "Nazia Hussain", "Sabina Islam", "Fauzia Ahmed",
                        "Najma Khan", "Asma Hossain", "Rabeya Rahman"]

        applicant_id = str(uuid.uuid4())
        hsc_roll = ''.join(random.choice(string.digits) for _ in range(6))
        hsc_reg = ''.join(random.choice(string.digits) for _ in range(11))
        hsc_board = random.choice(['Dhaka', 'Chittagong', 'Rajshahi', 'Barisal', 'Sylhet'])
        hsc_year = str(random.randint(2020, 2022))
        hsc_result = round(random.uniform(2.50, 5.00), 2)
        hsc_group = random.choice(['Science', 'Commerce', 'Arts'])

        name = names[i]
        email = name.lower().replace(' ', '') + '@' + random.choice(email_domains)
        college = random.choice(college_names)
        phone_number = ''.join(random.choice(string.digits) for _ in range(11))
        father_name = father_names[i]
        mother_name = mother_names[i]

        student = Applicants(applicant_id=applicant_id, hsc_roll=hsc_roll, hsc_reg=hsc_reg, hsc_board=hsc_board,
                             hsc_year=hsc_year, hsc_result=hsc_result, hsc_group=hsc_group, name=name, email=email,
                             college=college, phone_number=phone_number, father_name=father_name,
                             mother_name=mother_name)
        students.append(student)

    return students


def create_data():
    for i in university:
        session.add(University(**i))
        try:
            session.commit()
        except Exception:
            session.rollback()

    for i in admission_group:
        session.add(AdmissionGroup(**i))
        try:
            session.commit()
        except Exception:
            session.rollback()

    session.add_all(generate_random_students(10))
    try:
        session.commit()
    except Exception:
        session.rollback()


if __name__ == '__main__':
    create_data()
