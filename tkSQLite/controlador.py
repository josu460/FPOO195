from tkinter import messagebox
import sqlite3
import bcrypt

class Controlador:
    
    def conexion(self):
        try:
            conex = sqlite3.connect("C:\\Users\\josuu\\OneDrive\\Documentos\\POO\\FPOO195\\tkSQLite\\db195.db")

            print("Conectado")
            return conex
        except sqlite3.OperationalError:
            print("No se pudo conectar")
            
    def encriptapass(self,cont):
        passPlana=cont
        passPlana= passPlana.encode()
        sal= bcrypt.gensalt()
        passHash= bcrypt.hashpw(passPlana, sal)
        
        return passHash
    
    def insertUsuario(self,nom,corr,cont):
        
        conexion= self.conexion()
        
        if( nom== "" or corr == "" or cont== ""):
            messagebox.showwarning("Cuidado","inputs vacios no sea tibio")
            conexion.close()
        else:
            cursor = conexion.cursor()
            conH= self.encriptapass(cont)
            datos=(nom,corr,conH)
            sqlInsert="INSERT INTO tbUsuarios(nombre, correo, contra) VALUES (?,?,?)"
            
            cursor.execute(sqlInsert,datos)
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Exito", "guardado con exito!!")
            
    def buscarUsuario(self,id):
        conex=self.conexion()
        
        if(id== ''):
            messagebox.showwarning("Cuidado","inputs vacios")
            conex.close()
        else:
            try:
                cursor = conex.cursor()
                sqlSelect="select * from tbUsuarios where id="+id
                cursor.execute(sqlSelect)
                usuario=cursor.fetchone()
                conex.close()
                return usuario
            except sqlite3.OperationalError:
                print("No se pudo ejecutar la busqueda")
    
    def consultarUsuarios(self):
        conex = self.conexion()
        try:
            cursor = conex.cursor()
            sqlSelect = "SELECT * FROM tbUsuarios"
            cursor.execute(sqlSelect)
            usuarios = cursor.fetchall()
            conex.close()
            return usuarios
        except sqlite3.OperationalError:
            print("No se pudo ejecutar la consulta de usuarios")