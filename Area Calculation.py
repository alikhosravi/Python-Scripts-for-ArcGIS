import arcpy

fc = arcpy.GetParameterAsText(0)
fcout = arcpy.GetParameterAsText(1)

arcpy.CalculateAreas_stats(fc, fcout)

arcpy.AddMessage('-------------------')

arcpy.AddMessage('Area in Sq Meters')
arcpy.AddMessage('-------------------')
                
