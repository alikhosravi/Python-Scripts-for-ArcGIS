
import arcpy, os

folder = arcpy.GetParameterAsText(0)

filelist = os.listdir(folder)

for i in filelist:
    if i.endswith('.jpeg'):
        print(i)
        arcpy.AddMessage('-------------------')
        arcpy.AddMessage(i)

                
