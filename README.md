# IW-Entregable2

Enlace al repositorio de GitHub:
    https://github.com/Jon8a/IW-Entregable2


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
