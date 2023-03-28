from database import session
from database.models import Applicants, University, AdmissionGroup, Payment, Application, Exam
from uuid import uuid4

applicants = []

university = [
    {
        'university_id': 'cddf733e-6e9c-45af-8553-cc266e6aca2d',
        'university_name': 'University of Dhaka',
        'university_image': None,
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
        'university_image': None,
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
        'university_image': None,
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
        'university_image': None,
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
        'university_image': None,
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
        'university_image': None,
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
        'university_image': None,
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
        'group_name': 'University of Dhaka, Group-A',
        'exam_datetime': None,
        'application_fee': None
    },
    {
        'admission_group_id': uuid4(),
        'university_id': 'cddf733e-6e9c-45af-8553-cc266e6aca2d',
        'group_name': 'University of Dhaka, Group-B',
        'exam_datetime': None,
        'application_fee': None
    },
    {
        'admission_group_id': uuid4(),
        'university_id': 'cddf733e-6e9c-45af-8553-cc266e6aca2d',
        'group_name': 'University of Dhaka, Group-C',
        'exam_datetime': None,
        'application_fee': None
    },
    {
        'admission_group_id': uuid4(),
        'university_id': 'cddf733e-6e9c-45af-8553-cc266e6aca2d',
        'group_name': 'University of Dhaka, Group-D',
        'exam_datetime': None,
        'application_fee': None
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '6fcb1eb8-946a-41f9-8c98-2f0d8a5f2a3e',
        'group_name': 'University of Rajshahi, Group-A',
        'exam_datetime': None,
        'application_fee': None
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '6fcb1eb8-946a-41f9-8c98-2f0d8a5f2a3e',
        'group_name': 'University of Rajshahi, Group-B',
        'exam_datetime': None,
        'application_fee': None
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '6fcb1eb8-946a-41f9-8c98-2f0d8a5f2a3e',
        'group_name': 'University of Rajshahi, Group-C',
        'exam_datetime': None,
        'application_fee': None
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '6fcb1eb8-946a-41f9-8c98-2f0d8a5f2a3e',
        'group_name': 'University of Rajshahi, Group-D',
        'exam_datetime': None,
        'application_fee': None
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '3977ab12-cc17-42ec-83f0-b752802761e5',
        'group_name': 'University of Chittagong, Group-A',
        'exam_datetime': None,
        'application_fee': None
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '3977ab12-cc17-42ec-83f0-b752802761e5',
        'group_name': 'University of Chittagong, Group-B',
        'exam_datetime': None,
        'application_fee': None
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '3977ab12-cc17-42ec-83f0-b752802761e5',
        'group_name': 'University of Chittagong, Group-C',
        'exam_datetime': None,
        'application_fee': None
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '3977ab12-cc17-42ec-83f0-b752802761e5',
        'group_name': 'University of Chittagong, Group-D',
        'exam_datetime': None,
        'application_fee': None
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '77d1387c-0654-41a5-beef-9ec77fcb31f4',
        'group_name': 'Jahangirnagar University, Group-A',
        'exam_datetime': None,
        'application_fee': None
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '77d1387c-0654-41a5-beef-9ec77fcb31f4',
        'group_name': 'Jahangirnagar University, Group-B',
        'exam_datetime': None,
        'application_fee': None
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '77d1387c-0654-41a5-beef-9ec77fcb31f4',
        'group_name': 'Jahangirnagar University, Group-C',
        'exam_datetime': None,
        'application_fee': None
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '77d1387c-0654-41a5-beef-9ec77fcb31f4',
        'group_name': 'Jahangirnagar University, Group-D',
        'exam_datetime': None,
        'application_fee': None
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '5b7a2ba2-4a4d-44f8-81eb-41003c9fbd58',
        'group_name': 'Khulna University, Group-A',
        'exam_datetime': None,
        'application_fee': None
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '5b7a2ba2-4a4d-44f8-81eb-41003c9fbd58',
        'group_name': 'Khulna University, Group-B',
        'exam_datetime': None,
        'application_fee': None
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '5b7a2ba2-4a4d-44f8-81eb-41003c9fbd58',
        'group_name': 'Khulna University, Group-C',
        'exam_datetime': None,
        'application_fee': None
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '5b7a2ba2-4a4d-44f8-81eb-41003c9fbd58',
        'group_name': 'Khulna University, Group-D',
        'exam_datetime': None,
        'application_fee': None
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '9855d5ef-16a1-4ed0-b322-0426791efc09',
        'group_name': 'National University, Group-A',
        'exam_datetime': None,
        'application_fee': None
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '9855d5ef-16a1-4ed0-b322-0426791efc09',
        'group_name': 'National University, Group-B',
        'exam_datetime': None,
        'application_fee': None
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '9855d5ef-16a1-4ed0-b322-0426791efc09',
        'group_name': 'National University, Group-C',
        'exam_datetime': None,
        'application_fee': None
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '9855d5ef-16a1-4ed0-b322-0426791efc09',
        'group_name': 'National University, Group-D',
        'exam_datetime': None,
        'application_fee': None
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '932477b6-3824-4214-9ca6-951a7ace8d7e',
        'group_name': 'Bangladesh Agricultural University, Group-A',
        'exam_datetime': None,
        'application_fee': None
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '932477b6-3824-4214-9ca6-951a7ace8d7e',
        'group_name': 'Bangladesh Agricultural University, Group-B',
        'exam_datetime': None,
        'application_fee': None
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '932477b6-3824-4214-9ca6-951a7ace8d7e',
        'group_name': 'Bangladesh Agricultural University, Group-C',
        'exam_datetime': None,
        'application_fee': None
    },
    {
        'admission_group_id': uuid4(),
        'university_id': '932477b6-3824-4214-9ca6-951a7ace8d7e',
        'group_name': 'Bangladesh Agricultural University, Group-D',
        'exam_datetime': None,
        'application_fee': None
    },

]

payment = []

application = []

exam = []


def create_data():
    tables = {
        'applicants': [applicants, Applicants],
        'university': [university, University],
        'admission_group': [admission_group, AdmissionGroup],
        'payment': [payment, Payment],
        'application': [application, Application],
        'exam': [exam, Exam]
    }

    for i in university:
        session.add(University(**i))
        try:
            session.commit()
        except Exception:
            session.rollback()


if __name__ == '__main__':
    create_data()
