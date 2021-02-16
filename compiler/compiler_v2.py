import json
import requests
from bs4 import BeautifulSoup

#Copyright @Huseyin Alper Karedeniz, @Deniz Can Gezgin

#edit term name to accsess
#Put '{}' in json file before running!
term = "201601"
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
#lesson_details = soup.find_all("td", class_="dddefault")
lesson_name_details = soup.find_all("th", class_="ddlabel")
#table_details = soup.find_all("table", class_="datadisplaytable")
length = len(lesson_name_details)



for i in range(length):
    lesson = lesson_name_details[i]
    current_details = lesson.parent.findNext('td')
    current_table = lesson.parent.findNext("table")
    #current_table = table_details[i + 1]
    course_details = (lesson.a.text).split(" - ")
    if course_details[-1] == "X":
        continue
    #course code
    course_code = course_details[-2]
    if course_code[-1] != "R" and course_code[-1] != "L" and course_code[-1] != "D" and course_code[-1] != "P":
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
        course_credit = str(((current_table.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element.previous_element)[1:-1].strip(" ").split(" "))[0])
        if course_credit != "":
            course_credit = float(course_credit)
            data[term][course_code][4] = course_credit
        else:
            data[term][course_code][4] = "ERROR_EMPTYCREDIT"
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

        print(str(i+1) + "/" + str(length))
    else:
        continue
    

with open(json_name, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False)
json_file.close()