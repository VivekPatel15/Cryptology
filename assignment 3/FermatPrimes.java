//Vivek Patel
package assignment3;

import java.util.*;

public class FermatPrimes {
	
	static int loops = 0;
	
	public static long gcd(long a, long b) {
		if (b == 0) {
			return a;
		} else if (a == 0) {
			return b;
		} else {
			return gcd(b, a % b);
		}
	}
	
	public static long modPower(long a, long b, long m) {
		if (b == 0) {
			return 1;
		} 
		
		long p = modPower(a, b/2, m) % m;
		p = (p * p) % m;
		
		return (b % 2 == 0) ? p : (a * p) % m;
	}
	
	public static long modSquared(long a, long m) {
		return a * a % m;
	}
	
	public static boolean primeCheck(long n) {
		for (int i = 0; i <= 20; i++) {
			long x = Math.round(Math.floor(Math.random() * (n - 2) + 2.0));
			if (modPower(x, n - 1, n) != 1) {
				return false;
			}
		}
		return true;
	}
	
	public static void test(long n) {
		loops++;
		if (primeCheck(n)) {
			System.out.println("Prime number detected: " + n);
			System.out.println("Loops completed: " + loops);
			System.exit(1);
		} else if (loops == 17) {
			System.out.println("Unable to find a prime number in 16 loops.");
			System.exit(1);
		}
		
	}
	public static void generateRandom(){
		Random r = new Random();
		long low = new Double(Math.pow(2, 24)).longValue();
		long high = new Double(Math.pow(2, 25)).longValue();
		r.longs(low, high).forEach(n -> test(n));;
	}
	
	public static void main(String[] args){
        generateRandom();
    }

}
