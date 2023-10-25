**Arborescence du projet**

project_directory/
    |- app.py
    |- models/
    |   |- base.py
    |   |- table1.py
    |   |- table2.py
    |- Dockerfile


**Docker commande** 

`docker build -t nom_de_l_image .` Attention au "." à la fin
`docker run -d -p 3306:3306 --name nom_du_conteneur -e MYSQL_ROOT_PASSWORD=le_mot_de_passe nom_de_l_image`
