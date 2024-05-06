document.addEventListener('DOMContentLoaded', (event) =>{
    event.preventDefault();
 const csrftoken = getCookie('csrftoken');
 console.log(csrftoken); 
 
    let buttons = document.querySelectorAll('.add-to-cart');
    buttons.forEach(button => {
        button.addEventListener('click', (event)=>{
        event.preventDefault();   
        let product = button.value;
        
    
        fetch('/cart/add_to_cart/product.id/', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken},
            mode: 'same-origin',
            body: JSON.stringify({product: product}),
        }).then((response) => {
            if(!response.ok){
                throw Error(response.statusText);
            }
            return response.json();
        }).then((data) => {
            document.getElementById('cartCounter').innerHTML = data.total;
        }).catch((error) => {
            console.log('Error Occured: ', error);
        })

        });
    
    });
});





function getCookie(name){
    let cookievalue = null;

    console.log('call getcookie function');

    if (document.cookie && document.cookie !== '') {
        console.log('enter in if statement');
        const cookies = document.cookie.split(';');
        for(let i = 0; i < cookies.length; i++){
            console.log('enter in cookie for loop');
            const cookie = cookies[i].trim();

            if(cookie.substring(0, name.length +1) === (name  + '=')){
                cookievalue = decodeURIComponent(cookie.substring(name.length + 1));
                console.log('cookievalue:' ,cookievalue);
                break;
            }
        }
        
    }

    return cookievalue;

}