"use strict";

let year, courses, faculty, name;


$.getJSON("https://raw.githubusercontent.com/Halperk/suanalytics/main/data/data_202001.json", function (resp) {
    console.log(resp);
    console.log(resp[202001]["ACC 201"]);

});



function getCourseName(term, code) {//term format 202003

};



