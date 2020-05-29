# Project 2

Web Programming with Python and JavaScript


     <button class="btn btn-primary" id="enter"> Enter </button>
        <br> <br>
        <p id="text"> </p>


        
        direccion:
        
        Av. Pinedo 50, estacion Solá, Galpon 1, puerta 21, Barracas.

        Güemes 573 Tres Arroyos 

Castro 2230 Boedo



action="{{ url_for('add_review', isbn=book.isbn) }}" method="post" 



 <div class="alert alert-danger" id="result"> </div>



document.addEventListener("DOMContentLoaded", () => {
    //document.querySelector("#header").style.color= "grey"
    clearMessage("result");
   
});



function printMessage (name, type, message) {
    if (type === "success"){
        const mens = document.querySelector("#" + name)
        mens.style.display = "block";
        mens.className = "alert alert-success";
        mens.innerHTML = message;
    } else if (type === "error") {
        const mens = document.querySelector("#" + name)
        mens.style.display = "block";
        mens.className = "alert alert-danger";
        mens.innerHTML = message;
    }
} 

function clearMessage (name)
{
    document.querySelector("#" + name).style.display = "none"; //hide the mens
}

//"alert alert-success"




 <div id="login" class="container pt-4">
        <h1 id="header"> Welcome to Flack! </h1>
        <div class="form-inline bt-3">
            <input class="form-control mt-3" id="displayName" name="displayName" autocomplete="off" autofocus
                    placeholder="Choose a display name" type="text" style="width: 70%;">
            <input class="btn btn-primary mt-3 ml-3" id="enter" type="submit" value="Enter">
        </div>
    </div>