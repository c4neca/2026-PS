public class CalculaMedia {
    static double media(int[] numeros) {
        if (numeros.length == 0) return 0;
        int total = 0;
        for (int n : numeros) {
            total += n;
        }
        return (double) total / numeros.length;
    }
    public static void main(String[] args) {
        int[] valores = {10, 20, 30};
        System.out.println(media(valores)); 
    }
}