document.addEventListener("DOMContentLoaded", (event) => {
    const csrftoken = getCookie("csrftoken");
    console.log(csrftoken);
  
    let selectElement = document.querySelectorAll(".myselect");
    selectElement.forEach((selected) =>{
      selected.addEventListener("change", (event) => {

        let element_value = event.target.value;
        console.log('value: ', element_value);
        let childElement = event.target;
        console.log('child: ',childElement);
        let parentElement = childElement.parentNode;
        parentElement = parentElement.parentNode;
        console.log('parent: ',parentElement)
        let product_id = parentElement.id;
        console.log('select option parent id: ', product_id);
  
        fetch("/cart/confirm_purchase/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,
          },
          mode: "same-origin",
          body: JSON.stringify({ product_id: product_id, select_quantity: element_value }),
        })
          .then((response) => {
            if (!response.ok) {
              throw Error(response.statusText);
            }
            return response.json();
            
          })
          .catch((error) =>{
            console.log('Error Occured: ', error);
          });
    
      });
  
    });
    
  });

  function getCookie(name) {
    let cookievalue = null;
  
    console.log("call getcookie function");
  
    if (document.cookie && document.cookie !== "") {
      console.log("enter in if statement");
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        console.log("enter in cookie for loop");
        const cookie = cookies[i].trim();
  
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookievalue = decodeURIComponent(cookie.substring(name.length + 1));
          console.log("cookievalue:", cookievalue);
          break;
        }
      }
    }
  
    return cookievalue;
  }