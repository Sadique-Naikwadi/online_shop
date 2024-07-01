document.addEventListener("DOMContentLoaded", (event) => {
  event.preventDefault();
  const csrftoken = getCookie("csrftoken");
  console.log(csrftoken);

  let buttons = document.querySelectorAll(".remove-cart");
  buttons.forEach((button) => {
    button.addEventListener("click", (event) => {
      event.preventDefault();
      let product_id = button.value;
      console.log('product_id: ', product_id);
      
      let url = 'cart/remove_from_cart/';



      fetch("/cart/remove_from_cart/", {
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


