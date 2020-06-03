
console.log(document.querySelector("#test").innerHTML)

const test_template = Handlebars.compile(document.querySelector("#test").innerHTML);

document.addEventListener('DOMContentLoaded', () => {
   
    var contents = "Hello with Handlebars!";
    const myHTMLPart = test_template ({'contents': contents})
    document.querySelector('#main').innerHTML += myHTMLPart;
});


    