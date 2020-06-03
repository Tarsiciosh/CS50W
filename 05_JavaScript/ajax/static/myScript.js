document.addEventListener('DOMContentLoaded', () => {
    
    document.querySelector('#form').onsubmit = () => {
        const isbn = document.querySelector("#isbn").value;
        const request = new XMLHttpRequest(); // create request
        request.open("POST", "/review"); //

        data = new FormData(); //add the data to the request
        data.append("isbn", isbn);
        request.send(data); // sends the request to /review

        request.onload = () => { //when the server responses 
            const data = JSON.parse(request.responseText);
            alert(data)
            if (data.success) {
                const contents = `The count is ${data.count} and the average ${data.average}.`;
                document.querySelector('#result').innerHTML = contents;
            }
            else {
                document.querySelector('#result').innerHTML = 'There was an error.'
            }
        }
        return false; //to make the page no load again
    };
    
});