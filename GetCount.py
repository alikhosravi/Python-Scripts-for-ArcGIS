

import arcpy


fc = arcpy.GetParameterAsText(0)


desc = arcpy.GetCount_management(fc)


#PRINT basic information about each feature class in the folder.

arcpy.AddMessage('-------------------')
arcpy.AddMessage('Total Count is:')
arcpy.AddMessage(desc)
arcpy.AddMessage('-------------------')
                
