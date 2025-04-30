import java.util.Random;

public class Benchmarking {
    private  MetodosOrdenamiento  mOrdenamiento;

    public Benchmarking(){
        long currentTime = System.currentTimeMillis();
        long currentNano = System.nanoTime();
        System.out.println(currentTime);
        System.out.println(currentNano);
        mOrdenamiento = new MetodosOrdenamiento();
        int [] arreglo = generarArregloAlelatorio(1000000);
        Runnable tarea = () -> mOrdenamiento.burbujaTradicional(arreglo);
        mOrdenamiento.burbujaTradicional(arreglo);
        double tiempoDuracion = medirConCurrentTimeMiles(tarea);     
        double tiempoDuracionNano = medirConCurrentNano(tarea);  
        System.out.println("Tiempo de ejecución con currentTimeMillis: " + tiempoDuracion + " segundos");
        System.out.println("Tiempo de ejecución con currentNano: " + tiempoDuracionNano + " segundos");
    }

private int [] generarArregloAlelatorio(int tamanio){
   //0 al 99.999
    int [] arreglo = new int[tamanio];
    Random random= new Random();
    for (int i = 0; i < tamanio; i++){
        arreglo[i] = random.nextInt(10000000);
    }

    return arreglo;  
}
public double medirConCurrentTimeMiles(Runnable tarea){
    long inicio = System.currentTimeMillis();
    tarea.run();
    long fin = System.currentTimeMillis();
    double tiempoSegundos = (fin - inicio) / 1000.0;
    return tiempoSegundos;  
}
public double medirConCurrentNano(Runnable tarea){
    long inicio = System.nanoTime();
    tarea.run();
    long fin = System.nanoTime();
   return(fin - inicio) / 1000000.0;
     
}
}
