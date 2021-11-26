import arcpy, os, sys
from arcpy import env
env.workspace = arcpy.GetParameterAsText(0)
outfolder = arcpy.GetParameterAsText(1)
fc = arcpy.ListFeatureClasses('*.shp*','Polygon')
for fcs in fc:
    basename = os.path.splitext(fcs) [0]
    output = outfolder + basename + 'Out.shp'
    out = arcpy.Buffer_analysis(fcs, output, '500 Meters')
    arcpy.AddMessage(out)

