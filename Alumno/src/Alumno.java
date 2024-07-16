public class Alumno extends usuario {
    private String curso;

    // Constructor con nombre correcto
    public Alumno(String nombre, String apellido, String curso) {
        super(nombre, apellido);
        this.curso = curso;
    }

    // se debe implementar según las necesidades)
    public void obtenerNotas() {
        // Implementar la lógica para obtener las notas del alumno
    }

    public double calcularPromedio() {
        // Implementar la lógica para calcular el promedio de las notas
        return 0; // Valor temporal para probar el código
    }

    // Método aprobarReprobar() implementado
    public Boolean aprobarReprobar() {
        double promedio = calcularPromedio();
        double notaMinima = 7.0; // Ajustar la nota mínima según criterio
        return promedio >= notaMinima;
    }

    // Método getter y setter para el curso
    public String getCurso() {
        return curso;
    }

    public void setCurso(String curso) {
        this.curso = curso;
    }

    // Método adicional
    public void inscribirMateria(String materia) {
        String nombre = "Francisco";
        String apellido = "Rivera";
        System.out.println("El alumno " + nombre + " " + apellido + " ha sido inscrito en la materia " + materia);
    }
}