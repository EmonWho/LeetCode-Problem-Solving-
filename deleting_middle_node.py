class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        if head.next is None:
            return None
        x=head
        counter=0
        
        while x is not None and x.next is not None:
            x=x.next.next
            counter+=1
        x=head
        
        while counter > 1:
            x=x.next
            counter-=1
        x.next=x.next.next
        return head
