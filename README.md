LO NECESARIO
1-Tener una maquina virtual con odoo
2-putty(en caso de trabajar con windows)
EMPEZAMOS
1-Lo primero que debemos hacer es iniciar nuestro odoo para ver que todo funciona correctamente
esto se hace desde la terminal de putty con los siguientes comandos:
cd /opt/odoo
y lanzamos nuestra base ./odoo.py
2-Una vez hecho esto vamos a nuestro explorador y ponemos la ip de nuestra maquina virtual con la terminacion :8069 si todo funciona podemos empezar ya con la instalacion de nuestros modulos
3-Abrimos el netbeans y creamos un proyecto php con remote server y lo configuramos todo correctamente, anteriormente siempre instalabamos el theme_default en este caso no instalaremos el openacademy que es con el q vamos a trabajar.
4-Una vez creado nuestro proyecto probamos que todo funciona correctamente desde el mismo proyecto podemos hacer un upload para ver si esta perfecto.
YA PODEMOS EMPEZAR CON EL CODIGO
Lo primero que debemos modificar son todos los siguientes archivos:
1-en openrp.py sustituimos todo el contenido por el que viene a continuacion:
# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """Manage trainings""",

    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}

2-openacademy/init.py
# -*- coding: utf-8 -*-
from . import controllers
from . import models

3-openacademy/controllers.py
# -*- coding: utf-8 -*-
from openerp import http

# class Openacademy(http.Controller):
#     @http.route('/openacademy/openacademy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openacademy/openacademy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openacademy.listing', {
#             'root': '/openacademy/openacademy',
#             'objects': http.request.env['openacademy.openacademy'].search([]),
#         })

#     @http.route('/openacademy/openacademy/objects/<model("openacademy.openacademy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openacademy.object', {
#             'object': obj
#         })

3-demo.xml
<openerp>
    <data>
        <!--  -->
        <!--   <record id="object0" model="openacademy.openacademy"> -->
        <!--     <field name="name">Object 0</field> -->
        <!--   </record> -->
        <!--  -->
        <!--   <record id="object1" model="openacademy.openacademy"> -->
        <!--     <field name="name">Object 1</field> -->
        <!--   </record> -->
        <!--  -->
        <!--   <record id="object2" model="openacademy.openacademy"> -->
        <!--     <field name="name">Object 2</field> -->
        <!--   </record> -->
        <!--  -->
        <!--   <record id="object3" model="openacademy.openacademy"> -->
        <!--     <field name="name">Object 3</field> -->
        <!--   </record> -->
        <!--  -->
        <!--   <record id="object4" model="openacademy.openacademy"> -->
        <!--     <field name="name">Object 4</field> -->
        <!--   </record> -->
        <!--  -->
    </data>
</openerp>

4-models



















































