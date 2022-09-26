# Decisiones que se tomaron en el Proyecto EkchÝ

## Ambiente Django

Base de Datos => Se elije porque tiene incorporado la solución de autenticación.
Se toma la decision de no relacionar la tabla vencimiento impuesto con la tabla de impuesto porque eso requeriria reconocer el impuesto y en este momento no es posible. Si más adelante si se puede trasformar los datos del usuario o aplicación para poder identificarlos de forma automatica.

Libreria => Django Rest, Se utiliza para identificar donde se obtienen los datos y desde donde se procesan, separo lo que proceso en los gráficos y por otro lado la obtención o jquery de consulta donde obtengo los datos.

Unitest => Django tiene la funcionalidad Unitest y provee mas facil los scripts que se definen.


Visualización => Antes se iba a utilizar PowerBI porque contaba con la herramienta, pero después ya no tenia disponibilidad y no iba ser posible de probarlo de manera local, la idea era ejecutarlo en el entorno del trabajo.

Se tomo la decisión de utilizar una libreria para mostrar los gráficos, elegí
 <<Chart.js>> porque es Open sours y puedo conectarlo con la base de datos de Django.
## Configuración
El ambiente de Django se debe configurar según criterios ya preestablecidos, estas configuraciones ejecutan acciones que van intercalandose y llamando según lo que le vaya indicando.
Se crea tres archvos iniciales
* pdfupload.html => se activa en el formulario una accion el cual se definió en <pdf-upload>
* urls.py => se definen las rutas donde se ejecuta la función <pdf-upload>
* views.py => son las vistas o donde se ejecuta la funcion lógica de cada vista, básicamente maneja las peticiones y respuestas, en esta parte es donde se empieza a llamar cada modulo de la clase.
Cuando hace click en el boton para subir los archivos en el formulario se llama <action> definido. Que es una ruta de django para subir archivos.

Nota: El proceso anterior se ejecuta cuando estan precargados en la base de datos de administración, como son datos generales de cliente, nombre de impuesto, pais. Con el ID que escoje el Usuario al cargar el pdf, se realiza comparacón, y ejecuta y guarda elproceso y el archivo (ambos procesos cambiando el esado "Iniciado" el documento interno).




# Las mayores dificultades que se presentaron en el Proyecto EkchÝ

* Ir resolviendo cada una de las partes y de las caracteristicas para que funcionene en conjunto ejemplo:
 Hacer funcionar la base de datos con el modelo, y las funcionalidades de "extracción pdf" y "procesamiento excel".

* Implementar estructura para pasar los datos/ Dataset a los graficos, según lo requerido por cada uno de los elementos.

* Subir multiples archivos en Django y procesarlos. Se solucionó con  <stackverflow.com > https://stackoverflow.com/questions/20473572/django-rest-framework-file-upload/38388300#38388300 """Now in the api_view, we will be using the MultiPartParser decorator to upload files via a POST request. We would need a document_name and a file for this function to upload the file correctly as we had set the Model.
        imports
        from rest_framework.decorators import api_view, parser_classes
        from rest_framework.response import Response
        from rest_framework.parsers import MultiPartParser
        from .models import Document
        from .serializers import DocumentSerializer

        @api_view(['POST'])
        @parser_classes([MultiPartParser])
        def upload_document(request, filename, format=None):
            """
            A view that can accept POST requests with .media_type: multipart/form-data content.
            """
            file = request.FILES['file']
            doc = Document.objects.create(document_name=filename, file=file)
            # Do any thing else here
            serializer = DocumentSerializer(doc, many=False)
            return Response(serializer.data) """

* En el momento de hacer la subida en el pdf, no se podia obtener el identificador de la empresa, y era porque faltaba el campo <name> en el select del html.

* No se estaba cargando la libreria chart.js y se tuvo que poner el bloque de javascript en el evento <document.addEventListener("DOMContentLoaded",() => {>




## Tareas Foco 30/09/2022

* Probar para cada pais como funciona la subida de cada pais. crear y subir pdfs (se tienen que revisar cosas porque cada uno funciona de manera diferente)
* Subida de excel y hacer la comparación (pendiente definir tabla para guardar datos)
* Crear metodos según estructura de grafica de los indicadores (j) ok Pendiente probar
* Hacer el borrado de los pdf / (se borra registro bd pero no el archivo)
* Revisar proceamiento excel, probrar django y creación tabla BD.

## Tareas no urgentes
1. Tabla de autenticación (No prioritatio)
2. Subir a una API (No prioritatio)
3. Revision Docto helper.ipynb
4. Arreglar modelo de Procesamiento .drawio (pendiente / NP)
5. Actualizar mokup corrección
6. Indicadores definir y calcular ok
7. Anotar decisiones que se han tomado (Iterativo)








# Hecho


25 de septiembre
* Conectar la extracción
    - es sincronico ok
    - si es sincronico como manejar la espera? ok
    - hacer que cuando se suba el pdf se ejecute la extracción ok
    - Leer el pdf que se subió con la dirección de la BD ok
    - Hacer guardado de la extracción ok
* Crear una relación de extraccion y proceso (j) hacer relacion base de datos en proco en extraccion

atras del 24 de septiembre

* Clase leer Excel y procesamiento excel ok
* Ver librerias y graficos de py ok
*tabla con los valores del excel en DjangoCrear tables en excel (procesaiento excel <proceso>, <indicadores>,<resultaldos>(confirmar con  FOCO)
* buscar como subir múltiples PDF con Django y JavaScript

* hacer una clase, modelo de Django de la tabla
* y una clase que haga los cálculos

