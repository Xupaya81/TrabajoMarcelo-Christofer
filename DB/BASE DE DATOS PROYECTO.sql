CREATE TABLE TipoUsuario (
    IdTipoUsuario TINYINT NOT NULL AUTO_INCREMENT,
    TipoUsuario VARCHAR(50) NOT NULL,
    PRIMARY KEY (IdTipoUsuario) 
);

CREATE TABLE Empleados (
    IdEmpleado TINYINT NOT NULL AUTO_INCREMENT,
    Nombre VARCHAR(50),
    ApellidoPaterno VARCHAR(50),
    ApellidoMaterno VARCHAR(50),
    FechaContrato DATETIME NOT NULL,
    FechaNacimiento DATETIME NOT NULL,
    Salario VARCHAR(15),
    Correo VARCHAR(255) NOT NULL,
    Telefono VARCHAR(15),
    Direccion VARCHAR(50) NOT NULL,
    IdDepartamento INT, 
    IdTipoUsuario TINYINT,
    Rut VARCHAR(10) NOT NULL,
    PRIMARY KEY (IdEmpleado),
    CONSTRAINT fk_IdTipo FOREIGN KEY (IdTipo) REFERENCES TipoUsuario(IdTipoUsuario),
    CONSTRAINT fk_IdDepartamento FOREIGN KEY (IdDepartamento) REFERENCES Departamento(IdDepartamento) 
);

CREATE TABLE Departamento (
    IdDepartamento TINYINT NOT NULL AUTO_INCREMENT,
    Nombre VARCHAR(100) NOT NULL,
    PRIMARY KEY (IdDepartamento)
);

CREATE TABLE Proyecto (
    IdProyecto TINYINT NOT NULL AUTO_INCREMENT,
    Nombre VARCHAR(50) NOT NULL,
    Descripcion VARCHAR(255) NOT NULL,
    FechaInicio DATE NOT NULL,
    FechaEntrega DATE NOT NULL,
    PRIMARY KEY (IdProyecto)
);
CREATE TABLE ProyectoEmpleado (
    IdProyectoEmpleado TINYINT NOT NULL AUTO_INCREMENT,
    IdEmpleado TINYINT NOT NULL,
    IdProyecto TINYINT NOT NULL,
    PRIMARY KEY (IdProyectoEmpleado),
    CONSTRAINT fk_EmpleadoProyectoEmpleado FOREIGN KEY (IdEmpleado) REFERENCES Empleados(IdEmpleado),
    CONSTRAINT fk_ProyectoProyectoEmpleado FOREIGN KEY (IdProyecto) REFERENCES Proyecto(IdProyecto)
);

CREATE TABLE RegistroTiempo (
    IdRegistroTiempo TINYINT NOT NULL AUTO_INCREMENT,
    Fecha DATE NOT NULL,
    IdEmpleado TINYINT NOT NULL,
    CantidadHoras TINYINT NOT NULL,
    PRIMARY KEY (IdRegistroTiempo)
    CONSTRAINT fk_EmpleadoRegistroTiempo FOREIGN KEY (IdEmpleado) REFERENCES Empleados(IdEmpleado)
);
CREATE TABLE Asignacion (
    IdAsignacion TINYINT NOt NULL,
    IdDepartamento TINYINT NOT NULL,
    IdEmpleado TINYINT NOT NULL,
    CONSTRAINT fk_EmpleadoAsignacion FOREIGN KEY (IdEmpleado) REFERENCES Empleados(IdEmpleado)
    CONSTRAINT fk_DepartamentoAsignacion FOREIGN KEY (IdDepartamento) REFERENCES Departamento(IdDepartamento)
);
