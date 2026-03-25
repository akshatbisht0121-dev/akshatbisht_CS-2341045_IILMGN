class solution:
    def reversebetween(
        self, head: Optional [ListNode], left: int, right: int
        ) -> Optional[ListNode]:
            if head.next == None or left == right:
                return head
            count = 1
            p1start= p2 start = p3start = p1End = p2End = None
            p1Start = head
            while temp:
                if count ==(left- 1):
                    p1End = temp
                    p2Start = temp.next
                    temp= temp.next
                    p1End.next = None
                elif (count == right):
                    p2End = temp
                    p3Start = temp.next
                    temp = temp.next
                    p2End.next = None
                    break
                else:
                    temp= temp.next
                count += 1
            if left == 1:
                p2Start = head
           
             start = end = None
            while p2Start:
                temp = p2Start
                p2Start = p2Start.next
                temp.next = None    
            
                if end  == None:
                      start = end = temp
                      p2End.next = None
                else:
                    temp.next = start
                    start = temp
            if p1End:
                 p1End.next = start  
            else:
                head = start
            end.next = p3Start
            return head            
                 
                       