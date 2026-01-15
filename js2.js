function openNav() {
    document:getElementById("mySidebar").style.width = "250px";
    document:getElementById("main").style.width = "0";
}

function closeNav() {
    document.getElementById("mySideBar").style.width = "0"
    document.getElementById("main").style.marginLeft = "0";
}