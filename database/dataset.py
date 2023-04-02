import random
import string
import uuid
from datetime import timedelta, datetime
from uuid import uuid4

from database import session
from database.models import Applicants, University, AdmissionGroup

application_fee = [300, 400, 500, 600, 700, 800, 900]


def random_date():
    start_date = datetime.strptime('1 January, 2023', '%d %B, %Y')
    end_date = datetime.strptime('31 December, 2023', '%d %B, %Y')

    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)


applicants = []

university = [
    {
        'university_id': 'cddf733e-6e9c-45af-8553-cc266e6aca2d',
        'university_name': 'University of Dhaka',
        'university_image': f'front-end/assets/university_image/cddf733e-6e9c-45af-8553-cc266e6aca2d.jpg',
        'university_intro': 'The University of Dhaka is one of the oldest and most prestigious universities in '
                            'Bangladesh. Founded in 1921, it has a rich history of academic excellence and '
                            'intellectual leadership, with a strong commitment to advancing knowledge and promoting '
                            'social justice. With over 35,000 students and more than 1,800 faculty members, '
                            'the University of Dhaka is a vibrant and dynamic community that fosters creativity, '
                            'innovation, and critical thinking. Its diverse range of programs and research '
                            'initiatives make it a hub for intellectual exploration and a driving force for social, '
                            'cultural, and economic development in Bangladesh and beyond.'
    },
    {
        'university_id': '6fcb1eb8-946a-41f9-8c98-2f0d8a5f2a3e',
        'university_name': 'University of Rajshahi',
        'university_image': f'front-end/assets/university_image/6fcb1eb8-946a-41f9-8c98-2f0d8a5f2a3e.jpg',
        'university_intro': 'The University of Rajshahi is one of the largest and most respected public universities '
                            'in Bangladesh. Established in 1953, it has a proud legacy of academic excellence and '
                            'leadership, with a strong commitment to research, teaching, and community service. The '
                            'university offers a wide range of undergraduate and graduate programs across various '
                            'disciplines, including science, engineering, humanities, and social sciences. With a '
                            'sprawling campus spanning over 753 acres, the University of Rajshahi provides a vibrant '
                            'and stimulating environment for students and scholars to pursue their academic and '
                            'intellectual passions. Its alumni include some of the most prominent figures in '
                            'Bangladesh\'s history, and the university continues to play a crucial role in shaping '
                            'the country\'s future.'
    },
    {
        'university_id': '3977ab12-cc17-42ec-83f0-b752802761e5',
        'university_name': 'University of Chittagong',
        'university_image': f'front-end/assets/university_image/3977ab12-cc17-42ec-83f0-b752802761e5.jpg',
        'university_intro': 'The University of Chittagong is a renowned public university located in Chittagong, '
                            'Bangladesh. Established in 1966, it offers a wide range of undergraduate and '
                            'postgraduate programs across various disciplines. With a mission to provide quality '
                            'education and research, the university has played a significant role in shaping the '
                            'intellectual and cultural landscape of the region. Its faculty members and alumni have '
                            'made notable contributions to various fields, including science, humanities, and social '
                            'sciences.'
    },
    {
        'university_id': '77d1387c-0654-41a5-beef-9ec77fcb31f4',
        'university_name': 'Jahangirnagar University',
        'university_image': f'front-end/assets/university_image/77d1387c-0654-41a5-beef-9ec77fcb31f4.jpg',
        'university_intro': 'Jahangirnagar University is a public university located in Savar, Bangladesh. Founded in '
                            '1970, it is known for its commitment to academic excellence and social justice. With a '
                            'sprawling campus spanning over 697 acres, the university offers a wide range of '
                            'undergraduate and postgraduate programs across various disciplines, including science, '
                            'arts, and social sciences. The university has a strong research culture and its faculty '
                            'members and students are actively engaged in cutting-edge research that addresses '
                            'pressing social, economic, and environmental challenges facing Bangladesh and the world.'
    },
    {
        'university_id': '5b7a2ba2-4a4d-44f8-81eb-41003c9fbd58',
        'university_name': 'Khulna University',
        'university_image': f'front-end/assets/university_image/5b7a2ba2-4a4d-44f8-81eb-41003c9fbd58.jpg',
        'university_intro': 'Khulna University is a public university located in Khulna, Bangladesh. Established in '
                            '1991, it is known for its strong focus on research and innovation. The university offers '
                            'undergraduate and postgraduate programs across various disciplines, including science, '
                            'engineering, and social sciences. With a mission to provide quality education and '
                            'contribute to the development of the region, the university has been at the forefront of '
                            'efforts to address social, economic, and environmental challenges through cutting-edge '
                            'research and community engagement. Its faculty members and students are highly respected '
                            'in their respective fields, both nationally and internationally.'
    },
    {
        'university_id': '9855d5ef-16a1-4ed0-b322-0426791efc09',
        'university_name': 'National University',
        'university_image': f'front-end/assets/university_image/9855d5ef-16a1-4ed0-b322-0426791efc09.jpg',
        'university_intro': 'National University is a government-run university located in Gazipur, Bangladesh. '
                            'Established in 1992, it is the second-largest university in the world by enrollment, '
                            'with over 2.5 million students. The university offers a wide range of undergraduate and '
                            'postgraduate programs across various disciplines, including science, arts, and social '
                            'sciences. With a focus on distance education, the university has played a significant '
                            'role in expanding access to higher education in Bangladesh, particularly in rural areas. '
                            'Its programs are designed to meet the needs of diverse learners, including working '
                            'professionals and non-traditional students.'
    },
    {
        'university_id': '932477b6-3824-4214-9ca6-951a7ace8d7e',
        'university_name': 'Bangladesh Agricultural University',
        'university_image': f'front-end/assets/university_image/932477b6-3824-4214-9ca6-951a7ace8d7e.jpg',
        'university_intro': 'Bangladesh Agricultural University (BAU) is a specialized public university located in '
                            'Mymensingh, Bangladesh. Founded in 1961, it is dedicated to research, education, '
                            'and extension in the fields of agriculture, fisheries, and forestry. BAU offers '
                            'undergraduate, postgraduate, and doctoral programs in various agricultural disciplines, '
                            'including agronomy, horticulture, veterinary science, and fisheries. Its faculty members '
                            'and alumni are highly respected in the field of agriculture, and the university has '
                            'played a critical role in advancing agricultural research and innovation in Bangladesh '
                            'and beyond.'
    },
]

admission_group = [
    {
        'admission_group_id': uuid4(),
        'university_id': 'cddf733e-6e9c-45af-8553-cc266e6aca2d',
        'group_name': 'Group-A',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'application_fee': random.choice(application_fee)
    },
    {
        'admission_group_id': uuid4(),
        'university_id': 'cddf733e-6e9c-45af-8553-cc266e6aca2d',
        'group_name': 'Group-B',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'application_fee': random.choice(application_fee)
    },
    {
        'admission_group_id': uuid4(),
        'university_id': 'cddf733e-6e9c-45af-8553-cc266e6aca2d',
        'group_name': 'Group-C',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'application_fee': random.choice(application_fee)
    },
    {
        'admission_group_id': uuid4(),
        'university_id': 'cddf733e-6e9c-45af-8553-cc266e6aca2d',
        'group_name': 'Group-D',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'application_fee': random.choice(application_fee)
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '6fcb1eb8-946a-41f9-8c98-2f0d8a5f2a3e',
        'group_name': 'Group-A',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'application_fee': random.choice(application_fee)
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '6fcb1eb8-946a-41f9-8c98-2f0d8a5f2a3e',
        'group_name': 'Group-B',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'application_fee': random.choice(application_fee)
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '6fcb1eb8-946a-41f9-8c98-2f0d8a5f2a3e',
        'group_name': 'Group-C',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'application_fee': random.choice(application_fee)
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '6fcb1eb8-946a-41f9-8c98-2f0d8a5f2a3e',
        'group_name': 'Group-D',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'application_fee': random.choice(application_fee)
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '3977ab12-cc17-42ec-83f0-b752802761e5',
        'group_name': 'Group-A',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'application_fee': random.choice(application_fee)
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '3977ab12-cc17-42ec-83f0-b752802761e5',
        'group_name': 'Group-B',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'application_fee': random.choice(application_fee)
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '3977ab12-cc17-42ec-83f0-b752802761e5',
        'group_name': 'Group-C',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'application_fee': random.choice(application_fee)
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '3977ab12-cc17-42ec-83f0-b752802761e5',
        'group_name': 'Group-D',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'application_fee': random.choice(application_fee)
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '77d1387c-0654-41a5-beef-9ec77fcb31f4',
        'group_name': 'Group-A',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'application_fee': random.choice(application_fee)
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '77d1387c-0654-41a5-beef-9ec77fcb31f4',
        'group_name': 'Group-B',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'application_fee': random.choice(application_fee)
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '77d1387c-0654-41a5-beef-9ec77fcb31f4',
        'group_name': 'Group-C',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'application_fee': random.choice(application_fee)
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '77d1387c-0654-41a5-beef-9ec77fcb31f4',
        'group_name': 'Group-D',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'application_fee': random.choice(application_fee)
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '5b7a2ba2-4a4d-44f8-81eb-41003c9fbd58',
        'group_name': 'Group-A',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'application_fee': random.choice(application_fee)
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '5b7a2ba2-4a4d-44f8-81eb-41003c9fbd58',
        'group_name': 'Group-B',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'application_fee': random.choice(application_fee)
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '5b7a2ba2-4a4d-44f8-81eb-41003c9fbd58',
        'group_name': 'Group-C',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'application_fee': random.choice(application_fee)
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '5b7a2ba2-4a4d-44f8-81eb-41003c9fbd58',
        'group_name': 'Group-D',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'application_fee': random.choice(application_fee)
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '9855d5ef-16a1-4ed0-b322-0426791efc09',
        'group_name': 'Group-A',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'application_fee': random.choice(application_fee)
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '9855d5ef-16a1-4ed0-b322-0426791efc09',
        'group_name': 'Group-B',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'application_fee': random.choice(application_fee)
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '9855d5ef-16a1-4ed0-b322-0426791efc09',
        'group_name': 'Group-C',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'application_fee': random.choice(application_fee)
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '9855d5ef-16a1-4ed0-b322-0426791efc09',
        'group_name': 'Group-D',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'application_fee': random.choice(application_fee)
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '932477b6-3824-4214-9ca6-951a7ace8d7e',
        'group_name': 'Group-A',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'application_fee': random.choice(application_fee)
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '932477b6-3824-4214-9ca6-951a7ace8d7e',
        'group_name': 'Group-B',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'application_fee': random.choice(application_fee)
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '932477b6-3824-4214-9ca6-951a7ace8d7e',
        'group_name': 'Group-C',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'application_fee': random.choice(application_fee)
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '932477b6-3824-4214-9ca6-951a7ace8d7e',
        'group_name': 'Group-D',
        'exam_datetime': random_date().strftime('%d %B, %Y'),
        'application_fee': random.choice(application_fee)
    },

]

payment = []

application = []

exam = []


def generate_random_students(num_students):
    students = []

    for i in range(num_students):
        applicant_id = str(uuid.uuid4())
        hsc_roll = ''.join(random.choice(string.digits) for _ in range(6))
        hsc_reg = ''.join(random.choice(string.digits) for _ in range(11))
        hsc_board = random.choice(['Dhaka', 'Chittagong', 'Rajshahi', 'Barisal', 'Sylhet'])
        hsc_year = str(random.randint(2000, 2020))
        hsc_result = str(random.uniform(2.5, 5.0))[:4]
        hsc_group = random.choice(['Science', 'Commerce', 'Arts'])

        name = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(10))
        email = name.lower() + "@example.com"
        college = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(15))
        phone_number = ''.join(random.choice(string.digits) for _ in range(11))
        father_name = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(10))
        mother_name = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(10))

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
