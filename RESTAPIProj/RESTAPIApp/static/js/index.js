const SearchForm = document.getElementById('SearchForm'); //Accessing the form to add eventlistener and send API request.
const SearchQuery = document.getElementById('query'); //Accessing the user query from the input tab.
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value; //accessing the crsf token.

//listening to the form submission event.
SearchForm.addEventListener('submit', (event) => {
    event.preventDefault(); //it will prevent the page reloading.

    let Data = {
        'SearchQuery': SearchQuery.value,  //Text inside the searchqueryinput.
    };

    let url = "http://127.0.0.1:8000/properties/"; //url form the json data is coming.

    let options = {
        //there are the POST method options which will go with the API request.
        method: "POST", //POST method.
        body: JSON.stringify(Data), //Searchquery json data.
        headers: {
            //headers will send the info of the content type and csrf token in the backend.
            'content-Type': "application/json",  //data type will be json.
            'X-CSRFToken': csrftoken  //csrftoken verification.
        }
    };
    fetch(url, options) //fetch request.
    .then(Response => Response.json())//here we are converting the data into json format.
    .then(data => {
            //this function will show the results in the console.
            console.log(data);
    })
    .catch(error => console.log(error)); //if error's came it will appear into the console.
});