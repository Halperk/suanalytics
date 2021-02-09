import json
import requests
from bs4 import BeautifulSoup

#edit term
term = "202001"
filename = term + ".html"
with open(filename,"r", encoding="utf8") as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
html_file.close()

data = {}
json_name = 'data_' + term + '.json'
with open(json_name,"r", encoding='utf-8') as json_file:
    data = json.load(json_file)

# data = {"2019-2020 Fall":{"AL 102":["SL","Academic Literaties","Total","Actual", "3.0 SU",{"Ekrem Sabit Şimşek": [123,124], "Ali Nihat Eken": [163,156]},"CoRequisites","PreRequisities" ]}}
data[term] = {}

lesson_details = soup.find_all("td", class_="dddefault")
lesson_name_details = soup.find_all("th", class_="ddlabel")
table_details = soup.find_all("table", class_="datadisplaytable")
length = len(lesson_name_details)

for i in range(length):
    lesson = lesson_name_details[i]
    current_details = lesson.parent.findNext('td')
    current_table = table_details[i + 1]
    course_details = (lesson.a.text).split(" - ")
    #course code
    course_code = course_details[-2]
    if course_code[-1] != "R" and course_code[-1] != "L":
        if course_code not in data[term]:
            data[term][course_code] = ["","",0,0,0,{},[],[]]

        #course name
        course_name = course_details[0]
        data[term][course_code][1] = course_name
        #course address
        course_address = lesson.a["href"]

        details = current_details
        fieldlabeltext = details.find_all("span", class_="fieldlabeltext")
        #course faculty
        course_faculty = (fieldlabeltext[3].next_sibling)[1:-1].split(" ")[-1]
        data[term][course_code][0] = course_faculty
        #course credit
        course_credit = float(((current_table.previous_sibling.previous_sibling.previous_sibling.previous_sibling.previous_sibling.previous_sibling.previous_sibling.previous_sibling.previous_sibling)[1:-1].strip(" ").split(" "))[0])
        data[term][course_code][4] = course_credit
        #course instructors
        primary_instructor_raw = (current_table.find("abbr", {"title": "Primary"})).previous_sibling[:-1]
        instructor_dict = data[term][course_code][5]
        primary_instructor = ""
        names_of_instructor = primary_instructor_raw.split(" ")
        for x in range(len(names_of_instructor)):
            name = names_of_instructor[x]
            if name == "" or name == " ":
                continue
            else:
                primary_instructor = primary_instructor + name + " "
        primary_instructor = primary_instructor[:-1]
        if primary_instructor not in instructor_dict:
            data[term][course_code][5][primary_instructor] = [0,0]

        r = requests.get(course_address)
        source = BeautifulSoup(r.content,"lxml")
        match = source.find_all("td", class_="dddefault")
        #course capacity
        course_capacity = int(match[1].text)
        data[term][course_code][2] = data[term][course_code][2] + course_capacity
        data[term][course_code][5][primary_instructor][0] = data[term][course_code][5][primary_instructor][0] + course_capacity
        #course actual
        course_actual = int(match[2].text)
        data[term][course_code][3] = data[term][course_code][3] + course_actual
        data[term][course_code][5][primary_instructor][1] = data[term][course_code][5][primary_instructor][1] + course_actual
        
        co_reqs = []
        pre_reqs = []
        a_s = source.find_all('a', href=True)
        for a in range(4,len(a_s)-2):
            a_text = a_s[a].text
            if len(a_text) > 0 and '0' <= a_text[-1] <= '9':
                pre_reqs.append(a_text)
            elif len(a_text) > 0 and (a_text[-1] == 'R' or a_text[-1] == 'L' or a_text[-1] == 'D'):
                co_reqs.append(a_text)

        #course corequisities and prerequisities      
        data[term][course_code][6] = co_reqs
        data[term][course_code][7] = pre_reqs

        print(str(i) + "/" + str(length))
    else:
        continue

with open(json_name, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False)

dm_program_codes = ["BSCS-DM","BACULT-DM","BAECON-DM","BSEE-DM","BSIE-DM","BAIS-DM","BAMAN-DM",
                 "BSMAT-DM","BSME-DM","BSBIO-DM","BAPOLS-DM","BAPSIR-DM","BAPSY-DM","BAVACD-DM"]
dm_program_names = ["Computer Science and Engineering","Cultural Studies","Economics",
                 "Electronics Engineering","Industrial Engineering","International Studies",
                 "Management","Materials Science and Nano Engineering","Mechatronics Engineering",
                 "Molecular Biology, Genetics and Bioengineering","Political Science",
                 "Political Science and International Relations","Psychology",
                 "Visual Arts and Visual Communications Design"]

major_program_codes = ["BSCS","BAECON","BSEE","BSMS","BAMAN","BSMAT","BSME","BSBIO",
                       "BAPSIR","BAPSY","BAVACD"]
major_program_names = ["Computer Science and Engineering","Economics","Electronics Engineering",
                       "Industrial Engineering (Previous Name: Manufacturing Systems Engineering)",
                       "Management","Materials Science and Nano Engineering (Previous Name: Materials Science and Engineering)",
                       "Mechatronics Engineering","Molecular Biology, Genetics and Bioengineering (Pre. Name: Biological Sciences and Bioengineering)",
                       "Political Science and International Relations","Psychology",
                       "Visual Arts and Visual Communications Design"]

minor_program_codes = ["ARTTC-MINOR","ANALY-MINOR","CHEM-MINOR","CONF-MINOR","DECB-MINOR",
                       "ENERG-MINOR","ENTREP-MINOR","FIN-MINOR","GENDER-MINOR","MATH-MINOR",
                       "PHIL-MINOR","PHYS-MINOR","PSY-MINOR"]
minor_program_names = ["Art Theory and Criticism Minor","Business Analytics Minor",
                       "Chemistry Minor","Conflict Analysis & Resolution Minor",
                       "Decision and Behavior Minor","Energy Minor","Entrepreneurship Minor",
                       "Finance Minor","Gender and Women's Studies (Previous Name: Gender Studies) Minor",
                       "Mathematics Minor","Philosophy Minor","Physics Minor","Psychology Minor"]