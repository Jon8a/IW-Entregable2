// Validaciones personalizadas para los formularios de Componente, Producto y Pedido

// Componente precio no negativo y codigo referencia empieza por CMP
const componenteForm = document.getElementById('componenteForm');
if (componenteForm) {
    componenteForm.addEventListener('submit', function (e) {
        let error = "";
        // Si el precio es negativo
        let precio = parseFloat(document.getElementById('id_precio').value);
        if (precio < 0) {
            error += "El precio no puede ser negativo \n";
        }
        //Si el codigo de referencia no empieza por CMP
        let ref = document.getElementById('id_codigo_referencia').value;
        if (!ref.startsWith('CMP')) {
            error += "El código de referencia debe empezar por 'CMP'";
        }
        if (error) {
            //Alerta de error
            alert(error);
            e.preventDefault(); // Para que no se envíe el formulario
        }
    });
}

// Producto referencia empieza por PRD
const productoForm = document.getElementById('productoForm');
if (productoForm) {
    productoForm.addEventListener('submit', function (e) {
        let error = "";
        let ref = document.getElementById('id_referencia').value;
        if (!ref.startsWith('PRD')) {
            error += "La referencia debe empezar por 'PRD'";
        }
        if (error) {
            alert(error);
            e.preventDefault();
        }
    });
}

// Pedido código referencia empieza por PED
const pedidoForm = document.getElementById('pedidoForm');
if (pedidoForm) {
    pedidoForm.addEventListener('submit', function (e) {
        let error = "";
        let ref = document.getElementById('id_codigo_referencia').value;
        if (!ref.startsWith('PED')) {
            error += "El código de referencia debe empezar por 'PED'";
        }
        if (error) {
            alert(error);
            e.preventDefault();
        }
    });
}

// Convertir a mayúsculas los campos de texto con la clase "mayusculas", en este caso se aplica a los campos de código de referencia
document.addEventListener("DOMContentLoaded", function() {
  document.querySelectorAll(".mayusculas").forEach(function(input) {
    input.addEventListener("input", function() {
      this.value = this.value.toUpperCase();
    });
  });
});


