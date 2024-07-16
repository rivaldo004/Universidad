public class Main {
    public static void main(String[] args) {
        // Crear objetos Producto
        Producto camisa = new Producto("CAM-123", "Camisa estampada");
        Producto pantalon = new Producto("PAN-456", "Pantalón jeans");

        // Imprimir información de los productos
        System.out.println("Camisas: verano, invierno");
        System.out.println(camisa.toString());
        System.out.println("Pantalón: Jeans negro");
        System.out.println(pantalon.toString());

        // Crear objetos Transporte

        Transporte terrestre = new Transporte("TRA-789", "Camión", "Transporte terrestre de mercancía", 120.00);
        Transporte aereo = new Transporte("AERO-012", "Avión", "Transporte aéreo de pasajeros", 350.00);


        // Crear objetos Ropa

        Ropa vestido = new Ropa("VES-345", "Vestido casual", "M", "Azul");
        Ropa jeans = new Ropa("JEA-678", "Jeans rotos", "32", "Negro");


        // Cambiar la talla del jeans a "34"
        jeans.setTalla("34");
        System.out.println("Talla actual del jeans: " + jeans.getTalla());
    }
}