public class Main {

    public static void main(String[] args) {

        // class Profesor
        Profesor profesor1 = new Profesor("María", "Gómez", "Matemáticas");
        profesor1.mostrarInformacion();
        profesor1.asignarMateria("Cálculo");

        // Creación de objetos Alumno
        Alumno alumno1 = new Alumno("Pedro", "López", "Octavo");
        alumno1.mostrarInformacion();
        alumno1.inscribirMateria("Física");
    }
}