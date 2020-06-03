
// when loads the page:
document.addEventListener("DOMContentLoaded", function() {  
    
    const myButton = document.querySelector("button")
    
    myButton.onclick = count;
    
    myButton.onmouseover = over;

    myButton.onmouseleave = function() {
        document.querySelector("button").style.color = "white";
    }
    document.querySelector("#form").onsubmit = function () {
        const name = document.querySelector("#name").value;
        alert(`hello ${name}`);
    };
});

let counter = 0;

function count(){
    counter++;
    document.querySelector('#counter').innerHTML = counter;
    if (counter % 10 === 0) {
        alert(`counter is at ${counter}`);
        //template literal (` is not ') -> java
        //formated string -> python
    }
} 

function over () {
    document.querySelector('button').style.color = "red";
}
