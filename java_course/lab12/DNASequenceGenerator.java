package java_course.lab12;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class DNASequenceGenerator {

    private static final String[] DNA_NUCLEOTIDES = {"T", "C", "G", "A"};
    private static final int NUM_THREADS = 4;
    private static final int DEFAULT_SEQUENCE_LENGTH = 100;

    private final int sequenceLength;
    private final StringBuilder dnaSequence = new StringBuilder();
    private final Thread[] threads = new Thread[NUM_THREADS];

    public DNASequenceGenerator(int sequenceLength) {
        this.sequenceLength = sequenceLength;
    }

    public void generateSequence() throws InterruptedException {
        int iterationsPerThread = sequenceLength / NUM_THREADS;
        for (int i = 0; i < NUM_THREADS; i++) {
            int threadIterations = (i == NUM_THREADS - 1) ? sequenceLength - i * iterationsPerThread : iterationsPerThread;
            threads[i] = new Thread(new DNAGenerator(DNA_NUCLEOTIDES[i], threadIterations));
            threads[i].start();
        }
        for (int i = 0; i < NUM_THREADS; i++) {
            threads[i].join();
        }
    }

    public void writeToFile(String filePath) throws IOException {
        File file = new File(filePath);
        if (!file.exists()) {
            file.createNewFile();
        }
        FileWriter writer = new FileWriter(file);
        writer.write(dnaSequence.toString());
        writer.close();
    }

    private class DNAGenerator implements Runnable {

        private final String nucleotide;
        private final int numIterations;

        private DNAGenerator(String nucleotide, int numIterations) {
            this.nucleotide = nucleotide;
            this.numIterations = numIterations;
        }

        @Override
        public void run() {
            Random random = new Random();
            for (int i = 0; i < numIterations; i++) {
                dnaSequence.append(nucleotide);
                try {
                    Thread.sleep(random.nextInt(500)); // случайная задержка от 0 до 500 миллисекунд
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    public static void main(String[] args) {
        try {
            int sequenceLength = (args.length > 0) ? Integer.parseInt(args[0]) : DEFAULT_SEQUENCE_LENGTH;
            DNASequenceGenerator dnaGenerator = new DNASequenceGenerator(sequenceLength);
            dnaGenerator.generateSequence();
            dnaGenerator.writeToFile("dna_sequence.txt");
            System.out.println("DNA sequence successfully generated and written to file.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
}
