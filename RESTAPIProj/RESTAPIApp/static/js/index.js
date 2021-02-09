const SearchForm = document.getElementById('SearchForm'); //Accessing the form to add eventlistener and send API request.
const SearchQuery = document.getElementById('query'); //Accessing the user query from the input tab.
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value; //accessing the crsf token.
const PropertyContainer = document.getElementById('PropertyContainer');  //Accessing the property element to insert the filtered properties in it.


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
            console.log(data);
            // this function will show the results in the console.
            let html = "";
            data.forEach(element => {
                //This html element will append to the front end.
                html += `
                <div class="d-flex flex-row p-2 bd-highlight card my-4" style="width: 70rem;">
                    <img src="${element.Proprety_Image}" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">${element.PropertyName}</h5><span class="badge bg-secondary">Avaliable for:${element.Avaliable_For}</span>
                        <p class="card-text">PropertyInfo:-${element.Property_Description}</p>
                        <p class="card-text">PropertyAddress:-${element.PropertyAddress}</p>
                        <p class="card-text">Builder:-${element.BuilderName}</p>
                        <p class="card-text">Type:-${element.Property_Type}</p>
                        <p class="card-text">Price:-${element.Property_Price}</p>
                        <p class="card-text">Status:-${element.PropertyStatus}</p>
                    </div>
                </div>`
            });
            PropertyContainer.innerHTML += html;

        })
        .catch(error => console.log(error)); //if error's came it will appear into the console.
});