## Prueba
    - Ejecutar xmltravel.py
    
## Problema inicial

- Tenemos un csv con las siguientes columnas
    - __start_time__: Día y hora
    - __encryp_client__: Id de cliente encriptado
    - __encryp_supplier__: Id de proveedor encriptado
    - __environment__: Entorno de máquinas en el que se ejecuta (ej: GCloud, Amazon, etc)
    - __hub_machine__: Id de máquina dentro del entorno donde se ha ejecutado
    - __hub_status_id__: ??? `-- TODO --`
    - __error_code__: Código de error según se define en [la documentación de travlegatex](https://docs.travelgatex.com/legacy/docs/payments/errorcodes/), el código `0` significa que la llamada ha ido correctamente
    - __Hits__: Número de llamadas que corresponde con todas las otras columnas
- Ejemplo de CSV:
```csv
start_time,encryp_client,encryp_supplier,environment,hub_machine,hub_status_id,error_code,Hits
2019-11-26 16:00:00 UTC,NdKnVLm0j+zEGGqvRZ+XCg==,lmFAlO8CfEXnRjZKUsUOnQ==,TGMADXTGPHUB48V,TGMADXTGPHUB48V,1,204,1573
2019-11-26 16:00:00 UTC,NdKnVLm0j+zEGGqvRZ+XCg==,x+7U3Q4PVCJwWhC2kQ55XA==,TGMADXTGPHUB03V,TGMADXTGPHUB03V,1,0,74
2019-11-26 16:00:00 UTC,NdKnVLm0j+zEGGqvRZ+XCg==,/yp6VBikmvZKV+888x13IQ==,TGMADXTGPHUB50V,TGMADXTGPHUB50V,1,204,457
2019-11-26 16:00:00 UTC,NdKnVLm0j+zEGGqvRZ+XCg==,nfZ0SLk1uPLLOR6DcWKZvQ==,TGMADXTGPHUB23V,TGMADXTGPHUB23V,1,105,5
2019-11-26 16:00:00 UTC,NdKnVLm0j+zEGGqvRZ+XCg==,pfdeEwwa4m0br/aGjtH6hg==,TGMADXTGPHUB11V,TGMADXTGPHUB11V,1,0,1243
2019-11-26 16:00:00 UTC,P5mOpBzXMjHZoXT622mpzA==,7GI2HGXMo3+VZTAIRQD2XA==,GCloud_Hotel,HOTEL-087,1,104,2
2019-11-26 16:00:00 UTC,M0fwQVJNiRVDbPjZ4e2I+A==,VmlndfxlHatmUHupV3zFkQ==,GCloud_Hotel,HOTEL-468,1,204,1
2019-11-26 16:00:00 UTC,Ha+C3qznSMt9CYB+rC9AEQ==,1tIXmC4AKMqNgkhObGKEeA==,GCloud_Hotel,HOTEL-815,1,105,3
2019-11-26 16:00:00 UTC,NdKnVLm0j+zEGGqvRZ+XCg==,EOBUoMnM/IUyNJTyjUUugA==,TGMADXTGPHUB02V,TGMADXTGPHUB02V,1,105,4
```

- El CSV contiene una estadísticas de llamadas a la API de TravelgateX que hace de "proxy" entre cliente (encryp_client) y proveedor (encryp_supplier).e indica el número de llamadas para cada código de error.

## Trabajo realizado

- Se ha creado un módulo generador de datasets configurable para hacer ETLs básicas sobre el dataset original.
- Se ha creado un dataset con los siguientes datos: hour_in_day,error_code,Hits,encryp_client+encryp_supplier+environment
- Se ha creado un módulo normalizador que codifica y decodifica los campos no numéricos
- Se ha creado un módulo de detección de anomalías con KNN
- Se ha creado un módulo de visualización de las predicciones para el dataset generaro.

## TODO
    
- __PARSEO:__ 
    - Realizar una función que recoja los datos del CSV y transformar el campo de fecha a varios campos con día, mes, año, hora. 
    - Normalizar datos.
- __ENTRENAMIENTO:__ 
    - Seleccionar algoritmo a utilizar (KNN, ABOD). 
    - Preparar algoritmo. 
    - Entrenar "sistema neuronal"
- __COMPROBACIÓN:__ 
    - Contrastar datos contra el algoritmo. 
    - Output:
        - CSV
        - Consola: listado de identificadores con IN/OUT.
        - JSON
        - Gráfica


