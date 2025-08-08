bl_info = {
    "name": "Valor Único",
    "blender": (3, 0, 0),
    "category": "3D View",
}

import bpy

class MisPropiedades(bpy.types.PropertyGroup):
    mi_valor: bpy.props.FloatProperty(
        name="Mi Número",
        description="Un valor numérico",
        default=1.0
    )

class MiPanel(bpy.types.Panel):
    bl_label = "Valor Único"
    bl_idname = "PT_ValorUnico"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Simple"

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene.mi_dato, "mi_valor")

classes = [MisPropiedades, MiPanel]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.mi_dato = bpy.props.PointerProperty(type=MisPropiedades)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.mi_dato

if __name__ == "__main__":
    register()
    
"""
import bpy


# función para obtener la escala de extrucción en circulos 
def clcPorcentajeCiculoInterior(padre, hijo):
    operacion = (hijo * 100) / padre
    resultado = "Porcentaje de la circunferencia del hijo: ",operacion
    return resultado 


 
# Exterior, deseado retorna elporcentaje que se 
# introduce a la medida del escalado
interior = clcPorcentajeCiculoInterior(35, 20)

print(interior)

"""