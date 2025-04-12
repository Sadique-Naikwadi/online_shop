document.addEventListener("DOMContentLoaded", (event) => {
  
    const csrftoken = getCookie("csrftoken");
    
  
    let buttons = document.querySelectorAll(".add-to-cart");
    buttons.forEach((button) => {
      button.addEventListener("click", (event) => {
        event.preventDefault();
        let product_id = button.value;
  
        let url = gettext("/cart/add_to_cart/");
        
       
        
  
        fetch(`/${language}${url}`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,
          },
          mode: "same-origin",
          body: JSON.stringify({ product_id: product_id }),
        })
          .then((response) => {
            if (!response.ok) {
              throw Error(response.statusText);
            }
            return response.json();
          })
          .then((data) => {
            document.getElementById("cartCounter").innerHTML = data.total;
          })
          .catch((error) => {
            console.log("Error Occured: ", error);
          });
      });
    });

    // remove cart

        let remove_buttons = document.querySelectorAll(".remove-cart");
        remove_buttons.forEach((button) => {
        button.addEventListener("click", (event) => {
        event.preventDefault();
        let product_id = button.value;
        console.log('product_id: ', product_id);
        
        let url = gettext("/cart/remove_from_cart/");
        console.log('URL of Remove: ', url)



        fetch(`/${language}${url}`, {
            method: "POST",
            headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,
            },
            mode: "same-origin",
            body: JSON.stringify({ product_id: product_id }),
        })
            .then((response) => {
            if (!response.ok) {
                throw Error(response.statusText);
            }
            return response.json();
            })
            .then((data) => {
                if(data.status){
                    parent = document.querySelector("tbody");
                    child = document.getElementById(product_id);
                    parent.removeChild(child);
                    document.getElementById("cartCounter").innerHTML = data.cart;
                }
            
            })
            .catch((error) => {
            console.log("Error Occured: ", error);
            });
        });
    });

    // update quantity

    let selectElement = document.querySelectorAll(".myselect");
    selectElement.forEach((found) => {
      found.addEventListener("change", (event) => {
        event.preventDefault();
        let element_value = event.target.value;
        console.log('value: ', element_value);
        let childElement = event.target;
        console.log('child: ',childElement);
        let parentElement = childElement.parentNode;
        parentElement = parentElement.parentNode;
        console.log('parent: ',parentElement)
        let product_id = parentElement.id;
        console.log('select option parent id: ', product_id);

        let url = gettext("/cart/update_purchase/");
        console.log('URL of confirm: ', url);
  
        fetch(`/${language}${url}`, {
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
          .then((data) => {
            if(data.status){
              console.log(data.cart);
              document.getElementById("cartCounter").innerHTML = data.cart;
            }
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
  