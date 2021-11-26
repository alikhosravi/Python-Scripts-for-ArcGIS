import arcpy

fc = arcpy.GetParameterAsText(0)

fca = arcpy.ListFields(fc)

for i in fca:
    b = i.name, i.length, i.baseName, i.precision, i.type, i.editable, i.required
    a.append(b)

for j in a:
    print(j)
    arcpy.AddMessage('----------------------------------------------------')
    arcpy.AddMessage(j)