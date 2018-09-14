
public class MaxArea {
	public static void main(String args[]) {
		long time = System.currentTimeMillis();
		int[] height = {1,8,6,2,5,4,8,3,7};
		Solution_MaxArea sol = new Solution_MaxArea();
		System.out.println("Max area is "+sol.maxArea(height));
		time = System.currentTimeMillis() - time;
		System.out.println("Run Time:"+time+"ms");
	}
}

class Solution_MaxArea {
    public int maxArea(int[] height) {//假设height元素个数大于等于2
    	int area=0,lower,area_temp;
        for(int idx1=0;idx1<height.length-1;idx1++) {
        	for(int idx2 = idx1+1;idx2<height.length;idx2++) {
        		lower = height[idx1]>height[idx2]?height[idx2]:height[idx1];//选一个低的
        		area_temp = lower*(idx2-idx1);
        		area = area_temp>area?area_temp:area;
        	}
        }
        return area;
    }
}