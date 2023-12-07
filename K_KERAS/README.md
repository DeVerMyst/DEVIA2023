**RGB Classification data set**

L'idée est de réussir à faire un classification binaire sur un jeu de données 3D (couleurs)
Le dataset est gros et il devra être traité

Dataset: https://www.kaggle.com/c/dogs-vs-cats/data?select=train.zip 

il fait 853.96MB et est composé de photos de chien et de chat

Quelques lignes pour vous guider: 

* la fonction load_img de keras est utile pour charger les données et leur donner la taille que l'on souhaite
* la fonction img_to_array est utile pour transformer une image en array
* https://keras.io/api/data_loading/image/

Conseil/rappel pour l'architecture d'un classificateur d'image:
* couche d'entrée
* couches cachées
  * couches de convolution et autre (régularisation, normalisation, réduction de données)
* couche de sortie
  * couche d'applatissement 
  * couche de classification

Procédure
* Analysez l'équilibre des classes
* stockez les images dans une liste d'array et générez les labels (0 chien et 1 chat)
* sauvegardez votre array (numpy.save) ou autre
>save('dogs_vs_cats_photos.npy', photos)
save('dogs_vs_cats_labels.npy', labels)
* découpez le jeu de données en 3 en maintenant l'équilibre des classes pour le Train
  * Train (60%)
  * Valid (20%)
  * Test (20%)
  
**Premier test**

* Développez un premier model convolutif simple pour tester puis augmenter la compléxité du réseau. 
* Pour chaque architecture conservez dans un document l'architecture, les plots des loss et des metrics ainsi que le rapport de classification 

**Régularisation**
* ajoutez des couches de régularisation après les couches de convolutions
  
**Normalisation**
* ajoutez des couches de normalisation après les régularisations 
  
**Data Augmentation**
* augmentez votre dataset en modifiant vos images, refaire votre dataset
  * https://keras.io/api/layers/preprocessing_layers/image_augmentation/
  
**Exploration du transfert learning**
* Découvrez le transfert learning en chargeant un des modèles existant dans Keras comme le VGG16 par exemple! Et enlever le classificateur!
  * https://keras.io/api/applications/vgg/
* Rendez les couches du modèle non modifiable pour ne pas être entrainé une deuxième fois: 
```python 
# load model
 model = VGG16(include_top=False, input_shape=(224, 224, 3))
 # mark loaded layers as not trainable
 for layer in model.layers:
    layer.trainable = False
```
* Ajoutez une couche de classification qui sera la votre pour faire de la classification binaire
  * Afin d'entrainer votre propre classificateur spécialisé chien et chat il vous faut le créer 
```python 
 # add new classifier layers
 flat1 = Flatten()(model.layers[-1].output)
 class1 = Dense(...)(flat1)
 output = Dense(...)(class1)
 # define new model
 model = Model(inputs=model.inputs, outputs=output)
 ```