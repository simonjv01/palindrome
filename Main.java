public class Main {
    public static void main(String[] args) {
        String str = "madam";
        System.out.println(checkIfPalindrome(str));
    }

    public static boolean checkIfPalindrome(String str) {
        int n = str.length();
        for (int i = 0; i < n / 2; i++) {
            if (str.charAt(i) != str.charAt(n - i - 1)) {
                return false;
            }
        }
        return true;
    }
}
