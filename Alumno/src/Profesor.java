public class Profesor extends usuario {

    private String especialidad;

    // Constructor
    public Profesor(String nombre, String apellido, String especialidad) {
        super(nombre, apellido);
        this.especialidad = especialidad;
    }

    public void contarFaltas() {
        // Implementar la lógica para contar las faltas del profesor
    }

    public void mostrarInformacion() {
        super.mostrarInformacion(); // Llama al método de la clase padre
        System.out.println("Especialidad: " + especialidad);
    }

    // Métodos getter y setter
    public String getEspecialidad() {
        return especialidad;
    }

    public void setEspecialidad(String especialidad) {
        this.especialidad = especialidad;
    }

    // Método adicional
    public void asignarMateria(String materia) {
        String nombre = "Juan";
        String apellido = "Tobar";
        System.out.println("El profesor " + nombre + " " + apellido + " ha sido asignado a la materia " + materia);
    }
}
