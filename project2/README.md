# Project 2

Web Programming with Python and JavaScript

(win)
- cd C:\Users\spa3cap\Documents\GitHub\flask (0)
- venv\Scripts\activate (1)
- pip3 install -r requirements.txt
- cd C:\Users\spa3cap\Documents\GitHub\project2 (2)
- set FLASK_APP=app.py (3)
- set FLASK_ENV=development (4)
- flask run (5)

(mac)
- cd users/Tar/frameworks/flask (0)
- . venv/bin/activate (1)
- pip3 install -r requirements.txt
- cd github/CS50W/project2 (2)
- export FLASK_APP=app.py (3)
- export FLASK_ENV=development (4)
- flask run (5)


<button class="btn btn-primary" id="enter"> Enter </button>
<br> <br>
<p id="text"> </p>

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
