{
    'name': "Website Sale", # Required
    'version': '14.0.0.0.0',    # 14.0.[major].[minor].[patch]
    'depends': ["base"],  # Default: ['base'], deben estar instaladas previamente 
    'external_dependecies': {"Python":["open"], "bin":["libreoffice"]},  # Librerías necesarias 
    'author': "Author Name",
    'website': 'yourwebsite.com',   # Website del author,
    'maintainer': 'Beatriz Balack',   # Encargado del mantenimiento
    'license': 'GLP-2',     # Default: LGPL-3, 
    'category': 'Herramientas', # Sirve para clasificación, Not required
    'description': """Control de Plantas y clientes""", # Comillas triples
    'application': True,
        # True: Es un modulo completo, se puede instalar
        # False: Añade una funcionalidad extra a un modulo ya existente
    'installable': True, # Si se puede instalar desde la Web Ui
    'auto_install': False,  # Default: False 
    'pre_init_hook': 'version_check',  # Función antes de la instalación
    'post_init_hook': '_auto_install_l10n',  # Función después de la instalación,
    'uninstall_hook': '_auto_install',
    'data': [
        # Los datos siempre cargan en la instalacion, solo se cargan cuando se instala o actualiza el modulo. Secuencia debe ser la siguiente:
        'data/data.xml',
        'security/ir.model.access.csv',
        'wizard/wizard.xml'
        'views/views.xml',
        'report/report'
    ],
    'css': "static/src/css/index.css",
        # Dirección: 'static/src/css'
    'images': "static/src/images/logo.png",
        # Imagenes del modulo
    'demo': [
        # Es opcional tener un demo
        # Data que se usara como demostración
    'demo/demo_data.xml',
    ],
    'external_dependencies': {
        'python': ['requests'],
        'bin': ['wkhtmltopdf'],
    },
}

