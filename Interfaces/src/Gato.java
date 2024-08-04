public class Gato implements Animal {

    @Override
    public void hacerRuido() {
        System.out.println("Miau");
    }

    @Override
    public void caminar() {
        System.out.println("El gato esta caminando");
    }

    @Override
    public String tipoAnimal() {
        return "";
    }

    @Override
    public String tipoAnimal(String tipo) {
        return "El tipo de Gato es: " + tipo;
    }
}