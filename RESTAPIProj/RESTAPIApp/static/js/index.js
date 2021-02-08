const SearchForm = document.getElementById('SearchForm');
const SearchQuery = document.getElementById('query');
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value; //accessing the crsf token.

//POST API request
SearchForm.addEventListener('submit', (event) => {
    event.preventDefault();
    console.log("user query", SearchQuery.value);
    let Data = {
        'SearchQuery': SearchQuery.value,
    };
    //This function takes json from the url and append it to the page.
    let url = "http://127.0.0.1:8000/properties/"; //url form the json data is coming.
    let options = {
        //there are the POST method options which will go with the API request.
        method: "POST", //POST method.
        body: JSON.stringify(Data), //User json data.
        headers: {
            //headers will send the info of the content type and csrf token in the backend.
            'content-Type': "application/json",
            'X-CSRFToken': csrftoken
        }
    };
    fetch(url, options)
    .then(Response => Response.json())//here we are converting the data into json format.
    .then(data => {
            //this then function append the json data to the table items.
            console.log(data);
    })
    .catch(error => console.log(error)); //if error's came it will appear into the console.
});