# -*- coding: utf-8 -*-

# This script imports Hansen Solubility Parameter data for 
# polymers as listed in the Polymer Handbook Ch. 14, and
# makes a nice 4D plot with the experimental parameter
# values in 3-D space and a color-bar to indicate the size
# of the radius of interaciton.  The radius itself is too
# large to make a pretty plot, all the spheres would
# overlap.  In accordance with Hansen's approach, the
# Delta-d axis is compressed by a factor of two to give
# sphereical regions of "good" solvents.
# 
# This graphic will appear in the abstract to the POLY
# symposium on Industrial Polymer Science at the August '19
# ACS National Meeting in San Diego  

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as mplt
import numpy as np
import os
import csv

Delta_d = []
Delta_p = []
Delta_h = []
Radius = []

# Expect the file in the same folder as the code
csvfile = os.path.join('Polymer_HSP_Data_from_Handbook.csv')

# We'll use the CSV parser.
with open(csvfile, 'r') as In_File:

    Reader = csv.reader(In_File,delimiter=",")
    # Keep the header just in case
    Header = next(Reader)
    # This isn't really necessary, but it makes it much easier to follow
    for File_Row in Reader:
        Delta_d.append(float(File_Row[3]))
        Delta_p.append(float(File_Row[4]))
        Delta_h.append(float(File_Row[5]))
        Radius.append(float(File_Row[6]))
# Check
print(Delta_d, Delta_p, Delta_h, Radius)

Radius_Color = [Color_Val / 25.0 for Color_Val in Radius]
# Generate the plot objects
fig = mplt.figure(figsize = (6,6), dpi = 150 )
ax = mplt.axes(projection='3d')
# Re-scale the plot so that it is shortened by a factor of 2 in
# the delta-d direction per Hansen for spherical solubility regions
#scale_x = 2.0
#scale_y = 1.0
#scale_z = 1.0
#ax.get_proj = lambda: np.dot(Axes3D.get_proj(ax), np.diag([scale_x, scale_y, scale_z, 1]))
ax.set_xlim(15, 25)
ax.set_ylim(0, 20)
ax.set_zlim(0, 20)
# Build the plot itself
Im = ax.scatter3D(Delta_d, Delta_p, Delta_h, s=60, c=Radius_Color, cmap='coolwarm')
# Make walls transparent for better visibility of points
ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
# Make labels and tick marks
ax.set_xlabel(r'$\delta_d$')
ax.set_ylabel(r'$\delta_p$')
ax.set_zlabel(r'$\delta_h$')
ax.set_xticks([15, 17.5, 20, 22.5, 25])
ax.set_yticks([0, 5, 10, 15, 20])
ax.set_zticks([0, 5, 10, 15, 20])
# Add colorbar 
cbar = mplt.colorbar(Im,ticks=[0.2, 0.4, 0.6, 0.8, 1.0],shrink=0.7,aspect=14)
cbar.set_ticklabels(['5','10','15','20','25']) 
cbar.set_label("Radius of Interaction")
# Save the file, then finally, show the result (order matters)
mplt.savefig('graph_for_abstract.jpg')
mplt.show()
# Note that the final, published 
# version has the contrast adjusted 
# off-line for a better overall look
