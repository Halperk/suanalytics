window.onscroll = function() {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        document.getElementById("backtotop").style.display = "block";
    } else {
        document.getElementById("backtotop").style.display = "none";
    }
}
            
function scrollToPosition(position) {
    window.scrollTo({
        top: position,
        left: 0,
        behavior: "smooth"
    });
}
