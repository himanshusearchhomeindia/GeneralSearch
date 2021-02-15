let ur1 = location.search.slice(1).split('&'); //accessing the url from the page url tab with filtering the values from (1) it will divide the url into two ('&') it will filter the url from & and make a list of filtered elements.

query = {}  //making an empty query dictionary to append all the queries from the search box.

ur1.forEach((item) => {
  //This loop iterate over all the values of ur1 and split them wiht the ('+').
  item = item.split('='); //spliting the values with ('=').
  for (let index = 0; index <= item.length; index++) {
    //this for loop will iterate over the the item list and append the key and values in the query.
    query[item[index]] = item[index + 1] //item[index] for key and item[index + 1] for the values.
  }
});
let result = JSON.parse(JSON.stringify(query))  //converting the query into string and then in JSON form.

const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value; //accessing the crsf token.
//listening to the form submission event.
window.addEventListener('load', (e) => {
  //This event listener will listen to the page load event and as soon as the page get load it will send a fetch request and append the data in the page.
  e.preventDefault(); //it will prevent the page reloading.
  let Data = {
    'SearchQuery': result.query,  //Text inside the searchqueryinput.
    'LocationQuery': result.LocationQuery,  //Text inside the searchqueryinput.
    'PropertyTypeQuery': result.PropertyTypeQuery,  //Text inside the searchqueryinput.
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
      const PropertyContainer = document.getElementById('PropertyContainer');  //Accessing the property element to insert the filtered properties in it.
      // this function will show the results in the console.
      if (Object.keys(data).length != 0) {
        let html = "";
        data.forEach(element => {
          html += `<div class="col-md-6 col-sm-6">
          <div class="property_item heading_space">
            <div class="image">
              <img src="${element.Property_Image}" alt="listin" class="img-responsive">
              <div class="overlay">
                <div class="centered"><a class="link_arrow white_border" href="">View Detail</a></div>
              </div>
              <div class="feature"><span class="tag">Featured</span></div>
              <div class="price"><span class="tag">${element.Avaliable_For}</span></div>
              <div class="property_meta">
                <span><i class="fa fa-object-group"></i>${element.Area_in_sqft}</span>
                <span><i class="fa fa-bed"></i>2</span>
                <span><i class="fa fa-bath"></i>1 Bathroom</span>
              </div>
            </div>
            <div class="proerty_content">
              <div class="proerty_text">
                <h3><a href="property_details_1.html">${element.Property_Description}</a></h3>
                <span class="bottom10">${element.PropertyAddress}, ${element.Location}</span>
                <p><strong>${element.Property_Price}</strong></p>
              </div>
              <div class="favroute clearfix">
                <p class="pull-left"><i class="icon-calendar2"></i> 3 Days ago</p>
                <ul class="pull-right">
                  <li><a href="#."><i class="icon-video"></i></a></li>
                  <li><a href="#."><i class="icon-like"></i></a></li>
                </ul>
              </div>
            </div>
          </div>
        </div>`;
        });
        PropertyContainer.innerHTML = html;
        alert(data);

      } else {
        //if any error occured an alert message will get appear.
        alert('Something went wrong please try again!');
      }
    })
    .catch(() => {
      alert('Something went wrong please try again!');
    }); //if error's came it will appear into the console.
});