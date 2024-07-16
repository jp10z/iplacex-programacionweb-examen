# IPLACEX - Programación Web - Exámen

Este repositorio contiene el desarrollo del exámen 3 de la asignatura
`Programación web`.

El desarrollo está aún curso.

## Datos

- Nombre: José Ramos
- Periodo: 2024-2B
- Asignatura: Programación Web

## Consideraciones

- Estoy usando .gitignore para no subir al repositorio la carpeta del entorno virtual (venv) y otros archivos temporales, dado que no sería buena práctiva.

- El paquete flask lo instalo mediante archivo requeriments.txt, luego de la instalación utilicé el comando `pip freeze > requeriments-freeze.txt` para volcar la info de las versiones de las dependencias para no tener problemas de compatibilidad en futuras instalaciones.

## Ejecutar

1. Crear entorno virtual

```shell
python3 -m venv venv
```

2. Ingresar a entorno virtual

```shell
source venv/bin/activate
```

3. Instalar requisitos usando pip

```shell
pip install -r requeriments-freeze.txt
```

4. Levantar servicio

```shell
python3 app/main.py
```

5. Ingresar con un navegador a la página

```
http://localhost:5000/
```

## Capturas de pantalla

(Pendiente)