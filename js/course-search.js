const courseList = document.getElementById('course-search-list');
const searchBar = document.getElementById('course-search-bar');

searchBar.addEventListener('keyup', (e) => {
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
});

/*
searchBar.addEventListener('keyup', (ev) => {
    const searchStringName = ev.target.value.toLowerCase();
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
});
*/

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
    window.open("https://halperk.github.io/suanalytics/course-analytics/" + courseCode + "/");
}