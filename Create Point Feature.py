

import arcpy


Workspace = arcpy.GetParameterAsText(0)

Fc = arcpy.GetParameterAsText(1)

database = arcpy.CreateFileGDB_management(Workspace,Fc)

namedataset = arcpy.GetParameterAsText(2)

dataset = arcpy.CreateFeatureDataset_management(database,namedataset,'WGS 1984')

FeatureName = arcpy.GetParameterAsText(3)

feature = arcpy.CreateFeatureclass_management(dataset,FeatureName,"POINT")
                
