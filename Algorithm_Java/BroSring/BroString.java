public class BroString {
	public static void main(String argc[]) {
		String A = "1";
		String B = "1";
		Solution_BroString sol = new Solution_BroString();
		if(sol.isBroString(A,B)) {
			System.out.println("Is bro string!");
		}
		else {
			System.out.println("Is not bro string!");
		}
	}
}

class Solution_BroString {
	public boolean isBroString(String A , String B) {
		if(A.length()==B.length()) {
			int idx = 0;
			int num=0;
			char s1='\0',s2='\0',s3='\0',s4='\0';
			while(idx<A.length()) {
				if(A.charAt(idx) != B.charAt(idx)) {
					num ++;
					if(num==1) {
						s1 = A.charAt(idx);s2 = B.charAt(idx);
					}
					else if(num==2) {
						s3 = A.charAt(idx);s4 = B.charAt(idx);
					}
					else {
						return false;
					}
					
				}
				idx++;
			}
			if(num==2&&s1==s4&&s2==s3) {
				return true;
			}
			else if(num == 0) {
				for(int i=0;i<A.length();i++) {
					for(int j=i+1;j<A.length();j++) {
						if(A.charAt(i)==A.charAt(j)) {
							return true;
						}
					}
				}
			}
		}
		return false;
	}
}
