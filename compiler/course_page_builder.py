# SUAnalytics (2021) - Course Page Builder by Huseyin Alper Karadeniz

# result = str(input("Enter HTML source code: ")).replace("    ","").replace("\"",'\\"')
# print(result)

import json

# Course JSON File
course_json_file = "data_IF100.json"
with open(course_json_file) as f:
  data = json.load(f)

# Course Last Term Code
key_list = []
for x in data.keys():
  key_list.append(x)
last_term = key_list[-2]

faculties_short = ["FENS","FASS","SOM"]
faculties_long = ["Faculty of Engineering and Natural Sciences", "Faculty of Arts and Social Sciences", "Sabancı Business School"]

term_short = ["01", "02", "03"]
term_long = ["Fall", "Spring", "Summer"]

beginning_code = "<!DOCTYPE HTML> <html>"

# Course Code
course_code_with_blank = str(data[last_term]["c"])
course_code_without_blank = str(data[last_term]["c"]).replace(" ", "")

# Course Name
course_name = str(data[last_term]["n"])

# Course Full Faculty Name
course_faculty_full_name = faculties_long[faculties_short.index(str(data[last_term]["f"]))]

# Course Last Term
term_year = last_term[0:4]
term_term = term_long[term_short.index(last_term[4:6])]
course_last_term = term_term + " " + term_year + "-" + str(int(term_year) + 1)

# Course Faculty
course_faculty = str(data[last_term]["f"])

# Course Popularity
course_popularity = str(data[last_term]["p"])

# Course Credits
course_credits = str(data[last_term]["cr"])

# Course Actual Students
course_actual_student = str(data[last_term]["ac"])

# Course Total Capacity
course_total_capacity = str(data[last_term]["ca"])

# Course Fill Rate
fill_rate = float((int(course_actual_student)/int(course_total_capacity))*100)
course_fill_rate = str(int(round(fill_rate, 0)))

head_code = "<head> <meta charset=\"utf-8\"> <meta content=\"width=device-width, initial-scale=1\" name=\"viewport\" /> <meta name=\"copyright\" content=\"(c) 2021\"> <meta name=\"title\" content=\"SUAnalytics\"> <meta name=\"description\" content=\"Learn more about " + course_code_with_blank + " Sabancı University course analytics created by SUAnalytics. Sabanci University " + course_code_without_blank + " is offered by " + course_faculty_full_name + ".\"> <meta name=\"author\" content=\"Co-Authored by Huseyin Alper Karadeniz, Deniz Can Gezgin\"> <meta name=\"keywords\" content=\"SUAnalytics, Sabanci University, Sabancı University, Sabanci University Analytics, Sabancı University Analytics, " + course_code_with_blank + ", " + course_code_without_blank + ", Sabanci University " + course_code_with_blank + ", Sabanci University " + course_code_without_blank + ", Sabancı University " + course_code_with_blank + ", Sabancı University " + course_code_without_blank + ", Sabanci " + course_code_with_blank + ", Sabancı " + course_code_with_blank + ", Sabancı Üniversitesi, " + course_code_with_blank + " Sabancı, " + course_code_without_blank + " Sabancı, " + course_code_with_blank + " Sabanci, " + course_code_without_blank + " Sabanci\"> <title>SUAnalytics - " + course_code_with_blank + " Analytics | " + course_name + " | " + course_last_term + "</title> <link rel=\"stylesheet\" href=\"../../css/main.css\"> <link rel=\"stylesheet\" href=\"../../css/courses.css\"> <link rel=\"icon\" type=\"image/png\" href=\"../../src/favicon.png\"/> <link rel=\"stylesheet\" href=\"../../css/tiny-slider.css\"> <link rel=\"preconnect\" href=\"https://fonts.gstatic.com\"> <link href=\"https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap\" rel=\"stylesheet\"> <script async src=\"https://www.googletagmanager.com/gtag/js?id=G-80JDD4DQES\"></script> <script>window.dataLayer = window.dataLayer || [];function gtag(){dataLayer.push(arguments);}gtag('js', new Date());gtag('config', 'G-80JDD4DQES');</script> <script>   let data;  fetch('../../data/data_" + course_code_without_blank + ".json') .then(results => results.json()) .then(json_content => { data = json_content; });  </script> <script type=\"text/javascript\" src=\"https://www.gstatic.com/charts/loader.js\"></script> </head>"

navigation_code = "<body> <nav> <div class=\"nav-wrapper\"> <a href=\"../../\" class=\"project-name no-select\">SUAnalytics</a> <div id=\"nav-mobile\"> <input type=\"checkbox\" /> <span></span> <span></span> <span></span> <ul id=\"menu\"> <a href=\"../../\"><li>SUAnalytics</li></a><br> <a href=\"../../course-analytics/\"><li>Course Analytics</li></a><br> <a href=\"../../top-courses/\"><li>Top Courses</li></a><br> <a href=\"../../gpa-calculator/\"><li>GPA Calculator</li></a><br> <a href=\"../../about/\"><li>About</li></a><br> <a href=\"mailto: huseyinalper@sabanciuniv.edu\"><li>Contact</li></a> </ul> </div> <ul id=\"nav-desktop\"> <li><a class=\"no-select\" href=\"../../course-analytics/\">Course Analytics</a></li> <li><a class=\"no-select\" href=\"../../top-courses/\">Top Courses</a></li> <li><a class=\"no-select\" href=\"../../gpa-calculator/\">GPA Calculator</a></li> <li><a class=\"no-select\" style=\"color: #C6333D;\" href=\"../../about/\">About</a></li> </ul> </div> </nav> <div class=\"main\" id=\"course-scroll-top\">"

course_essential_code = "<div class=\"course-essentials\"> <div class=\"course-code\"> <a id=\"course-code-d\">" + course_code_with_blank + "</a> </div> <div class=\"course-name\"> <a id=\"course-name-d\">" + course_name + "</a> </div> <div class=\"course-term\"> <a id=\"course-term-d\">" + course_last_term + "</a> </div> <div class=\"course-term-change\"> <a onclick=\"moveChangeTerms()\">Change Term</a> </div> </div>"

statistics_main_code = "<div class=\"statistics-main\"> <div class=\"main-statistics-title\"> <a>Main Statistics</a> </div> <div class=\"main-statistics\"> <div class=\"main-statistics-top\"> <div class=\"main-statistic\"> <div class=\"main-statistic-top\"> <a id=\"course-faculty-d\">" + course_faculty + "</a> </div> <div class=\"main-statistic-bottom\"> <a>Faculty</a> </div> </div> <div class=\"main-statistic\"> <div class=\"main-statistic-top\"> <a id=\"course-popularity-d\">#" + course_popularity + "</a> </div> <div class=\"main-statistic-bottom\"> <a>Popularity</a> </div> </div> <div class=\"main-statistic\"> <div class=\"main-statistic-top\"> <a id=\"course-credit-d\">" + course_credits + "</a> </div> <div class=\"main-statistic-bottom\"> <a>Credits</a> </div> </div> </div> <div class=\"main-statistics-bottom\"> <div class=\"main-statistic\"> <div class=\"main-statistic-top\"> <a id=\"course-fillrate-d\">" + course_fill_rate + "%</a> </div> <div class=\"main-statistic-bottom\"> <a>Fill Rate</a> </div> </div> <div class=\"main-statistic\"> <div class=\"main-statistic-top\"> <a id=\"course-actual-d\">" + course_actual_student + "</a> </div> <div class=\"main-statistic-bottom\"> <a>Actual Student</a> </div> </div> <div class=\"main-statistic\"> <div class=\"main-statistic-top\"> <a id=\"course-capacity-d\">" + course_total_capacity + "</a> </div> <div class=\"main-statistic-bottom\"> <a>Total Capacity</a> </div> </div> </div> </div> </div>"

# Course Instructors
instructor1 = ""
instructor2 = ""
instructor3 = ""
distribution_percentage = 0;
colorPalette = ["#6050DC","#D52DB7","#FF2E7E","#FF6B45","#FFAB05"]
course_instructors = data[last_term]["i"]
for i in range(len(course_instructors)):
  instructor = course_instructors[i]
  instructor_name = instructor["tn"]
  instructor_actual_students = instructor["ta"]
  instructor_total_capacity = instructor["tc"]

  color = colorPalette[i % len(colorPalette)]

  instructor_fill_rate = str(round(((instructor_actual_students/instructor_total_capacity)*100),1))
  i1 = "<div class=\"instructor\"> <div class=\"instructor-name\">" + instructor_name + "</div> <div class=\"bar\"><div class=\"bar-inner\" style=\"width: " + instructor_fill_rate + "%;\"><a class=\"bar-inner-rate\">" + instructor_fill_rate + "%</a></div></div> <div class=\"instructor-quota\">" + str(instructor_actual_students) + "/" + str(instructor_total_capacity) + "</div> </div>"
  instructor1 = instructor1 + i1

  instructor_distribution_percentage = round(((instructor_actual_students/int(course_actual_student))*100),2)
  i2 = "<div class=\"instructor-chart-bar-instructor\" style=\"width: " + str(instructor_distribution_percentage) + "%; left: " + str(distribution_percentage) + "%; background: " + color + ";\"></div>"
  instructor2 = instructor2 + i2

  i3 = "<div class=\"instructor-chart-list-instructor\"> <div class=\"instructor-color\" style=\"background: " + color + ";\"></div> <a>" + instructor_name + " (" + str(instructor_distribution_percentage) + "%)</a> </div>"
  instructor3 = instructor3 + i3

  distribution_percentage = distribution_percentage + instructor_distribution_percentage

statistics_instructors_first_code = "<div class=\"statistics-instructors\"> <div class=\"instructor-statistics-title\"> <a>Instructor Statistics</a> </div> <div class=\"instructor-statistics\"> <div class=\"instructors\"> <div id=\"instructor-bars\" class=\"instructors-bar-chart\">"
statistics_instructors_second_code = "</div> </div> <div class=\"instructor-chart\"> <div class=\"instructor-chart-distributions\"> <div class=\"instructor-chart-bar\"> <div class=\"instructor-chart-bar-instructors\" id=\"instructor-chart-distributions-bar\">"
statistics_instructors_third_code = "</div> </div> <div class=\"instructor-chart-list\" id=\"instructor-chart-distributions-text\">"
statistics_instructors_fourth_code = "</div> </div> </div> </div> </div>"

statistics_instructors_code = statistics_instructors_first_code + instructor1 + statistics_instructors_second_code + instructor2 + statistics_instructors_third_code + instructor3 + statistics_instructors_fourth_code

requisites_code_first = "<div id=\"requisites-all\" class=\"requisites\"> <div class=\"prerequisites\"> <div class=\"requisite-title\"><a>Prerequisites</a></div> <div id=\"prerequisite-list\" class=\"requisite-list\">"

# Course Prerequisites
course_prerequisites = data[last_term]["pr"]
if len(course_prerequisites) == 0:
  prerequisites_code = "<div class='requisite'><a>No prerequisites</a></div>"
else:
  prerequisites_code = ""
  for prerequisite in course_prerequisites:
    prerequisite_link = prerequisite.replace(" ", "")
    prerequisite_div = "<div class='linked-requisite requisite'><a href='../" + prerequisite_link + "'>" + prerequisite + "</a></div>"
    prerequisites_code = prerequisites_code + prerequisite_div

requisites_code_second = "</div> </div> <div class=\"corequisites\"> <div class=\"requisite-title\"><a>Corequisites</a></div> <div id=\"corequisite-list\" class=\"requisite-list\">"

# Course Corequisites
course_corequisites = data[last_term]["co"]
if len(course_corequisites) == 0:
  corequisites_code = "<div class='requisite'><a>No corequisites</a></div>"
else:
  corequisites_code = ""
  for corequisite in course_corequisites:
    corequisite_div = "<div class='requisite'><a>" + corequisite + "</a></div>"
    corequisites_code = corequisites_code + corequisite_div

requisites_code_third = "</div> </div> </div>"

requisites_code = requisites_code_first + prerequisites_code + requisites_code_second + corequisites_code + requisites_code_third

statistics_other_code = "<div class=\"statistics-others\" id=\"other-courses-scroll-bottom\"> <div class=\"other-terms-title\"> <a>Other Terms</a> </div>  <div class=\"term-slider\">  <div class=\"other-terms\"> <div class=\"container\"> <ul class=\"controls\" id=\"customize-controls\" aria-label=\"Carousel Navigation\" tabindex=\"0\"> <li class=\"prev no-select\" data-controls=\"prev\" aria-controls=\"customize\" tabindex=\"-1\"> <a><i class=\"top-arrow-icon slider-arrow slider-arrow-prev\"></i></a> </li> <li class=\"next no-select\" data-controls=\"next\" aria-controls=\"customize\" tabindex=\"-1\"> <a><i class=\"top-arrow-icon slider-arrow slider-arrow-next\"></i></a> </li> </ul> <div class=\"slider\"> <div class=\"year\"> <div class=\"year-title\"><a>1999-2000</a></div> <div class=\"year-terms\"> <div class=\"term inactive-term\" id=\"199901\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Fall 1999-2000</a></div> </div> <div class=\"term inactive-term\" id=\"199902\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Spring 1999-2000</a></div> </div> <div class=\"term inactive-term\" id=\"199903\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Summer 1999-2000</a></div> </div> </div> </div>  <div class=\"year\"> <div class=\"year-title\"><a>2000-2001</a></div> <div class=\"year-terms\"> <div class=\"term inactive-term\" id=\"200001\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Fall 2000-2001</a></div> </div> <div class=\"term inactive-term\" id=\"200002\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Spring 2000-2001</a></div> </div> <div class=\"term inactive-term\" id=\"200003\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Summer 2000-2001</a></div> </div> </div> </div>  <div class=\"year\"> <div class=\"year-title\"><a>2001-2002</a></div> <div class=\"year-terms\"> <div class=\"term inactive-term\" id=\"200101\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Fall 2001-2002</a></div> </div> <div class=\"term inactive-term\" id=\"200102\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Spring 2001-2002</a></div> </div> <div class=\"term inactive-term\" id=\"200103\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Summer 2001-2002</a></div> </div> </div> </div>  <div class=\"year\"> <div class=\"year-title\"><a>2002-2003</a></div> <div class=\"year-terms\"> <div class=\"term inactive-term\" id=\"200201\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Fall 2002-2003</a></div> </div> <div class=\"term inactive-term\" id=\"200202\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Spring 2002-2003</a></div> </div> <div class=\"term inactive-term\" id=\"200203\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Summer 2002-2003</a></div> </div> </div> </div>  <div class=\"year\"> <div class=\"year-title\"><a>2003-2004</a></div> <div class=\"year-terms\"> <div class=\"term inactive-term\" id=\"200301\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Fall 2003-2004</a></div> </div> <div class=\"term inactive-term\" id=\"200302\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Spring 2003-2004</a></div> </div> <div class=\"term inactive-term\" id=\"200303\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Summer 2003-2004</a></div> </div> </div> </div>  <div class=\"year\"> <div class=\"year-title\"><a>2004-2005</a></div> <div class=\"year-terms\"> <div class=\"term inactive-term\" id=\"200401\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Fall 2004-2005</a></div> </div> <div class=\"term inactive-term\" id=\"200402\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Spring 2004-2005</a></div> </div> <div class=\"term inactive-term\" id=\"200403\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Summer 2004-2005</a></div> </div> </div> </div>  <div class=\"year\"> <div class=\"year-title\"><a>2005-2006</a></div> <div class=\"year-terms\"> <div class=\"term inactive-term\" id=\"200501\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Fall 2005-2006</a></div> </div> <div class=\"term inactive-term\" id=\"200502\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Spring 2005-2006</a></div> </div> <div class=\"term inactive-term\" id=\"200503\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Summer 2005-2006</a></div> </div> </div> </div>  <div class=\"year\"> <div class=\"year-title\"><a>2006-2007</a></div> <div class=\"year-terms\"> <div class=\"term inactive-term\" id=\"200601\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Fall 2006-2007</a></div> </div> <div class=\"term inactive-term\" id=\"200602\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Spring 2006-2007</a></div> </div> <div class=\"term inactive-term\" id=\"200603\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Summer 2006-2007</a></div> </div> </div> </div>  <div class=\"year\"> <div class=\"year-title\"><a>2007-2008</a></div> <div class=\"year-terms\"> <div class=\"term inactive-term\" id=\"200701\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Fall 2007-2008</a></div> </div> <div class=\"term inactive-term\" id=\"200702\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Spring 2007-2008</a></div> </div> <div class=\"term inactive-term\" id=\"200703\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Summer 2007-2008</a></div> </div> </div> </div>  <div class=\"year\"> <div class=\"year-title\"><a>2008-2009</a></div> <div class=\"year-terms\"> <div class=\"term inactive-term\" id=\"200801\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Fall 2008-2009</a></div> </div> <div class=\"term inactive-term\" id=\"200802\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Spring 2008-2009</a></div> </div> <div class=\"term inactive-term\" id=\"200803\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Summer 2008-2009</a></div> </div> </div> </div>  <div class=\"year\"> <div class=\"year-title\"><a>2009-2010</a></div> <div class=\"year-terms\"> <div class=\"term inactive-term\" id=\"200901\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Fall 2009-2010</a></div> </div> <div class=\"term inactive-term\" id=\"200902\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Spring 2009-2010</a></div> </div> <div class=\"term inactive-term\" id=\"200903\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Summer 2009-2010</a></div> </div> </div> </div>  <div class=\"year\"> <div class=\"year-title\"><a>2010-2011</a></div> <div class=\"year-terms\"> <div class=\"term inactive-term\" id=\"201001\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Fall 2010-2011</a></div> </div> <div class=\"term inactive-term\" id=\"201002\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Spring 2010-2011</a></div> </div> <div class=\"term inactive-term\" id=\"201003\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Summer 2010-2011</a></div> </div> </div> </div>  <div class=\"year\"> <div class=\"year-title\"><a>2011-2012</a></div> <div class=\"year-terms\"> <div class=\"term inactive-term\" id=\"201101\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Fall 2011-2012</a></div> </div> <div class=\"term inactive-term\" id=\"201102\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Spring 2011-2012</a></div> </div> <div class=\"term inactive-term\" id=\"201103\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Summer 2011-2012</a></div> </div> </div> </div>  <div class=\"year\"> <div class=\"year-title\"><a>2012-2013</a></div> <div class=\"year-terms\"> <div class=\"term inactive-term\" id=\"201201\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Fall 2012-2013</a></div> </div> <div class=\"term inactive-term\" id=\"201202\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Spring 2012-2013</a></div> </div> <div class=\"term inactive-term\" id=\"201203\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Summer 2012-2013</a></div> </div> </div> </div>  <div class=\"year\"> <div class=\"year-title\"><a>2013-2014</a></div> <div class=\"year-terms\"> <div class=\"term inactive-term\" id=\"201301\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Fall 2013-2014</a></div> </div> <div class=\"term inactive-term\" id=\"201302\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Spring 2013-2014</a></div> </div> <div class=\"term inactive-term\" id=\"201303\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Summer 2013-2014</a></div> </div> </div> </div>  <div class=\"year\"> <div class=\"year-title\"><a>2014-2015</a></div> <div class=\"year-terms\"> <div class=\"term inactive-term\" id=\"201401\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Fall 2014-2015</a></div> </div> <div class=\"term inactive-term\" id=\"201402\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Spring 2014-2015</a></div> </div> <div class=\"term inactive-term\" id=\"201403\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Summer 2014-2015</a></div> </div> </div> </div>  <div class=\"year\"> <div class=\"year-title\"><a>2015-2016</a></div> <div class=\"year-terms\"> <div class=\"term inactive-term\" id=\"201501\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Fall 2015-2016</a></div> </div> <div class=\"term inactive-term\" id=\"201502\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Spring 2015-2016</a></div> </div> <div class=\"term inactive-term\" id=\"201503\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Summer 2015-2016</a></div> </div> </div> </div>  <div class=\"year\"> <div class=\"year-title\"><a>2016-2017</a></div> <div class=\"year-terms\"> <div class=\"term inactive-term\" id=\"201601\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Fall 2016-2017</a></div> </div> <div class=\"term inactive-term\" id=\"201602\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Spring 2016-2017</a></div> </div> <div class=\"term inactive-term\" id=\"201603\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Summer 2016-2017</a></div> </div> </div> </div>  <div class=\"year\"> <div class=\"year-title\"><a>2017-2018</a></div> <div class=\"year-terms\"> <div class=\"term inactive-term\" id=\"201701\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Fall 2017-2018</a></div> </div> <div class=\"term inactive-term\" id=\"201702\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Spring 2017-2018</a></div> </div> <div class=\"term inactive-term\" id=\"201703\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Summer 2017-2018</a></div> </div> </div> </div>  <div class=\"year\"> <div class=\"year-title\"><a>2018-2019</a></div> <div class=\"year-terms\"> <div class=\"term inactive-term\" id=\"201801\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Fall 2018-2019</a></div> </div> <div class=\"term inactive-term\" id=\"201802\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Spring 2018-2019</a></div> </div> <div class=\"term inactive-term\" id=\"201803\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Summer 2018-2019</a></div> </div> </div> </div>  <div class=\"year\"> <div class=\"year-title\"><a>2019-2020</a></div> <div class=\"year-terms\"> <div class=\"term inactive-term\" id=\"201901\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Fall 2019-2020</a></div> </div> <div class=\"term inactive-term\" id=\"201902\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Spring 2019-2020</a></div> </div> <div class=\"term inactive-term\" id=\"201903\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Summer 2019-2020</a></div> </div> </div> </div>  <div class=\"year\"> <div class=\"year-title\"><a>2020-2021</a></div> <div class=\"year-terms\"> <div class=\"term inactive-term\" id=\"202001\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Fall 2020-2021</a></div> </div> <div class=\"term inactive-term\" id=\"202002\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Spring 2020-2021</a></div> </div> <div class=\"term inactive-term\" id=\"202003\" onclick=\"changeTerm(this.id)\"> <div class=\"term-title\"><a>Summer 2020-2021</a></div> </div> </div> </div> </div> </div> </div> </div> </div>"

# Course Catalog Entry
course_catalog_entry = str(data["catList"][data[last_term]["ce"]])
course_catalog_entry_code = "<div class=\"course-catalog-entry\"> <div class=\"course-catalog-entry-title\"> <a>Course Catalog Entry</a> </div> <div class=\"course-catalog-entry-description\"> <a id=\"course-catalog-entry-text\">" + course_catalog_entry + "</a> </div> </div> </div>"

footer_code = "<footer class=\"footer\"> <div class=\"footer-top\"> <div class=\"footer-top-section footer-description\"> <a>SUAnalytics</a> <p>SUAnalytics is a project that aims to collect and analyze the data of various topics in Sabanci University, display them with fruitful visualizations and publish analyses about them.</p> </div> </div> <div class=\"footer-bottom\"> <div class=\"footer-bottom-first\"> <a class=\"footer-link\" style=\"border-right: 1px solid #FFFFFF;\" href=\"../../privacy-policy/\">Privacy Policy</a> <a class=\"footer-link\" href=\"../../terms-and-conditions/\">Terms & Conditions</a> </div> <div class=\"footer-bottom-second\"> <a>© 2021 - SUAnalytics</a> <a>All rights reserved.</a> </div> </div> </footer>  <div> <a id=\"backtotop\" style=\"display: none;\" onclick=\"scrollToPosition(0)\"> <i class='top-arrow-icon'></i> </a> </div> <script src=\"../../js/tiny-slider.js\"></script> <script src=\"../../js/courses.js\"></script> </body> </html>"

final_result_code = beginning_code + head_code + navigation_code + course_essential_code + statistics_main_code + statistics_instructors_code + requisites_code + statistics_other_code + course_catalog_entry_code + footer_code

with open('index.html', 'w') as file:
    file.write(final_result_code)