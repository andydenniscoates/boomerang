import c4d
#Welcome to the world of Python

 # Writtn by Andy Coates 2019
 # www.andy-coates.com
 # andy@andy-coates.com
 #
 #

def Walker(obj):
    if not obj: return

    elif obj.GetDown():
        return obj.GetDown()
    while obj.GetUp() and not obj.GetNext():
        obj = obj.GetUp()
    return obj.GetNext()

def main():

    doc.ExecutePasses(None, True, True, True, c4d.BUILDFLAGS_NONE)

    file = c4d.storage.SaveDialog(c4d.FILESELECTTYPE_ANYTHING, title='Save csv file as', force_suffix='csv')
    csv_file = open(file, 'w')

     # hardcode the header into the document, this is the mapping matters format
    csv_file.write('Projector_Name,Projector_Qte(Stack),Projector_Native-Rez-X,Projector_Native-Rez-Y,Projector_Lumens(lux),Projector_Brightness(%),Projector_Total_Lumens(lux),Projector_Trow-Ratio,Lens_Shift-H(%),Lens_Shift-V(%),Lens_X,Lens_Y,Lens_Z,Pitch(deg),Yaw(deg),Roll(deg),Target_X,Target_Y,Target_Z,Target_Distance,Target_Width,Target_Height,Target_Illuminance,Target_DPI,Unit_Dim,Unit_Illuminance,Projector_UUID\n')



    obj = doc.GetFirstObject()
    while obj:
        if obj.GetType() == 5102:  #Light ID is 5102  camera ID is 5103 OBJECT_NULL=5140,
            #while startingFrame < endFrame:
                name = obj.GetName()
                obj_matrix = obj.GetMg()
                position = obj_matrix.off
                rotation_rad = c4d.utils.MatrixToHPB(obj_matrix,c4d.ROTATIONORDER_XYZGLOBAL)
                rotation_deg = c4d.Vector(c4d.utils.Deg(rotation_rad.x), c4d.utils.Deg(rotation_rad.y), c4d.utils.Deg(rotation_rad.z))

                distance = obj[c4d.LIGHT_DETAILS_OUTERDISTANCE,1]
                lumens = obj[c4d.ID_USERDATA,5]
                target_x = obj[c4d.ID_USERDATA,14]
                target_y = obj[c4d.ID_USERDATA,15]
                target_z = obj[c4d.ID_USERDATA,16]
                rez_x = obj[c4d.ID_USERDATA,4]
                rez_y = obj[c4d.ID_USERDATA,2]
                throw_ratio = obj[c4d.ID_USERDATA,3]
                t_width = obj[c4d.ID_USERDATA,11]
                t_height = obj[c4d.ID_USERDATA,10]

                lens_x = position.x
                lens_y = position.y
                lens_z = position.z
                pitch = rotation_deg.x
                yaw = rotation_deg.y
                roll = rotation_deg.z
                stack = 1
                brightness = 100
                total_lumens = lumens
                shift_h = 0
                shift_v = 0
                t_illum = obj[c4d.ID_USERDATA,9] #Target Illumination is resulting LUx based on screen area and limnes
                t_dpi = 0
                #unit_dim = m        FORCED
                #unit_illum = 0      FORCED




                line = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,m,lux,'%(name,
                                                        stack,
                                                        rez_x,
                                                        rez_y,
                                                        lumens,
                                                        brightness,
                                                        total_lumens,
                                                        throw_ratio,
                                                        shift_h,
                                                        shift_v,
                                                        lens_x,
                                                        lens_z,
                                                        lens_y,
                                                        pitch,
                                                        yaw,
                                                        roll,
                                                        target_x,
                                                        target_z,
                                                        target_y,
                                                        distance,
                                                        t_width,
                                                        t_height,
                                                        t_illum,
                                                        t_dpi)
                                                        #unit_dim,
                                                        #unit_illum)


                csv_file.write(line + '\r\n')

                doc.ExecutePasses(None,True, True, True, c4d.BUILDFLAGS_NONE)
        obj = Walker(obj)
    csv_file.close()


    print (name,lumens, 'lensX',lens_x, 'lensY',lens_y, 'lensZ',lens_z, 'pitch', pitch, 'yaw', yaw, 'roll', roll, 'tarX',target_x, 'tary',target_y, 'tarZ',target_z, distance )
    print ('theres your data')

if __name__=='__main__':
    main()