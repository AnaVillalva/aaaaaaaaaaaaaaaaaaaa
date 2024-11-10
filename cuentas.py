import tkinter as tk
from tkinter import messagebox
import random
import string

class Cuentas:
    def __init__(self):
        self.contrasenas = {}  # Diccionario para almacenar las contraseñas

    # 1.1 Agregar una nueva contraseña
    def agregar_contrasena(self):
        ventana = tk.Toplevel()
        ventana.title("Agregar Contraseña")
        ventana.geometry("300x200")

        tk.Label(ventana, text="Tipo de Cuenta:").pack(pady=5)
        tipo_entry = tk.Entry(ventana)
        tipo_entry.pack(pady=5)

        tk.Label(ventana, text="Nombre de Usuario o ID:").pack(pady=5)
        usuario_entry = tk.Entry(ventana)
        usuario_entry.pack(pady=5)

        tk.Label(ventana, text="Contraseña:").pack(pady=5)
        contrasena_entry = tk.Entry(ventana, show="*")
        contrasena_entry.pack(pady=5)

        def guardar_contrasena():
            tipo_cuenta = tipo_entry.get()
            usuario_cuenta = usuario_entry.get()
            contrasena_cuenta = contrasena_entry.get()

            if usuario_cuenta in self.contrasenas:
                messagebox.showerror("Error", "Esta cuenta ya existe.")
            else:
                self.contrasenas[usuario_cuenta] = {'tipo': tipo_cuenta, 'contraseña': contrasena_cuenta}
                messagebox.showinfo("Éxito", "Contraseña agregada correctamente.")
                ventana.destroy()

        tk.Button(ventana, text="Guardar", command=guardar_contrasena).pack(pady=10)

    # 1.2 Ver todas las contraseñas
    def ver_contrasenas(self):
        ventana = tk.Toplevel()
        ventana.title("Ver Contraseñas")
        ventana.geometry("400x400")

        tk.Label(ventana, text="¿Deseas ver todas las contraseñas o solo de un tipo específico?").pack(pady=10)
        
        def mostrar_todas():
            for usuario, datos in self.contrasenas.items():
                tk.Label(ventana, text=f"Cuenta: {usuario}").pack()
                tk.Label(ventana, text=f" - Tipo: {datos['tipo']}").pack()
                tk.Label(ventana, text=f" - Contraseña: {datos['contraseña']}").pack()
                tk.Label(ventana, text="").pack()

        tk.Button(ventana, text="Ver todas", command=mostrar_todas).pack(pady=5)

        tk.Label(ventana, text="Filtrar por tipo de cuenta (ej: email, social):").pack(pady=5)
        tipo_entry = tk.Entry(ventana)
        tipo_entry.pack(pady=5)

        def mostrar_filtradas():
            tipo_filtro = tipo_entry.get()
            for usuario, datos in self.contrasenas.items():
                if datos['tipo'] == tipo_filtro:
                    tk.Label(ventana, text=f"Cuenta: {usuario}").pack()
                    tk.Label(ventana, text=f" - Contraseña: {datos['contraseña']}").pack()
                    tk.Label(ventana, text="").pack()
        
        tk.Button(ventana, text="Filtrar", command=mostrar_filtradas).pack(pady=5)

    # 1.3 Buscar una contraseña
    def buscar_contrasena(self):
        ventana = tk.Toplevel()
        ventana.title("Buscar Contraseña")
        ventana.geometry("300x200")

        tk.Label(ventana, text="Ingrese el nombre de la cuenta que desea buscar:").pack(pady=10)
        usuario_entry = tk.Entry(ventana)
        usuario_entry.pack(pady=5)

        def realizar_busqueda():
            usuario_cuenta = usuario_entry.get()
            if usuario_cuenta in self.contrasenas:
                datos = self.contrasenas[usuario_cuenta]
                resultado = f"Cuenta: {usuario_cuenta}\nTipo: {datos['tipo']}\nContraseña: {datos['contraseña']}"
                messagebox.showinfo("Resultado de la Búsqueda", resultado)
            else:
                messagebox.showerror("Error", "Cuenta no encontrada.")
            ventana.destroy()

        tk.Button(ventana, text="Buscar", command=realizar_busqueda).pack(pady=10)

    # 1.4 Actualizar una contraseña
    def actualizar_contrasena(self):
        ventana = tk.Toplevel()
        ventana.title("Actualizar Contraseña")
        ventana.geometry("300x250")

        tk.Label(ventana, text="Ingrese el nombre de la cuenta a actualizar:").pack(pady=5)
        usuario_entry = tk.Entry(ventana)
        usuario_entry.pack(pady=5)

        tk.Label(ventana, text="Ingrese la nueva contraseña:").pack(pady=5)
        nueva_contrasena_entry = tk.Entry(ventana, show="*")
        nueva_contrasena_entry.pack(pady=5)

        tk.Label(ventana, text="Confirme la nueva contraseña:").pack(pady=5)
        confirmacion_entry = tk.Entry(ventana, show="*")
        confirmacion_entry.pack(pady=5)

        def actualizar():
            usuario_cuenta = usuario_entry.get()
            nueva_contrasena = nueva_contrasena_entry.get()
            confirmacion = confirmacion_entry.get()

            if usuario_cuenta in self.contrasenas:
                if nueva_contrasena == confirmacion:
                    self.contrasenas[usuario_cuenta]['contraseña'] = nueva_contrasena
                    messagebox.showinfo("Éxito", "Contraseña actualizada correctamente.")
                    ventana.destroy()
                else:
                    messagebox.showerror("Error", "Las contraseñas no coinciden.")
            else:
                messagebox.showerror("Error", "Cuenta no encontrada.")

        tk.Button(ventana, text="Actualizar", command=actualizar).pack(pady=10)

    # 1.5 Eliminar una cuenta
    def eliminar_contrasena(self):
        ventana = tk.Toplevel()
        ventana.title("Eliminar Contraseña")
        ventana.geometry("300x200")

        tk.Label(ventana, text="Ingrese el nombre de la cuenta que desea eliminar:").pack(pady=10)
        usuario_entry = tk.Entry(ventana)
        usuario_entry.pack(pady=5)

        def realizar_eliminacion():
            usuario_cuenta = usuario_entry.get()
            if usuario_cuenta in self.contrasenas:
                confirmacion = messagebox.askyesno("Confirmación", f"¿Está seguro de que desea eliminar la contraseña para {usuario_cuenta}?")
                if confirmacion:
                    del self.contrasenas[usuario_cuenta]
                    messagebox.showinfo("Éxito", f"Contraseña para {usuario_cuenta} eliminada.")
                    ventana.destroy()
                else:
                    messagebox.showinfo("Cancelado", "Acción cancelada.")
            else:
                messagebox.showerror("Error", "Cuenta no encontrada.")

        tk.Button(ventana, text="Eliminar", command=realizar_eliminacion).pack(pady=10)
    
    #metodo para generar una contraseña segura
    # cuentas.py


    # Método para generar una contraseña segura
    def generar_contrasena(self, longitud=12):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        # Generar la contraseña aleatoria
        contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
        return contrasena

    # Función para abrir la ventana de generación de contraseñas
    def ventana_generar_contrasena(self):
        ventana = tk.Toplevel()
        ventana.title("Generar Contraseña Segura")
        ventana.geometry("300x200")

        # Entrada para la longitud de la contraseña
        tk.Label(ventana, text="Longitud de la contraseña:").pack(pady=5)
        longitud_entry = tk.Entry(ventana)
        longitud_entry.insert(0, "12")  # Longitud predeterminada
        longitud_entry.pack(pady=5)

        # Área para mostrar la contraseña generada
        resultado_label = tk.Label(ventana, text="", wraplength=280, justify="center")
        resultado_label.pack(pady=10)

        # Función para generar la contraseña y mostrarla
        def generar():
            try:
                longitud = int(longitud_entry.get())
                if longitud < 6:
                    messagebox.showwarning("Advertencia", "Se recomienda una longitud de al menos 6 caracteres para seguridad.")
                contrasena = self.generar_contrasena(longitud)
                resultado_label.config(text=f"Contraseña Generada:\n{contrasena}")

                # Hacer que la contraseña esté disponible para copiar
                ventana.clipboard_clear()
                ventana.clipboard_append(contrasena)
                messagebox.showinfo("Copiada al portapapeles", "La contraseña ha sido copiada al portapapeles.")
            except ValueError:
                messagebox.showerror("Error", "Ingrese un número válido para la longitud.")

        # Botón para generar y copiar la contraseña
        tk.Button(ventana, text="Generar y Copiar Contraseña", command=generar).pack(pady=20)
