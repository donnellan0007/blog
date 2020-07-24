feather.replace();

var profile = document.getElementById('profile-nav-stuff');

profile.addEventListener('mouseover', (e) => {
    profile.classList.add('hover-class');
})

$("#osc-nav-he").click(function() {
    $("body").load('index.html')
})