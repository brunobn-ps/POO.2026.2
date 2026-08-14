import java.util.Scanner;

public class ex1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        System.out.print("Digite o seu nome: ")
        String name = entrada.nextline();

        System.out.printIn("Olá, " + name + "!");
        
        entrada.close()
    }
}


// para compilar: javac ex1.java