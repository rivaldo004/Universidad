public class Perro implements Animal {    // asi se implementa el interfas
    @Override
    public void hacerRuido() {
        System.out.println("Grrrrrrrrrrrr!");
    }

    @Override
    public void caminar() {
        System.out.println("El perro esta caminando");
    }

    @Override
    public String tipoAnimal() {
        return "";
    }

    @Override
    public String tipoAnimal(String tipo) {
        return "Es de tipo" + tipo;
    }
}