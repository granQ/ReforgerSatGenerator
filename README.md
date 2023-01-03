# ReforgerSatGenerator
A python tool for Arma Reforger to help combine the mask output from would bench to a satellite image. 

Please note!!!
This script don't create something amazing, thats dependet on your mask and the ground textures you provide. 
This is however very fast, free and possible to update with a on new exported mask. 

***********
* Credits *
***********
Basically all code is made by Bjorn Dahlgren.

************************************
* Installation (for windows users) *
************************************

1) I recommend to download Pyhton from Windows store.
2) Run Command, with the following: python3 -m pip install --upgrade Pillow

3) Download all files from here, default installation path is: 
  P:\ReforgerSatGenerator\ReforgerSatGenerator.py
  
4) Export your mask from the world tools to the folder (mask_export)
5) Run the batfile, soon your satellite.png dhall been created.

****************
* Useful notes *
****************

In the pyhton script you can choose between tiled or stretched backgrounds, as well as blured or not.
Recommend to try out what is best for combination for your project.

Backgroundcolor can be changed (hex code) but is default a dark green, this will be visible in areas were your mask might not be equal to 100% (e.g 25% grass, 25% pebbles and 25% dirt).

