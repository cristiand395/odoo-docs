## Requisitos 
- Sistema operativo: Linux, Windows con WSL2 o Mac OS
  - [Windows con WSL2](windows-con-wsl2): Se recomienda más de 8gb de RAM porque consume muchos recurso
- [Git y GitHub](#git-y-github)
- [Python](#python)
- [PostgreSQL](#postgresql)
- [Repositorio Odoo](#repositorio-odoo)
- [Repositorio OCA](#repositorio-oca)

## Windows con WSL2:
(Fuente: https://learn.microsoft.com/es-es/windows/wsl/install)
- Desde la Windows Store instalar una distribución de Ubuntu (Ejemplo: 20.04.5 LTS)
- A partir de ahora ejecutar la terminal de Windows siempre como administrador
```sh
wsl --install
```
- Reiniciar el ordenador

## Git y GitHub
```sh
sudo apt install git
git config --global user.name "Nombre completo"
git config --global user.email "tu@email.com"
ssh-keygen -t ed25519 -C "tu@email.com"
ssh-add ~/.ssh/id_ed25519
sudo apt-get install xclip
xclip -sel clip < ~/.ssh/id_ed25519.pub  # Copiar en portapapeles la llave
```
- Agregar la clave privada a la cuenta de GitHub. [Guía]('https://docs.github.com/es/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account')
  
## Python
```sh
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.8 pip python3-pip python3-dev libxml2-dev libxslt1-dev libcups2-dev libldap2-dev libsasl2-dev libssl-dev libpq-dev libjpeg-dev pre-commit -y
```

## PostgreSQL
```sh
sudo apt install postgresql -y
sudo service postgresql start   # Iniciar servidor
sudo su - postgres
```
```sql
CREATE ROLE <rolename>;
ALTER USER <username> WITH SUPERUSER;
ALTER USER <username> WITH LOGIN;
ALTER ROLE <rolename> with password "<db-password>";
ALTER ROLE <rolename> SET client_encoding = 'UTF8';
CREATE DATABASE <database>;
ALTER DATABASE <database> OWNER TO <username>;
\q
```
- Si van a restaurar una base de datos:
```sql
CREATE DATABASE <database>;
ALTER DATABASE <database> OWNER TO <username>;
```
- SI es un archivo comprimido (.tar.xz), dentro de la carpeta del archivo:
```sh
xz -dkc <file>.tar.xz | pg_restore -Ox -d <database>
```

#### Estructura de carpetas:
```
odoo
├── oca
│    └── Módulos oca
├── odoo
│    └── Odoo base
└── custom
     └── Módulos Custom
```

##### Repositorio Odoo:
`pwd: /odoo/odoo`
```sh
git clone https://www.github.com/odoo/odoo --depth 1 --branch 14.0 --single-branch . 
pip3 install -r requirements.txt
cd /tmp/
sudo wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.focal_amd64.deb
sudo apt install gdebi
sudo gdebi --n wkhtmltox_0.12.5-1.focal_amd64.deb
sudo ln -s /usr/local/bin/wkhtmltopdf /usr/bin
sudo ln -s /usr/local/bin/wkhtmltoimage /usr/bin
```

##### Repositorios OCA:
`pwd: /odoo/oca`
- Clonar los repositorios necesarios para tu entorno. [Repositorios]('https://github.com/oca')
```sh
git clone git@github.com:OCA/<repositorio>.git --depth 1 --branch 14.0 --single-branch
```
- Si quieres clonar masivamente muchos módulos:
  - Crear lista de repositorios. Ejemplo: `oca_dependencies.txt`
```
account-analytic
account-closing
account-financial-reporting
...
```
  - Crear un script para ejecutar la clonación en bucle. Ejemplo: `install_oca_dependencies.sh`
```sh
#!/bin/bash
SAVEIFS=$IFS
IFS=$(echo -en "\n\b")
File="oca_dependencies.txt"
Lines=$(cat $File)
for Line in $Lines
  do git clone git@github.com:OCA/${Line:0:-1}.git --depth 1 --branch 14.0 --single-branch
done
# restore $IFS
IFS=$SAVEIFS
```
  - Ejecutar el script
```sh
bash install_oca_dependencies.sh
```
###### **_(Opcional)_** Actualizar repositorios y hacer merge de commits necesarios usando [git-aggregate]('https://github.com/acsone/git-aggregator')
- Crear un archivo `repos.yaml` o `repos.yml`. Ejemplo:
```yml
.../odoo/oca/account-analytic:
  defaults:
    depth: 100 # Aumentar a medida que aumentes merges. Por defecto es 1.
  merges:
  - oca 14.0 # Rama origen
  - oca refs/pull/495/head # PR que desean combinar
  remotes:
    oca: https://github.com/OCA/account-analytic.git # Url del repositorio
  target: oca 14.0 # Rama destino
```
- Actualizar y combinar PR's, `-d` para especificar un repositorio (_opcional_):
```sh
gitaggregate -c repos.yaml -d <module>
```

## Iniciar Entorno Local:
`pwd: /odoo/odoo`
```sh
#Iniciar base de datos
sudo service postgresql start
# Iniciar Odoo instalando `base`, solo la primera vez suele ser necesario para cargar el resto de los módulos
./odoo-bin -c ./debian/odoo.conf -i base
```
- Flags:
  - `-i`: Instalar módulo
  - `-u`: Actualizar módulo, puedes separarlo por comas
  - `-d`: Especificar base de datos


###### **_(Recomendado)_** Crear Alias:
Se recomienda crear alias globales, ya que se usarán los mismos comandos constantemente
- Configuración del archivo ``bashsrc``, ir a la última línea del archivo
```sh
# Postgres Aliases
alias postgres_start='sudo service postgresql start'
alias postgres_stop='sudo service postgresql stop'
alias postgres_restart='sudo service postgresql restart'
# Odoo Aliases
alias odoo_start='~/odoo/odoo/odoo-bin -c ~/odoo/odoo/debian/odoo.conf'
``` 
- Aplicar los cambios
```sh
source ~/.bashrc
```

