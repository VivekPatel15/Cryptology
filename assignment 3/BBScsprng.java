//Vivek Patel
package assignment3;

import java.util.*;
import java.math.*;

class BBScsprng {

	public static void main(String[] args) {
		BigInteger p = new BigInteger("24672462467892469787");
		BigInteger q = new BigInteger("396736894567834589803");
		BigInteger n = p.multiply(q);
		BigInteger x = new BigInteger("873245647888478349013");
		
		@SuppressWarnings("resource")
		Scanner scanner = new Scanner(System.in);
		System.out.println("Input Binary sequence: ");
		String ptext = scanner.nextLine();
		System.out.println("Now encrypting entered sequence: " + ptext);
		
		//String ptext = "0101 0011 0100 0101 0100 0011 0101 0101 0101 0010 0100 0101";
		String plainText = ptext.replaceAll("\\s+", "");
		
		int size = plainText.length();
    	
		List<BigInteger> keys = new ArrayList<>();
    	
		for (int i = 0; i < size; i++){
    		BigInteger b = x.pow(2).mod(n);
    		//System.out.println("x" + i + ": " + b);
    		keys.add(b);
    		x = b;
    	}
		
		StringBuilder bits = new StringBuilder();
		StringBuilder cipherText = new StringBuilder();
		
		for (int j = 0; j < keys.size(); j++) {
			if (keys.get(j).mod(new BigInteger("2")).equals(BigInteger.ZERO)){
				bits.append("0");
			} else {
				bits.append("1");
			}
		}
		
		String cipherKey = bits.toString();
		int keySize = cipherKey.length();
		
		for (int k = 0; k < keySize; k++) {
			cipherText.append(cipherKey.charAt(k) ^ plainText.charAt(k));
		}
		
		System.out.print("The Cipher is: ");
		for (int m = 0; m < cipherText.toString().length(); m++) {
			if (m % 4 == 0 && m != 0) {
				System.out.print(" ");
			}System.out.print(cipherText.toString().charAt(m));
				
		}
		
	}
}