
public class RemoveNthFromEnd {
	public static void main(String[] args) {
		
	}
}

class Solution_RemoveNthFromEnd {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode del_node = head,pointer = head;
        for(int idx = 0;idx < n;idx++) {
        	pointer = pointer.next;//将pointer指向要删除的节点的后面第n个
        }
        if(pointer.next==null) {
        	head = head.next;
        	return head;
        }
        while(pointer.next!=null) {
        	pointer = pointer.next;
        	del_node = del_node.next;
        }
        del_node.next = del_node.next==null?null:del_node.next.next;
        return head;
    }
}


class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}