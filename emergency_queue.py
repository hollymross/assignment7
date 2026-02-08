class Patient:
    def __init__(self, name, value):
        self.name = name
        self.value = value



class MinHeap:
    def __init__(self):
        self.data = []

    def print_heap(self):
        print("Current waitlist")
        for task in self.data:
            print(f"-{task.name} (Priority: {task.value})")
        
    def insert(self,task):
        self.data.append(task)
        self.heapify_up(len(self.data)-1)

    def heapify_up(self,index):
        while index > 0:
            parent_index = (index - 1) // 2

            current_task = self.data[index]
            parent_task = self.data[parent_index]

            if current_task.value < parent_task.value:
                temp = self.data[index]
                self.data[index] = self.data[parent_index]
                self.data[parent_index] = temp

                index = parent_index
            
            else:
                break

    def heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

    
        if left < len(self.data) and self.data[left].priority < self.data[smallest].priority:
            smallest = left

    
        if right < len(self.data) and self.data[right].priority < self.data[smallest].priority:
            smallest = right

    
        if smallest != index:
     
            temp = self.data[index]
            self.data[index] = self.data[smallest]
            self.data[smallest] = temp
      
      
        self.heapify_down(smallest)

    def remove_min(self):
        if not self.data: 
            return None

        if len(self.data) == 1: 
            return self.data.pop()

        min_value = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)
        return min_value            



# Test your MinHeap class here including edge cases

heap = MinHeap()
heap.insert(Patient("John", 3))
heap.insert(Patient("Mary", 1))
heap.insert(Patient("Jeff", 5))
heap.print_heap()

#First we made the patient class which takes in the patient name and their priority in the list. Then we made the MinHeap class which is where the order of the list is made. Based on
#the priority of the patient, it will place them in that order and keep everything in line. It does this by comparing the index value of the parent index to the new index and sees if 
#it is higher or lower in priority. If it has a higher priority, it will take that spot and mode everything in the list down, if it does not take the spot it will be placed lower than
#the parent index. This is tested with the patients John, Mary, and Jeff, where Mary has the highest priority, John has the second highest priority, and Jeff has the lowest priority. 
