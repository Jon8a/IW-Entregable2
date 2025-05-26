document.addEventListener("DOMContentLoaded", function () {
    
    const slider = document.getElementById("deslizante");
    const valor = document.getElementById("valorDeslizante");

    //Cuando se modifica el valor del slider, se actualiza el tamaño del texto
    slider.addEventListener("input", function () {
        
        //Se actualiza el valor del texto que muestra el tamaño actual
        const tamaño = slider.value + "px";
        valor.textContent = tamaño; 
        slider.textContent = tamaño;

        // Se aplica el tamaño de texto a todos los elementos de texto
        document.querySelectorAll("h1, h2, h3, h4, h5, h6, p, li, td, th, label, a").forEach(function(elemento) {
            elemento.style.fontSize = tamaño;
        });
    });
});