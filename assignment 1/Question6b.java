// Vivek Patel
import java.math.BigInteger;
import java.util.*;

class Question6b {
  static  int a = 3;
  static  int b = 2;

  static Hashtable<Integer, Character> cN = new Hashtable<Integer, Character>();
  static Hashtable<Character, Integer> nC = new Hashtable<Character, Integer>();
  static{
    cN.put(0, 'A');
    cN.put(1, 'C');
    cN.put(2, 'G');
    cN.put(3, 'T');
    nC.put('A', 0);
    nC.put('C', 1);
    nC.put('G', 2);
    nC.put('T', 3);
  }

  public static void main(String[] args) {
    String sequence = "ACGT";
    String ciphertext = encrypt(sequence);
    String plaintext = decrypt(ciphertext);
    System.out.println("Sequence: " + sequence);
    System.out.println("Encrypted Ciphertext: " + ciphertext);
    System.out.println("Decrypted Plaintext: " + plaintext);
  }

  static String encrypt(String s){
    StringBuilder cipher = new StringBuilder();
    for (int j = 0; j < s.length(); j++){
      char c = s.charAt(j);
      int i = nC.get(c);
      int t = ((a * i) + b) % 4;
      c = cN.get(t);
      cipher.append(c);
    }
    return cipher.toString();
  }

  static String decrypt(String s){
    StringBuilder text = new StringBuilder();
    BigInteger inverseA = BigInteger.valueOf(a).modInverse(BigInteger.valueOf(4));
    for(int k = 0; k < s.length(); k++){
      char c = s.charAt(k);
      int i = nC.get(c); 
      int t = (inverseA.intValue() * (i - b + 4)) % 4;
      c = cN.get(t);
      text.append(c);
    }
    return text.toString();
  }
}