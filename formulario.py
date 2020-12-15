from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

class formBlog(FlaskForm):
    buscarBlog = StringField('BUSCAR UN BLOG')
    crearBlog = StringField('Crear un nuevo blog', render_kw= {"onmouseover":"listarEst()"})
    editarBlog = StringField('Editar blog', render_kw= {"onmouseover":"listarEst()"})
    eliminarBlog = StringField('Elimiar blog', render_kw= {"onmouseover":"listarEst()"})
    comentarBlog = StringField('Crear un nuevo blog', render_kw= {"onmouseover":"listarEst()"})

class formLogin(FlaskForm):
    email = StringField('Usuario', validators=[DataRequired(message='No dejar vacio, completar')], render_kw={"placeholder":"Digite el nombre de usuario"})
    password = PasswordField('Contraseña', validators=[DataRequired(message='No dejar vacio, completar')], render_kw={"placeholder":"Digite la contraseña"})
    enviar = SubmitField('Iniciar Sesion', render_kw= {"onmouseover":"guardarEst()"})
    recuperar = SubmitField('Recuperar Constraseña', render_kw= {"onmouseover":"guardarEst()"})

class formIndex(FlaskForm):
    registrarse = SubmitField('Registrarse')
    iniciarSesion = SubmitField('Iniciar Sesion', render_kw= {"onmouseover":"guardarEst()"})
    buscarBlog = SubmitField('Buscar Blog', render_kw= {"onmouseover":"guardarEst()"})
    
class formCrearBlog(FlaskForm):
    titulo = SubmitField('Título Blog')
    descripcion = SubmitField('Descripción')
    pulicoPrivado= SubmitField('Iniciar Sesion', choices=[( 'Publico' ),( 'Privado' )])
    crear = SubmitField('Crear', render_kw= {"onmouseover":"guardarEst()"})
    
class formNuevaContrasena(FlaskForm):
    contrasena = PasswordField('Contraseña', validators=[DataRequired(message='No dejar vacio, completar')], render_kw={"placeholder":"Digite la contraseña"})
    confirmContrasena = PasswordField('Repetir Contraseña', validators=[DataRequired(message='No dejar vacio, completar')], render_kw={"placeholder":"Digite la contraseña"})
    cambiar = SubmitField('Cambiar', render_kw= {"onmouseover":"guardarEst()"})
    
class recuperarContrasena(FlaskForm):
    email = StringField('Usuario', validators=[DataRequired(message='No dejar vacio, completar')], render_kw={"placeholder":"Digite el nombre de usuario"})
    recuperar = SubmitField('ENVIAR MAIL', render_kw= {"onmouseover":"guardarEst()"})
    
class formRegistro(FlaskForm):
    nombre = StringField('NOMBRE COMPLETO',  validators=[DataRequired(message='No dejar vacio, completar')], render_kw={"placeholder":"Digite su nombre completo"})
    apellido = StringField('APELLIDOS',  validators=[DataRequired(message='No dejar vacio, completar')], render_kw={"placeholder":"Digite sus apellidos"})
    email = StringField('CORREO ELECTRONICO',  validators=[DataRequired(message='No dejar vacio, completar')], render_kw={"placeholder":"Digite sus correo electrónico"})
    passw = PasswordField('CONTRASEÑA', validators=[DataRequired(message='No dejar vacio, completar')], render_kw={"placeholder":"Digite su contraseña"})
    passver = PasswordField('CONTRASEÑA', validators=[DataRequired(message='No dejar vacio, completar')], render_kw={"placeholder":"Repita su contraseña"})
    registrese = StringField('REGISTRESE', render_kw= {"onmouseover":"listarEst()"})
    