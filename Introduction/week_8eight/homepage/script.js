document.addEventListener("DOMContentLoaded", function() {
    const images = [
        "Images/patrick1.jpeg",
        "Images/patrick2.jpeg",
        "Images/patrick3.jpeg",
        "Images/patrick4.jpeg",
        "Images/patrick5.jpeg",
        "Images/patrick6.jpeg",
        "Images/patrick7.jpeg",
        "Images/patrick8.jpeg",
        "Images/patrick9.jpeg",
        "Images/patrick10.jpeg",
        "Images/patrick11.jpeg",
        "Images/patrick12.jpeg"


    ];
    let index = 0;
    const main_image = document.getElementById("index_image");
    let right = document.getElementById("button_right");
    right.addEventListener("click", function() {
        index = (index + 1 + images.length) % images.length;
        main_image.src = images[index];

    })
    let left = document.getElementById("button_left");
    left.addEventListener("click", function() {
        index = (index - 1 + images.length) % images.length;
        main_image.src = images[index];
    })

})

document.addEventListener("DOMContentLoaded", function(){
    image = document.getElementById("gif").src;
    image.style.display = "none";
    yes = document.getElementById("yesOption");
    yes.addEventListener("click", function(){
       image.src = "Images/perro_bailando.gif";
       image.style.display = "block";
    })
    no = document.getElementById("noOption");
    no.addEventListener("click", function(){
       image.src = "Images/triste.gif";
        image.style.display = "block";
    })

})
