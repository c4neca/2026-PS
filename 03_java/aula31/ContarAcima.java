public class ContarAcima {
    public static int contarAcima(int[] valores, int limite) {
        int quantidade = 0;
        for (int v : valores) {
            if (v > limite) {
                quantidade++;
            }
        }
        return quantidade;
    }
}