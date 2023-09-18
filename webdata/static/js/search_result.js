var results_scrollable = document.getElementById("results_scrollable");

function isFlightAvail(){
    var avail = document.getElementById("avail");
    var condition = true;
    // pokoknya kalo ada flightsnya, munculin available flights dan data flights yang ada
    // kalo gaada yang available, munculin tulisan No Flights Available dan bikin results scrollable display none
    // tolong sambungin ke databasenya ya makasi
    if(condition){
        avail.textContent = "Available Flights";
        results_scrollable.style.display = "flex";
    }else{
        avail.textContent = "No Flights Available";
        results_scrollable.style.display = "none";
    }
}

var buttons = document.querySelectorAll(".bn-button");

buttons.forEach(function(button){
    button.addEventListener("click", function(){
        window.location.href = "index.html"
        // index.html nya diganti aja sama detail penerbangan
    });
});
