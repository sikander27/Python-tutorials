from collections import defaultdict
import requests
from bs4 import BeautifulSoup
import time
import json

IDS = [(237, 'Bachelor in Science - (Computer Applications) (Autonomous)'),
 (108, 'Bachelor Management Studies'),
 (239, 'Bachelor of Arts'),
 (245, 'Bachelor of Arts - Diploma in Foundation of Yoga'),
 (246, 'Bachelor of Arts - Diploma in Yoga'),
 (248, 'Bachelor of Arts - Fashion Design (Autonomous)'),
 (249,
  'Bachelor of Arts - Film, Television and New Media Production (Autonomous)'),
 (247, 'Bachelor of Arts - Geography (Autonomous)'),
 (250, 'Bachelor of Arts - Multimedia and Mass Communication (Autonomous)'),
 (252, 'Bachelor of Arts - Social Work(Autonomous)'),
 (243, 'Bachelor of Arts - Visual Arts (Autonomous)'),
 (251, 'Bachelor of Arts (Autonomous)'),
 (241, 'Bachelor of Arts (Culinary Arts)'),
 (240, 'Bachelor of Arts (Film, Television and New Media Production)'),
 (254,
  'Bachelor of Arts (Honours) - Apparel Design and Construction (Autonomous)'),
 (244, 'Bachelor of Arts (Multimedia and Mass Communication)'),
 (113, 'Bachelor of Arts( FRENCH STUDIES )'),
 (112, 'Bachelor of Arts(Bachelor of  Arts (GERMAN))'),
 (114, 'Bachelor of Arts(Bachelor of Arts  (FRENCH))'),
 (226, 'Bachelor of Arts(DEMO)'),
 (268,
  'Bachelor of Business Administration (Autonomous) (Business Analytics and Management)'),
 (267, 'Bachelor of Business Administration (Autonomous) (Capital Market)'),
 (269, 'Bachelor of Business Administration (Autonomous) (Digital Marketing)'),
 (272, 'Bachelor of Business Administration (Autonomous) (Event Management)'),
 (270,
  'Bachelor of Business Administration (Autonomous) (Logistics &amp;Supply Chain Management)'),
 (276, 'Bachelor of Business Administration (Autonomous) (Logistics)'),
 (271, 'Bachelor of Business Administration (Autonomous) (Sports Management)'),
 (255, 'Bachelor of Business Administration (Honours)(Autonomous)'),
 (259,
  'Bachelor of Business Administration (Honours)(Autonomous) (Business Administration)'),
 (265,
  'Bachelor of Business Administration (Honours)(Autonomous) (Digital Business)'),
 (260,
  'Bachelor of Business Administration (Honours)(Autonomous) (Entrepreneurship)'),
 (262,
  'Bachelor of Business Administration (Honours)(Autonomous) (Industry Integrated)'),
 (264,
  'Bachelor of Business Administration (Honours)(Autonomous) (Logistics)'),
 (258,
  'Bachelor of Business Administration (Honours)(Autonomous) (Marketing Management)'),
 (261,
  'Bachelor of Business Administration (Honours)(Autonomous) (Professional Accountancy And Financial Management)'),
 (263,
  'Bachelor of Business Administration (Honours)(Autonomous) (Shipping and Logistics Management)'),
 (257,
  'Bachelor of Business Administration (Honours)(Autonomous) (Sports Management)'),
 (256,
  'Bachelor of Business Administration (Honours)(Autonomous) (Tourism and Travel Management)'),
 (234, 'Bachelor of Commerce'),
 (266, 'Bachelor of Commerce - (Business Administration) (Autonomous)'),
 (277, 'Bachelor of Commerce (Accounting and Finance)'),
 (290, 'Bachelor of Commerce (Autonomous)'),
 (305,
  'Bachelor of Commerce (Autonomous) ( Digital Marketing and Artificial Intelligence)'),
 (304, 'Bachelor of Commerce (Autonomous) (Actuarial Studies)'),
 (395, 'Bachelor of Commerce (Autonomous) (Business Process Management)'),
 (306, 'Bachelor of Commerce (Autonomous) (Certified Management Accounting)'),
 (297, 'Bachelor of Commerce (Autonomous) (Digital Business)'),
 (292, 'Bachelor of Commerce (Autonomous) (E-Commerce)'),
 (299, 'Bachelor of Commerce (Autonomous) (Economics and Analytics)'),
 (298, 'Bachelor of Commerce (Autonomous) (Economics)'),
 (294, 'Bachelor of Commerce (Autonomous) (Entrepreneurship)'),
 (295, 'Bachelor of Commerce (Autonomous) (Finance)'),
 (301, 'Bachelor of Commerce (Autonomous) (Financial Management)'),
 (296, 'Bachelor of Commerce (Autonomous) (Financial Markets)'),
 (293, 'Bachelor of Commerce (Autonomous) (International Accounting)'),
 (303, 'Bachelor of Commerce (Autonomous) (International Accounting)'),
 (302, 'Bachelor of Commerce (Autonomous) (Investment Management)'),
 (274, 'Bachelor of Commerce (Autonomous) (Management and Finance)'),
 (291, 'Bachelor of Commerce (Autonomous) (Retail Management)'),
 (300, 'Bachelor of Commerce (Autonomous) (Service Industry Management)'),
 (288, 'Bachelor of Commerce (Banking &amp;Isurance) (Autonomous)'),
 (279, 'Bachelor of Commerce (Banking and Insurance)'),
 (281, 'Bachelor of Commerce (Financial Management)'),
 (289, 'Bachelor of Commerce (Financial Management) (Autonomous)'),
 (278, 'Bachelor of Commerce (Financial Market)'),
 (275, 'Bachelor of Commerce (Financial Market) (Autonomous)'),
 (285, 'Bachelor of Commerce (Honours)(Autonomous)'),
 (287,
  'Bachelor of Commerce (Honours)(Autonomous) (Finance and Management Accounting)'),
 (286,
  'Bachelor of Commerce (Honours)(Autonomous) (International Accounting)'),
 (282, 'Bachelor of Commerce (Investment Management)'),
 (280, 'Bachelor of Commerce (Management Studies)'),
 (307, 'Bachelor of Commerce (Management Studies)(Autonomous)'),
 (283, 'Bachelor of Commerce (Transport Management)'),
 (284, 'Bachelor of Commerce(Accounting and Finance)(Autonomous)'),
 (273, 'Bachelor of Computer Application (Autonomous)'),
 (318, 'Bachelor of Fine Arts - Advanced Diploma in Dance (Kathak)'),
 (312, 'Bachelor of Fine Arts - Applied Art'),
 (314, 'Bachelor of Fine Arts - Ceramics'),
 (317, 'Bachelor of Fine Arts - Diploma in Dance (Kathak)'),
 (316, 'Bachelor of Fine Arts - Foundation Course'),
 (309, 'Bachelor of Fine Arts - Interior Decoration'),
 (310, 'Bachelor of Fine Arts - Metal Work'),
 (313, 'Bachelor of Fine Arts - Painting'),
 (308, 'Bachelor of Fine Arts - Sculpture'),
 (311, 'Bachelor of Fine Arts - Textile Design'),
 (321, 'Bachelor of Management Studies (Autonomous) (Retail Management)'),
 (323, 'Bachelor of Management Studies (Capital Market) (Autonomous)'),
 (322, 'Bachelor of Management Studies (E.M.E.) (Autonomous)'),
 (320, 'Bachelor of Management Studies (Sports Management) (Autonomous)'),
 (315, 'Bachelor of Performing Arts - Dance'),
 (109, 'Bachelor of Performing Arts(Music-Hindustani Vocal)'),
 (110, 'Bachelor of Performing Arts(Music-Sitar)'),
 (111, 'Bachelor of Performing Arts(Music-Tabla)'),
 (115, 'Bachelor of Physical Education(Bachelor of Physical Education )'),
 (324, 'Bachelor of Science'),
 (331, 'Bachelor of Science (Aeronautics) (Avionics)'),
 (330, 'Bachelor of Science (Aeronautics) (Mechanical)'),
 (340, 'Bachelor of Science (Autonomous)'),
 (337,
  'Bachelor of Science (Autonomous) (Actuarial Science &amp;Quantitative Finance)'),
 (358, 'Bachelor of Science (Autonomous) (Actuarial Science)'),
 (344, 'Bachelor of Science (Autonomous) (Animation and VFX)'),
 (343,
  'Bachelor of Science (Autonomous) (Applied Statistics and Data Analytics)'),
 (361,
  'Bachelor of Science (Autonomous) (Artificial Intelligence and Machine Learning)'),
 (397, 'Bachelor of Science (Autonomous) (Artificial Intelligence)'),
 (362,
  'Bachelor of Science (Autonomous) (Cloud Technology and Information Security)'),
 (348, 'Bachelor of Science (Autonomous) (Data Science and Analytics)'),
 (350,
  'Bachelor of Science (Autonomous) (Data Science and Artificial Intelligence)'),
 (347, 'Bachelor of Science (Autonomous) (Data Science and Data Analytics)'),
 (396, 'Bachelor of Science (Autonomous) (Economics)'),
 (360, 'Bachelor of Science (Autonomous) (Environmental Science)'),
 (352, 'Bachelor of Science (Autonomous) (Fashion Design)'),
 (364, 'Bachelor of Science (Autonomous) (Fashion Studies)'),
 (336, 'Bachelor of Science (Autonomous) (Hospitality and Catering)'),
 (238,
  'Bachelor of Science (Autonomous) (Hospitality and Catering) (Sattalite centre )'),
 (346, 'Bachelor of Science (Autonomous) (Human Science)'),
 (345, 'Bachelor of Science (Autonomous) (Interior Design)'),
 (351, 'Bachelor of Science (Autonomous) (Medical Imaging Technology)'),
 (341, 'Bachelor of Science (Autonomous) (Medical Laboratory Technology)'),
 (359, 'Bachelor of Science (Autonomous) (Packaging Technology)'),
 (353, 'Bachelor of Science (Autonomous) (Pharma Drug Science)'),
 (342, 'Bachelor of Science (Autonomous) (Psychology)'),
 (349, 'Bachelor of Science (Autonomous) (Sports Science)'),
 (326, 'Bachelor of Science (Aviation)'),
 (354, 'Bachelor of Science (Aviation) (Autonomous)'),
 (335, 'Bachelor of Science (Biotechnology)'),
 (356, 'Bachelor of Science (Biotechnology) (Autonomous)'),
 (333, 'Bachelor of Science (Computer Science)'),
 (365, 'Bachelor of Science (Computer Science) (Autonomous)'),
 (339,
  'Bachelor of Science (Data Science and Business Analytics) (Autonomous)'),
 (338, 'Bachelor of Science (Data Science)'),
 (366, 'Bachelor of Science (Data Science) (Autonomous)'),
 (332, 'Bachelor of Science (Forensic Science)'),
 (329, 'Bachelor of Science (Home Science)'),
 (357,
  'Bachelor of Science (Honours) (Autonomous) (Integrative Nutrition &amp;Dietetics)'),
 (363, 'Bachelor of Science (Honours) (Autonomous) (Interior Design)'),
 (334, 'Bachelor of Science (Hospitality Studies)'),
 (325, 'Bachelor of Science (Information Technology)'),
 (355, 'Bachelor of Science (Information Technology) (Autonomous)'),
 (328, 'Bachelor of Science (Maritime Hopitality Studies)'),
 (327, 'Bachelor of Science (Nautical Science)'),
 (253, 'Bachelor of Vocation - Theatre and Stage Craft (Autonomous)'),
 (242, 'Bachelor of Vocational - Media Production'),
 (369,
  'Bachelor of Vocational ( Management and Entrepreneurship Development)'),
 (378, 'Bachelor of Vocational (Autonomous) ( Banking and Financial Service)'),
 (376,
  'Bachelor of Vocational (Autonomous) ( Business Management and Enterepreneurial Development)'),
 (384, 'Bachelor of Vocational (Autonomous) ( Cyber Security and Forensics)'),
 (377, 'Bachelor of Vocational (Autonomous) ( Tourism and Hospitality)'),
 (386,
  'Bachelor of Vocational (Autonomous) (Artificial Intelligence and Data Science)'),
 (375,
  'Bachelor of Vocational (Autonomous) (Financial Market and Trading Operations)'),
 (370, 'Bachelor of Vocational (Autonomous) (Financial Markets and Sevices)'),
 (383, 'Bachelor of Vocational (Autonomous) (Food Technology)'),
 (381, 'Bachelor of Vocational (Autonomous) (Medical Laboratory Technology)'),
 (371, 'Bachelor of Vocational (Autonomous) (Real Estate Management)'),
 (374, 'Bachelor of Vocational (Autonomous) (Sales and Marketing Management)'),
 (382, 'Bachelor of Vocational (Autonomous) (Software Development)'),
 (385, 'Bachelor of Vocational (Autonomous) (Sustainable Agriculture)'),
 (372, 'Bachelor of Vocational (Autonomous) (Tourism and Travel Management)'),
 (373, 'Bachelor of Vocational (Autonomous) (Travel and Tourism Management)'),
 (380, 'Bachelor of Vocational (Health Care)'),
 (379, 'Bachelor of Vocational (Medical Laboratory Technology )'),
 (368, 'Bachelor of Vocational(Hospitality and Tourism)'),
 (367, 'Bachelor of Vocational(Tourism and Hospitality Management)')]

# Function to make a POST request and return the tbody content
def fetch_preference_list(token_id):
    url = "https://muugadmission.samarth.edu.in/index.php/course/programme/fetch-preference-list"
    params = {'_token': token_id}
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    try:
        response = requests.post(url, data=params, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
    soup = BeautifulSoup(response.text, 'html.parser')
    tbody = soup.find('tbody')
    return tbody


# List to store td elements
td_elements = []

college_map = defaultdict(list)

# Iterate through the IDS and fetch the preference list
for id, name in IDS:
    print(f"Calling for {id}")
    tbody = fetch_preference_list(id)
    if tbody:
        rows = tbody.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if len(cols) > 0:
                label = cols[0].find('label')
                if label:
                    key = label.get_text(strip=True)
                    college_map[key].append(name)
    # import pdb; pdb.set_trace()

# Print the college map
for key, value in college_map.items():
    print(f"{key}: {value}")

# Save the college map to a file
with open('college_map2.json', 'w') as file:
    json.dump(college_map, file, indent=4)

print("College map saved to 'college_map.json'")

print("Merged HTML saved to 'merged_preference_list.html'")
         