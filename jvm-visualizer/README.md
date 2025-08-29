Java code being represented:

// Main.java
public class Main {
    public static int factorial(int n) {
        if (n <= 1) return 1;
        return n * factorial(n - 1);
    }

    public static void main(String[] args) {
        int result = factorial(4); // ← ldc 4, invokestatic factorial, istore_1
        Hello h = new Hello();     // ← new Hello, invokespecial <init>, astore_2
        // no printing; we just compute and allocate to mirror the visualizer
    }
}

// Hello.java
public class Hello {
    public Hello() { /* default ctor */ }
}
