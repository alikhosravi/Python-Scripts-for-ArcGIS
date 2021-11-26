

import sys, arcpy



arcpy.env.workspace = arcpy.GetParameterAsText(0)

fcs = arcpy.ListRasters()

#PRINT basic information about each feature class in the folder.
print("Feature classes in folder {0}".format(arcpy.env.workspace));

for fc in fcs:
                print(fc)
                arcpy.AddMessage(fc)
		arcpy.AddMessage('----------------')
print("Feature class list complete");
                
