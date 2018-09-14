# -*- coding: utf-8 -*-
import arcpy,os,time,exceptions
t_inicio=time.clock()# captura el tiempo de inicio del proceso
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(3116)
arcpy.env.overwriteOutput = True

try:
    infea=arcpy.GetParameterAsText(0)
    feaUpdate= arcpy.GetParameterAsText(1)
    capa_salida=arcpy.GetParameterAsText(2)

    if __name__ == '__main__':
        print "Ejecutando erase a 64bits ...."
        print infea , feaUpdate,capa_salida
        arcpy.Erase_analysis (in_features=infea, erase_features=feaUpdate, out_feature_class=capa_salida,cluster_tolerance="")

except exceptions.Exception as e:
    print e.__class__, e.__doc__, e.message
    os.system("pause")