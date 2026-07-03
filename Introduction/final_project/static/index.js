console.log("JavaScript Loaded");

document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#view-profile').addEventListener('click', show_profile);
});

function show_profile() {
    document.getElementById("profile_view").style.display = "block";
    document.getElementById("index_view").style.display = "none";
    document.getElementById("welcome").style.display = "none";
    document.getElementById("select_view").style.display = "none";
}


