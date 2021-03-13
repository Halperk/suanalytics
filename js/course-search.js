const courseList = document.getElementById('course-search-list');
const searchBar = document.getElementById('course-search-bar');

const searchTypeButtonCode = document.getElementById('course-search-type-code');
const searchTypeButtonName = document.getElementById('course-search-type-name');
let searchType = "course-code";

function searchFromCourseCode() {
    searchTypeButtonName.classList.remove('search-type-activated');
    searchTypeButtonCode.classList.add('search-type-activated');
    searchBar.placeholder = "Search a course from course code";
    searchType = "course-code";
}

function searchFromCourseName() {
    searchTypeButtonCode.classList.remove('search-type-activated');
    searchTypeButtonName.classList.add('search-type-activated');
    searchBar.placeholder = "Search a course from course name";
    searchType = "course-name";
}

searchBar.addEventListener('keyup', (e) => {
    if (searchType === "course-code") {
        searchCoursesByCode(e);
    } else if (searchType === "course-name") {
        searchCoursesByName(e);
    } else {
        searchCoursesByCode(e);
    }
});

function searchCoursesByCode(e) {
    const searchString = e.target.value.toUpperCase().replace(/\s/g, "");
    if (searchString != "") {
        const filteredCourses = data.filter((course) => {
            return (
                course.code.replace(/\s/g, "").indexOf(searchString) === 0
            );
        });
        displayCourses(filteredCourses);
    }
    else {
        courseList.innerHTML = ''
    }
}

function searchCoursesByName(e) {
    const searchStringName = e.target.value.toLowerCase();
    if (searchStringName != "") {
        const filteredCoursesName = data.filter((course) => {
            return (
                course.name.toLowerCase().indexOf(searchStringName) !== -1
            );
        });
        displayCourses(filteredCoursesName);
    }

    else {
        courseList.innerHTML = ''
    }
}

const displayCourses = (courses) => {
    let link;
    const htmlString = courses.map((course) => {
        courseCode = course.code.replace(" ", "").toLowerCase();
        courseHtmlCode = "<li onclick=\"goToCoursePage(this.id)\" id=\"" + courseCode + "\" class=\"course-search-course\"><h2>" + course.code + "</h2><p>" + course.name + "</p></li>";
        return courseHtmlCode
    }).join('');
    courseList.innerHTML = htmlString;
};

function goToCoursePage(courseCode) {
    window.open("https://halperk.github.io/suanalytics/course-analytics/" + courseCode + "/", "_self");
}
