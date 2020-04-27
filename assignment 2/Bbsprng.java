import java.math.BigInteger;

class Bbsprng {

  public static void main(String[] args) {
    BigInteger p = new BigInteger("24672462467892469787");
    BigInteger q = new BigInteger("396736894567834589803");
    BigInteger n = p.multiply(q);

    int size = 9;
    BigInteger x = new BigInteger("873245647888478349013");

    for (int i = 0; i < size; i++){
    	BigInteger b = x.pow(2).mod(n);
    	System.out.println("x" + i + ": " + b);
    	x = b;
    }
  }
}