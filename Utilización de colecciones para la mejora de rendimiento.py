class Libro:
    def __init__(self, titulo, autor, categoria, ISBN):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.ISBN = ISBN

    def __repr__(self):
        return f"Libro(titulo='{self.titulo}', autor='{self.autor}', categoria='{self.categoria}', ISBN='{self.ISBN}')"


class Usuario:
    def __init__(self, nombre, ID_usuario):
        self.nombre = nombre
        self.ID_usuario = ID_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        self.libros_prestados.remove(libro)

    def listar_libros_prestados(self):
        return self.libros_prestados

    def __repr__(self):
        return f"Usuario(nombre='{self.nombre}', ID_usuario='{self.ID_usuario}')"


class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = set()
        self.usuarios_registrados = {}

    def añadir_libro(self, libro):
        self.libros[libro.ISBN] = libro

    def quitar_libro(self, ISBN):
        if ISBN in self.libros:
            del self.libros[ISBN]

    def registrar_usuario(self, usuario):
        if usuario.ID_usuario not in self.usuarios:
            self.usuarios.add(usuario.ID_usuario)
            self.usuarios_registrados[usuario.ID_usuario] = usuario

    def dar_baja_usuario(self, ID_usuario):
        if ID_usuario in self.usuarios:
            self.usuarios.remove(ID_usuario)
            del self.usuarios_registrados[ID_usuario]

    def prestar_libro(self, ISBN, ID_usuario):
        if ISBN in self.libros and ID_usuario in self.usuarios_registrados:
            libro = self.libros[ISBN]
            usuario = self.usuarios_registrados[ID_usuario]
            usuario.prestar_libro(libro)
            self.quitar_libro(ISBN)

    def devolver_libro(self, ISBN, ID_usuario):
        if ISBN not in self.libros and ID_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados[ID_usuario]
            libro = next((l for l in usuario.listar_libros_prestados() if l.ISBN == ISBN), None)
            if libro:
                usuario.devolver_libro(libro)
                self.añadir_libro(libro)

    def buscar_libro(self, titulo=None, autor=None, categoria=None):
        resultados = []
        for libro in self.libros.values():
            if (titulo and libro.titulo != titulo) or \
               (autor and libro.autor != autor) or \
               (categoria and libro.categoria != categoria):
                continue
            resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, ID_usuario):
        if ID_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados[ID_usuario]
            return usuario.listar_libros_prestados()
        return []

    def __repr__(self):
        return f"Biblioteca(libros={self.libros}, usuarios={self.usuarios}, usuarios_registrados={self.usuarios_registrados})"
