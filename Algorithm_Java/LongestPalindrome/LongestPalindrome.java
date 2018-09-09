
public class LongestPalindrome {
	public static void main(String[] args) {
		String s = "2222";
		Solution_LongestPalindrome sol = new Solution_LongestPalindrome();
		System.out.println(sol.longestPalindrome(s));
	}
}

class Solution_LongestPalindrome {
    public String longestPalindrome(String s) {
    	int length=0,start=0,end=0;
        for(int mid=0;mid<s.length();mid++) {
        	int i=mid-1,j=mid+1;
            for(;i>=0&&j<s.length();i--,j++) {
            	if(s.charAt(i)!=s.charAt(j)) {
            		break;//不对称
            	}
            }
            if(length<j-i-1){
            	length = j-i-1;
            	start = i+1;end = j-1;
            }
        }

        for(int left=0;left<s.length()-1;left++) {
        	int i=left,j=left+1;
        	for(;i>=0&&j<s.length();i--,j++) {
        		if(s.charAt(i)!=s.charAt(j)) {
            		break;//不对称
            	}       		
        	}
            if(length<j-i-1){
            	length = j-i-1;
            	start = i+1;end = j-1;
            }
        }

        if(length!=0)
        	return s.substring(start, end+1);
        else
        	return "";
    }
}