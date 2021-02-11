const SearchForm = document.getElementById('SearchForm'); //Accessing the form to add eventlistener and send API request.
const SearchQuery = document.getElementById('query'); //Accessing the user query from the input tab.
const LocationQuery = document.getElementById('LocationQuery'); //Accessing the property location from the input tab.
const PropertyTypeQuery = document.getElementById('PropertyTypeQuery'); //Accessing the property type from the input tab.
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value; //accessing the crsf token.
const PropertyContainer = document.getElementById('PropertyContainer');  //Accessing the property element to insert the filtered properties in it.


//listening to the form submission event.
SearchForm.addEventListener('submit', (event) => {
  event.preventDefault(); //it will prevent the page reloading.

  let Data = {
    'SearchQuery': SearchQuery.value,  //Text inside the searchqueryinput.
    'LocationQuery': LocationQuery.value,  //Text inside the searchqueryinput.
    'PropertyTypeQuery': PropertyTypeQuery.value,  //Text inside the searchqueryinput.
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

      // this function will show the results in the console.
      if (Object.keys(data).length != 0) {
        let html = "";
        data.forEach(element => {
          //This html element will append to the front end.
          html += `
                      <div class="col-md-6 col-sm-6">
                <div class="property_item heading_space">
                  <div class="image">
                    <img src="${element.Proprety_Image}" alt="listin" class="img-responsive">
                    <div class="overlay">
                      <div class="centered"><a class="link_arrow white_border" href="property_details_1.html">View Detail</a></div>
                    </div>
                    <div class="feature"><span class="tag">For:- ${element.Avaliable_For}</span></div>
                    <div class="price"><span class="tag">Price:- ${element.Property_Price}</span></div>
                    <div class="property_meta">
                      <span><i class="fa fa-object-group"></i>${element.Area_in_sqft} </span>
                    </div>
                  </div>
                  <div class="proerty_content">
                    <div class="proerty_text">
                      <h3><a href="property_details_1.html">${element.PropertyName}</a></h3>
                      <span class="bottom10">${element.Property_Description}</strong></p>
                      <span class="bottom10">Location:-${element.Location}</strong></p>
                      <span class="bottom10">Address:-${element.PropertyAddress}</strong></p>
                      <span class="bottom10">BHK:-${element.BHK}</strong></p>
                    </div>
                    <div class="favroute clearfix">
                      <p class="pull-left">Status:- ${element.PropertyStatus}</p>
                      <p class="pull-left">Type:- ${element.Property_Type}</p>
                    </div>
                  </div>
                </div>
              </div>`
        });
        PropertyContainer.innerHTML = html;

      } else {
        //if any error occured an alert message will get appear.
        alert('Please enter right input!')
      }
    })
    .catch(() => {
      alert('Please enter right input!')
    }); //if error's came it will appear into the console.
});