//GET API function.
function GetData() {
    //This function takes json from the url and append it to the page.
    let url = "http://127.0.0.1:8000/api/employee/"; //url form the json data is coming.
    fetch(url).then(Response => Response.json())//here we are converting the data into json format.
        .then(data => {
            //this then function append the json data to the table items.
            // console.log(data);
            let TableData = "";
            data.forEach((element) => {
                TableData += `
                            <tr>
                                <td>${element.E_id}</td>     
                                <td>${element.E_name}</td>     
                                <td>${element.E_mob}</td>     
                            </tr>
                            `;
            });
            let Table = document.getElementById('table');
            Table.innerHTML += TableData;
        })
        .catch(error => console.log(error)); //if error's came it will appear into the console.
};
GetData(); //running the function.