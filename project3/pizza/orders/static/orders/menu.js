document.addEventListener("DOMContentLoaded", () => {
    document.querySelector("#tt").onchange = () => {
        toppingsType = document.querySelector("#tt").value;
        console.log(toppingsType);
        if (toppingsType == 2) { //1 topping
            document.querySelector("#t1").style.display = "block";
            document.querySelector("#t2").style.display = "none";
            document.querySelector("#t3").style.display = "none";      
        }
        if (toppingsType == 3) { //2 topping
            document.querySelector("#t1").style.display = "block";
            document.querySelector("#t2").style.display = "block";
            document.querySelector("#t3").style.display = "none";      
        }
        if (toppingsType == 4) { //3 topping
            document.querySelector("#t1").style.display = "block";
            document.querySelector("#t2").style.display = "block";
            document.querySelector("#t3").style.display = "block";      
        }
    }

  
    /*
    document.querySelector("#confirmOrder").onclick = () => {
        
        token = document.querySelector("csrfmiddlewaretoken");
        console.log(token)

        const request = new XMLHttpRequest();
        request.open("POST","/confirm_order"); 
        request.onload = () => {
            const data = JSON.parse(request.responseText);
            if (data.success == false) {
                console.log("problem getting info");
            } else { //SUCCESS
                console.log("order confirm")
            }     
        }
        // if the item to add is a pizza:
        data = new FormData();
        message = "confirmed"
        data.append("message", message);
        request.send (data);
        console.log("confirm order pressed");
    }
    */

    /*
    document.querySelector("#addItem").onclick = () => {
        const request = new XMLHttpRequest();
        request.open("POST","/add_item"); 
        request.onload = () => {
            const data = JSON.parse(request.responseText);
            if (data.success == false) {
                console.log("problem getting info");
            } else { //SUCCESS
                console.log("item added")
            }     
        }
        // if the item to add is a pizza:
        data = new FormData();
        pizzaTypeID = document.querySelector("#pizzaTypeID").value;
        data.append("pizzaTypeID",pizzaTypeID);
        request.send (data);
        console.log("add item");
        // if the item to add is a sub:
        // 
    }
    */

});

/*
pizzaTypeID = request.POST["pizzaType"]
sizeID = request.POST["size"]
toppingsTypeID = request.POST["toppingsType"]    
topping1ID = request.POST["topping1"]*/