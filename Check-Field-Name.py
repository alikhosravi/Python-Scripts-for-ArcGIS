import arcpy

from arcpy import env

fc = arcpy.GetParameterAsText(0)

fcfield = arcpy.ListFields(fc)

fname = arcpy.GetParameterAsText(1)


found = False


for fcd in fcfield:
    if fcd.name.lower() == fname.lower():
        print('Field {0} Found'.format(fname))
        arcpy.AddMessage(fname)
        arcpy.AddMessage('Found')
        found = True
    else:
        print('Field {0} Not Found'.format(fname))
        found = False
        arcpy.AddMessage(fname)
        arcpy.AddMessage('Not Found')
        

