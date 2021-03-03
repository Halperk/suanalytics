let lastTerm;

const slider = tns({
    container: '.slider',
    loop: false,
    items: 1,
    slideBy: 'page',
    nav: false,    
    autoplay: false,
    speed: 1200,
    autoplayButtonOutput: false,
    mouseDrag: true,
    lazyload: true,
    controlsContainer: "#customize-controls",
    responsive: {
        620: {
            items: 2,
        },

        856: {
            items: 3,
        },

        1172: {
            items: 4,
        },
    }});

slider.goTo('last');

const termTermDetection = {"01": "Fall", "02": "Spring", "03": "Summer"}
            
function scrollToPosition(position) {
    window.scrollTo({
        top: position,
        left: 0,
        behavior: "smooth"
    });
}

function initializePage() {
    terms = Object.keys(data);
    lastTerm = terms[terms.length-2];
    changeTerm(lastTerm);

    for (x = 0; x < terms.length - 1; x++) {
        document.getElementById(terms[x]).classList.toggle("inactive-term");
    }
}

setTimeout(initializePage, 150);

function checkTerms() {
    if (document.getElementById(lastTerm).classList.contains("inactive-term")) {
        initializePage()
    }
}

setTimeout(checkTerms, 1500);

function changeTermBottom(termNew) {
    changeTerm(termNew);
}

function changeTerm(term) {

    termTerm = termTermDetection[term.slice(4,6)]+" "+term.slice(0,4)+"-"+(parseInt(parseInt(term.slice(0,4)))+1);

    let courseCode = data[term]["c"];
    let courseName = data[term]["n"];
    let courseFaculty = data[term]["f"];
    let coursePopularity = "#"+data[term]["p"];
    let courseCredit = data[term]["cr"].toFixed(1);
    let courseActual = data[term]["ac"];
    let courseCapacity = data[term]["ca"];
    let courseFillRate = ((courseActual/courseCapacity)*100).toFixed(1)+"%";
    let instructors = data[term]["i"];
    let coursePreReqs = data[term]["pr"];
    let courseCoReqs = data[term]["co"];
    let catalogEntryIdx = data[term]["ce"];

    document.title = "SUAnalytics - " + courseCode + " Analytics | " + courseName + " | " + termTerm;
    document.querySelector("#course-code-d").innerText = courseCode;
    document.querySelector("#course-term-d").innerText = termTerm;
    document.querySelector("#course-name-d").innerText = courseName;
    document.querySelector("#course-faculty-d").innerText = courseFaculty;
    document.querySelector("#course-popularity-d").innerText = coursePopularity;
    document.querySelector("#course-credit-d").innerText = courseCredit;
    document.querySelector("#course-fillrate-d").innerText = courseFillRate;
    document.querySelector("#course-actual-d").innerText = courseActual;
    document.querySelector("#course-capacity-d").innerText = courseCapacity;

    scrollToPosition(0);

    const colorPalette = ["#6050DC","#D52DB7","#FF2E7E","#FF6B45","#FFAB05"]
    let i = 0;
    let instructorsHtml = "";
    let instructorChartDistributionsBarsHtml = "";
    let instructorChartDistributionsTextsHtml = "";
    let percentage = 0.0;
    let instructorCount = instructors.length;
    for (i = 0; i < instructorCount; i++) {

        let instructorName = instructors[i]["tn"];
        let instructorActual = instructors[i]["ta"];
        let instructorCapacity = instructors[i]["tc"];
        let instructorFillRate = ((instructorActual/instructorCapacity)*100).toFixed(1);

        let instructorHtml = "<div class='instructor'><div class='instructor-name'>"+instructorName+"</div><div class='bar'><div class='bar-inner' style='width: "+instructorFillRate+"%;'><a class='bar-inner-rate'>"+instructorFillRate+"%</a></div></div><div class='instructor-quota'>"+instructorActual+"/"+instructorCapacity+"</div></div>";

        let instructorPercentage = ((instructorActual/courseActual)*100).toFixed(2);
        let color = colorPalette[i%colorPalette.length];
        let instructorChartDistributionsBarHtml = "<div class='instructor-chart-bar-instructor' style='width: "+instructorPercentage+"%; left: "+percentage+"%; background: "+color+";'></div>";
        let instructorChartDistributionsTextHtml = "<div class='instructor-chart-list-instructor'><div class='instructor-color' style='background: "+color+";'></div><a>"+instructorName+" ("+instructorPercentage+"%)</a></div>";

        percentage = percentage + parseFloat(instructorPercentage);
        instructorsHtml = instructorsHtml + instructorHtml;
        instructorChartDistributionsBarsHtml = instructorChartDistributionsBarsHtml + instructorChartDistributionsBarHtml;
        instructorChartDistributionsTextsHtml = instructorChartDistributionsTextsHtml + instructorChartDistributionsTextHtml;
    }
    document.getElementById('instructor-bars').innerHTML = instructorsHtml;
    document.getElementById('instructor-chart-distributions-bar').innerHTML = instructorChartDistributionsBarsHtml;
    document.getElementById('instructor-chart-distributions-text').innerHTML = instructorChartDistributionsTextsHtml;

    let p = 0;
    let preReqsHtml = "";
    let coursePreReqCount = coursePreReqs.length;
    if (coursePreReqCount == 0) {
        document.getElementById('prerequisite-list').innerHTML = "<div class='requisite'><a>No prerequisites</a></div>";
    } else {

        for (p = 0; p < coursePreReqCount; p++) {
            let preReq = coursePreReqs[p];
            let preReqName = preReq.replace(/\s+/g, '').toLowerCase();
            let preReqHtml = "<div class='linked-requisite requisite'><a href='../"+preReqName+"'>"+preReq+"</a></div>";
            preReqsHtml = preReqsHtml + preReqHtml;
        }
        document.getElementById('prerequisite-list').innerHTML = preReqsHtml;

    }

    let c = 0;
    let coReqsHtml = "";
    let courseCoReqCount = courseCoReqs.length;
    if (courseCoReqCount == 0) {
        document.getElementById('corequisite-list').innerHTML = "<div class='requisite'><a>No corequisites</a></div>";
    } else {

        for (c = 0; c < courseCoReqCount; c++) {
            let coReq = courseCoReqs[c];
            let coReqHtml = "<div class='requisite'><a>"+coReq+"</a></div>";
            coReqsHtml = coReqsHtml + coReqHtml;
        }
        document.getElementById('corequisite-list').innerHTML = coReqsHtml;

    }

    let catalogEntry = data["catList"][catalogEntryIdx];
    document.getElementById('course-catalog-entry-text').innerHTML = catalogEntry;

}

function moveChangeTerms(){
    scrollToPosition(document.getElementById('other-courses-scroll-bottom').getBoundingClientRect().top - (6 * parseFloat(getComputedStyle(document.documentElement).fontSize)))
}
