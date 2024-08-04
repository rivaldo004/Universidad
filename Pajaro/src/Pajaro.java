public class Pajaro extends Animal implements Volador{
    private String nombre;

    // Const
    public Pajaro(String nombre) {
        this.nombre = nombre;
    }
    public String cantar(String tipo) {
        return "El pajaro" + nombre + "Canta" + tipo;
    }

    @Override
    public void volar() {
        System.out.println("El pajaro vuela");
    }
}