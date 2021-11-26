import arcpy


fc = arcpy.GetParameterAsText(0)

clipfc = arcpy.GetParameterAsText(1)

fcout = arcpy.GetParameterAsText(2)


arcpy.Clip_analysis(fc, clipfc, fcout)              
