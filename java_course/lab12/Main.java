package java_course.lab12;

import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Thread t1 = new Thread(new DnaGenerator("T"));
        Thread t2 = new Thread(new DnaGenerator("C"));
        Thread t3 = new Thread(new DnaGenerator("G"));
        Thread t4 = new Thread(new DnaGenerator("A"));

        t1.start();
        t2.start();
        t3.start();
        t4.start();
    }

    public static class DnaGenerator implements Runnable {
        private String nucleotide;
        private Random random;

        public DnaGenerator(String nucleotide) {
            this.nucleotide = nucleotide;
            this.random = new Random();
        }

        public void run() {
            while (true) {
                int delay = random.nextInt(1000) + 500; // Генерируем случайную задержку от 500 до 1500 мс
                try {
                    Thread.sleep(delay);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.print(nucleotide);
            }
        }
    }
}
