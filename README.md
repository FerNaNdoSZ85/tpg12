# tpg12
primera modificaciones en el flujo de la app

Se modifico el flujo de la pagina, es decir como se recorre el sitio:
* Inicialmente, el sitio requeria que el usuario (admin/usuario), esten logueado. Lo que no es obligacion para mostrar el contenido publico acerca del funcionamientdo
  de la pagina (para que es, que ofrece, de que se trata, etc.... solo pedia registrarse/loguearse). 
  Entonces, basada en esta idea, se muestra el Menu de opciones disponibles entre las que figuran las opciones Loguearse, Registrarse, Administrar, etc
  (antes, registrarse era la pagina de "Bienvenida").

* Durante la produccion del sitio se encontraron errores, particularmente entre los datos de la BD y la forma en que se relacionan entre si (usuarios- cuestionarios),
  pendientes de correccion.
  
* Se agregaron unas funcionalidades (templates), las cuales estan aun en desarrollo (estas dependen la interaccion entre tablas de la BD).

* En el flujo, hay caracteristicas que no deberian mostrarse una vez logueado o deslogueado (administrar, cerrar sesion, jugador.. etc).
