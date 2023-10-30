@here Cette fonctionnalité, va en effet être plus compliqué qu'il n'y parait. N'y allez que quand vous aurez stabilisé, a minima la phase 2/3. 

Compliqué car : 
- vous allez probablement devoir recourir à l'utilisation de `yield` en python (ce qui est l'occasion de le découvrir en soit) 
  * https://realpython.com/introduction-to-python-generators/
  * https://fr.wikipedia.org/wiki/G%C3%A9n%C3%A9rateur_(informatique)
- Ré-ecriture de votre code d'affichage en streamlit pour supporter le stream
- parsing en temps réél dans le cas de la détection du code avec la triple backquote ``
- détection de la fin  du stream pour passer en mode édition.