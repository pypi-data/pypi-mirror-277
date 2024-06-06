# User Interface

## Overview

The Steered Molecular Dynamics (SMD) method was developed to mimic Atomic Force Microscopy (AFM) pulling experiments, where external forces are applied to probe biomolecules in addition to their intrinsic forces defined in classical MD simulations. SMD simulations have been widely used to explore the mechanics of biomolecular processes such as unbinding and unfolding at the single-molecule level.
Here, we present smdanalysis, a Python3 user-friendly package that helps users to analyze their data efficiently.

## Usage

_Note that it is recomanded to create a virtual environment for each software package.
A virtual environment manages python requirements and versions and it is very useful if you
are working on or want to use different parallel packages/projects._


-To create a virtual anaconda environment containing the software package, use the yml file:

`conda env create -f env.yml`



#### At the end of the session:

you might want to deactivate the environment:

`conda deactivate`


In case you want to delete the environment:

`conda remove -n yourenvname --all`



**To install/run the software on your local machine :**

`git clone https://gitlab.com/fm4b_lab/smdanalysis.git`

Once you clone the package. Run on the terminal the following:
`cd smdanalysis`




**What librairies does the package require:

Below details:

- [SciPy](https://www.scipy.org/install.html#pip-install): `'find_peaks'` function from Scipy.signal package is used for peak detection, it can take 8 optional parameters, most important one for our study is [prominence](https://en.wikipedia.org/wiki/Topographic_prominence).
- [Numpy](https://numpy.org/install/) : library is used to empower users to connect their data with the large and rapidly growing ecosystem of data science tools available more broadly in the community.
- [ProDy](http://prody.csb.pitt.edu/index.html) is an open source python package for protein structural dynamics analysis. It is used in software to compute extensions between C-alpha atoms of different residues.
- [Matplotlib](https://matplotlib.org/): is used for data visualization.
- [Pandas](https://pandas.pydata.org/)  provide extremely streamlined forms of data representation. This helps to analyze and understand data better. Pandas was developed to mainly handle large datasets efficiently. It helps to save a lot of time by importing and exporting large amounts of data very fast.
- [Tkinter](https://docs.python.org/3/library/tk.html) is used for graphical user interface, It provides a robust and platform independent windowing toolkit.





## Needed files

_Please note that this software package supports DCD files of NAMD 2.1 and later._

To be able to run the software and perform the analysis make sure you
have three files:

* The log file of SMD simulation: this files contains all the information concerning 
the simulation such as: the velocity, the timesteps, the (x, y, z) coordinates
of the direction of pulling...etc.

* The DCD file of trajectory: This file contains all the atoms positions in Angstrom at each time step.
The coordinates of each atom within a given time step are stored in this file and called frames.

* The PDB file of structure: This fle store the information that describes the 3D
structure of biomelecules, the are downloadable from the PDB (Protein Data Bank).


## Usage

To start the Graphical User Interface. Run on the terminal the following command:

 `python3 main.py`

Once the interface appears, upload the log file of Steered Molecular Dynamics (SMD) simulation.
You will see the force-distance curve on the interface as soon as the file has loaded.

## Force-Distance analysis

A force-distance curve represents the forces applied to the biomolecule vs tip-sample
distance. 

The screenshot shows a typical data analysis in the SMD software interface.
The plot at the left shows a force-distance curve. On the right are the main controls. 

![force-distance](outputs/Capture_d_écran_2021-01-18_à_11.22.44.png)

You have the possibility to export the curve in .png or .pdf format. You can also export the data in a .csv file.

On the left of the interface are the energy parameters. You can select the parameter of your interest and plot the curve by pressing the `plot energy parameter` button.


## Peak detection

In the force-distance profiles recorded in SMD simulaions, in case of protein unbiding or unfolding of single or multidomain complexes, a sudden drop in the force profile will be observed. These peak like drops in the force profile gives us unfolding or unbiding forces. 

In the screenshot, you can see the detected peaks on the curve on the left. 
On the right, you can use the default values (knots and prominence).

The algorithm used for smoothing is Natural Cubic Spline also referred to as Numerical Interpolation. It is a
piece-wise third-order  polynomial that is twice continuously differentiable. It fits all
the data points and is appropriate for large datasets. First, the dataset is segmented, the number of these
segmentation points is referred to as `knots`. After that, an interpolant is calculated between each 
two `knots`. In the interface, a default value of `knots` is suggested. After setting a `knots` value, make sure you press `plot force vs time` to see the smoothed curve.


To detect only significant peaks that correspond to unfolding/unbiding, a parameter called `prominence`
is used. The prominence of a peak measures the minimum height necessary to get down from the summit 
to any heigher baseline. It measures how much a peak stands out from the other peaks. 

 
Once the `Detect peaks` button is pressed, a table containing all the detected
 peaks appears just below the control parameters. 
You can save the peaks for further analysis. 


![peak detection](outputs/1st_peak_detection.png)


You have the possibility to export data. An example  of the exported .csv file is available 
in the [Ouputs](https://gitlab.com/ismahene_mesbah/smd_software/-/blob/master/outputs/slopes.csv)


## Extension

Extension analysis can be performed on the third tab, entitled `extension` . 
Start by uploading the PDB file of structure. End-to-end coordinates will appear.
 Then, upload the DCD file of trajectory. 
The extension will be computed automatically from end-to-end and the extension VS force curve will appear.
 You can modify the coordinates and compute the extension between the start and
 end residues of each domain. 
The screenshot shows the extension of residues of each domain vs time curve on the left, 
all the control parameters are on the right. 


 ![extension vs time](outputs/extensionVStime.png)



## Peak detection from the extension

 
Computing and plotting the dereivative of the extension is very useful to detect
 the increase in the original extension-time graph. 
This approach has been implemented to refine and  automatize the determination of 
which domain unfolds at which force peak. 
Detected peaks can be selected by the user and superposed on the force-time curve. 


Start by plotting the derivative of extension. You can smooth the data using the Gaussian filter, 
you will need to enter the size of the window. 

![extension derivative](outputs/2nd_peak_detection_derivative.png)


You can give the number of peaks you want to detect or a height threshold then  press 
the `Detect peaks` button.
 The peaks will appear in the table on the right. 

You can click on the peaks of your ineterst and save them or  plot them on the force vs time curve. 
If you want to check your list press the `Check list of peaks` button. If you want to modify/delete
some peaks click on the same button before modifying/deleting the peaks.


The screenshot shows the force-time curve after selecting the peaks from the table.

 ![extension](outputs/FD_detection_from_extension_multi_domain.png)  


## Loading Rates

After selecting and saving the peaks from the previous analysis. You can calculate the loading rates at
 each peak. The loading rates are obtained by fitting a linear line to the force-time data.

 The sreenshot shows an example of slopes (loading rates) plotting at a distance of 1 nm. 



 ![slopes](outputs/slopes.png)

