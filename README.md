# IW-Entregable2

Enlace al repositorio de GitHub:
    https://github.com/Jon8a/IW-Entregable2

Resultado de pip freeze en el archivo: requirements.txt
---------------------------------------------------------------------------------------------------------------

Este proyecto ha sido desarrollado en el contexto del Reto 2 de la asignatura, usando Django como framework backend. Permite gestionar pedidos, productos y componentes para una empresa, incluyendo información de clientes y el estado de los pedidos.

Caracteristicas del Reto 2 Gestión de pedidos:

La empresa llamada Deustronic Components S.L. ha decidido que ya ha llegado la hora de
solucionar sus problemas derivados del uso de hojas Excel y comenzar a utilizar una
aplicación para la gestión de pedidos. Tras un análisis de las alternativas disponibles, ha
optado por encargar el desarrollo de una nueva aplicación a medida a vuestro equipo.
La empresa se dedica a la fabricación de productos electrónicos (dispone de varias
categorías y modelos) que comercializa a empresas de todo el mundo. Le gustaría poder
gestionar su catálogo de productos así como los pedidos realizados por los clientes.

● Pedido
    ○ Código de referencia del pedido (debe ser único)
    ○ Fecha de entrega estimada del pedido
    ○ Fecha de entrega del pedido (al crearlo no se indica, se modifica después)
    ○ Datos del cliente (CIF, nombre de empresa, dirección y datos de contacto)
    ○ Productos solicitados (no es necesario indicar la cantidad de cada producto)
    ○ Estado del pedido (en proceso, preparado, entregado)
    ○ Urgencia del pedido (urgente, prioritario, normal)
    ○ Detalles del pedido (campo de texto)
● Producto
    ○ Referencia (debe ser única)
    ○ Precio
    ○ Nombre
    ○ Descripción
    ○ Categoría
    ○ Componentes de un producto
● Componente
    ○ Código de referencia
    ○ Nombre de modelo
    ○ Tipo de componente
    ○ Proveedor
    ○ Especificaciones técnicas (texto)

Siendo esta la información principal que se maneja, las funcionalidades más importantes
requeridas son:

● Gestión de productos: creación, visualización (listado y detalle) y baja.
● Gestión de pedidos: creación, visualización (listado y detalle) y actualización.

La empresa también está abierta a cualquier funcionalidad extra que se quiera incorporar:
● Gestión de clientes
● Gestión de Proveedores de un componente (many-to-many)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Funcionalidades Extra Implementadas:

Se ha implementado la gestion de Clientes-Empresa, dando la posibilidad de ver, crear y eliminar Empresas y con una relacion one-to-many permitiendo que una empresa tenga varios pedidos

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Para instalar y ejecutar el proyecto habra que realizar estos pasos:

Crear el entorno virtual a utilizar:
    python -m venv entorno

Activar el entorno creado:
    .\entorno\Scripts\activate

Instalar los requerimientos para el funcionamiento:
    pip install -r requirements.txt

Ejecutar el servidor local:
    python manage.py runserver

Y finalmente acceder a la aplicacion mediante el navegador en esta url:
    http://127.0.0.1:8000/


----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Entrega E3,E4:

Ampliación de funcionalidades en Python:

    (2 puntos) Envío de emails desde la aplicación:

        Se ha programado de tal forma que cuando se actualice un pedido se enviara un email a el email que contiene el campo de datos de contacto del cliente vinculado a dicho pedido, actualizandole de el nuevo estado del pedido
        Para probarlo crear un cliente con el email a usar y crear o asignarle un pedido, luego editar el estado de dicho pedido lo que deberia mandarle un email

    (2 puntos) Subida de ficheros al servidor mediante <input type="file"> y
    mostrarlos en una página (tienen que poder descargarse)

        Se ha programado de tal forma que podra añadirse un archivo en los componentes (pensado para planos, modelo3D...) en caso de querer añadir mas de un archivo debera añadirse un zip que contenga todo

    (1 punto) Paginación en tablas/listados de los resultados de una tabla.

        Se ha programado de forma que si el listado contiene mas de 10 registros se paginaran dando la opcion de navegar a la pagina siguiente o la ultima en caso de existir paginas siguientes y de ir a la anteriror o la primera en caso de haber anteriores


Implementar las siguientes funcionalidades JavaScript:

    (1p) Crear un evento al hacer click en un botón o enlace que produzca el
    cambio (aumentar/disminuir) del tamaño de todos los elementos de texto
    (<h1>, <h2>, <p>, ...).

        Se ha hecho de forma que habra un slider en el footer que permita manipular en tiempo real el tamaño de todos los elementos de texto, visualizando el valor en pixeles en todo momento
    
    (1p) Validar campos de un formulario antes de su envío al servidor,
    impidiendo el envío si no se supera la validación

        Programado para no permitir el envio del formulario en caso de no cumplir con unos prefijos preestablecidos para los codigos de referencia de todos lo modelos (por cuestion de navegabilidad y orden) ademas de no permitir que un componente tenga precio negativo

    (1p) Autocalcular un campo de un formulario

        Programado para convertir los caracteres contenidos en el formulario de codigo de referencia de todos los modelos a mayusculas (Esta programado al final de el archivo validaciones.js)

    (1p) Capturar un evento en el DOM y producir un cambio en el
    estilo/contenido de la página (p. ej: mostrar/ocultar un bloque al hacer click
    en “expandir información”, mostrar una alerta si el usuario realiza una acción
    determinada,...)

        Saltara una alerta si un usuario edita el estado actual de la entrega de un pedido alertando de que se enviara un email a la empresa designada con los cambios realizados
        Ademas tambien habra una alerta en caso de que no se cumplan las validaciones anteriormente descritas alertando el motivo

Funcionalidades JavaScript para cargar y/o almacenar datos utilizando Fetch:

    (2p) Cargar datos y modificar el DOM mediante JavaScript: llamada a API de
    Django utilizando Fetch para obtener datos y mostrar los valores modificando
    el DOM:

        Funcionalidad programada de forma que, al seleccionar componentes en el formulario de producto, se haga automáticamente una llamada a una API de Django usando Fetch. El JavaScript recoge los IDs de los componentes seleccionados, consulta el precio total al backend y, cuando recibe la respuesta, actualiza el campo de precio en el formulario sin recargar la página. Así, el usuario ve el precio actualizado en tiempo real según los componentes elegidos

            Los archivos que contien esta funcionalidad son:

                producto_form.html
                producto_editar.html
                views.py
                urls.py
                models.py


