
# Eyetracker-OpenSesame

Este script nace con el fin de procesar los archivos que entrega OpenSesame al realizar un experimento con el eyetracker y covertilos en datos con
un formato mucho mas amigable de analizar y procesar, los detalles a continuación.

## Data

Para este script se debe colocar todos los archivos que se crean al terminar el experimento en una carpeta, especialmete deben estar los archivos.csv y archivos.tsv 
de los participantes. 
IMPORTANTE: Los archivos deben tener el mismo nombre y solo ir variando (-número) el número del participante.
            EJEMPLO-> eyetask-1.csv, eyetask-2.csv, eyetask-3.csv, eyetask-4.csv 
                      eyetask-1.tsv, eyetask-2.tsv, eyetask-3.tsv, eyetask-4.tsv 
                tiene que ser asi, ya que de esta manera funciona el código
                

## Instrucciones

Al finalizar el experimento, se tendrán 3 archivos: participante-1.csv, participante-1.tsv y participante-1.log. Estos archivos tienen toda la información
sobre la prueba que realizo el participante-1. 
el archivo.tsv contiene la informacion recopilada por el eyetracker, esto sucede ya que la API del eyetracker se comunica con OpenSesame mientras el experimento
es llevado a cabo. Lo ideal es recibir la información tal cual viene ya que todos los procesos dependen de la API y al alterar algo, esto puede colapsar. 
Por ende, es mejor recibir todos los datos que rastrea el eyetracker en este archivo.tsv

Por otro lado, OpenSesame rastrea por su lado la informacion del experimento, lo mejor es tambien no editar nada y dejar que todos los datos se almacenen en el .csv y en el .log

ESTE SCRIPT HACE LO SIGUIENTE:

En una carpeta se deben colocar absolutamente todos los archivos que se generaron, se deberia ver algo asi:
  -input_dir --> participante-1.csv, participante-1.tsv y participante-1.log
                 participante-2.csv, participante-2.tsv y participante-2.log
                 participante-3.csv, participante-3.tsv y participante-3.log
  
Todos los archivos .tsv se transforman a un archivo .csv, con el uso de expresiones regulares se deja el mismo nombre que tenian original pero se le agrega -et 
para identificar que este tiene la informacion del eyetracker. 

Luego se crea una carpeta que se llama et-and-os-results (et - eyetracker y os - OpenSesame) se guardan todos los archivos .csv originales y los .tsv que ahora 
son -et.csv, es decir 
- et-and-os-results --> participante-1.csv participante-1-et.csv
                        participante-2.csv participante-2-et.csv
                        participante-3.csv participante-3-et.csv
  
Despues el código continua, y por participante junta la información del eyetracker + la del experimento en Opensesame en un solo archivo llamado 
all-data-participante-1.csv
La identificacion de los pares de archivos que van juntos (por ejemplo participante-1.csv participante-1-et.csv ) se hace tambien con expresiones regulares, 
es por ello que se hace incapie en el nombre de los archivos a la hora empoezar la realización del experimento con los participantes. 

el resultado es un nuevo directorio llamado all-results-by-subjects
- all-results-by-subjects --> all-data-participante-1.csv
                              all-data-participante-2.csv
                              all-data-participante-3.csv
  
Esto se hace asi, ya que finalmente con el código de Sebastiaan Mathot (situado en la página de la documentación de OpenSesame -Manuals - Data logging)
se obtiene 1 solo archivo.csv que contiene a todos los participantes, pero solo se conservan columnas especificas (aquellas que tienen la información relevante a analizar). Esta última parte recorre all-results-by-subjects, se debe especificar en el código cuales son las columnas que se quieren conservar y se obtiene un solo .csv con esa información


## Output

Un archivo .csv que contiene la informacion en columnas la informacion de parametros especificos de todos los participantes del experimento, por ejemplo si solo se necesita la dilatacion de la pupila, el tiempo de respuesta, la repsuesta que puso el participante y la respuesta correcta se tendran esos valores de todos los participantes pero en un solo archivo, más todos los directorios utilzados anteriormente

## References

https://osdoc.cogsci.nl/3.3/manual/logging/


