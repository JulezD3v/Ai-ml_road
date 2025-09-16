#Code that  explains about depth first search that uses the stsacka algoritthm (last in first out)
#Depth First Search
class Frontier:
    def __init__(self):
        # Initialize frontier as an empty list
        self.frontier = [34,89,890,9]

    def empty(self):
        # Check if frontier is empty
        return len(self.frontier) == 0

    def remove(self):
        """
        Removes and returns the last node/item in the frontier.
        If the frontier is empty, it raises an Exception.
        
        This uses list slicing (self.frontier[1:]) to drop the last element.
        """
        # Termination of the search if the frontier is empty
        if self.empty():
            raise Exception("empty frontier")
        else:
            # Get the first node/item in the list
            node = self.frontier[0]
            # Reassign frontier to a new list without the last element
            self.frontier = self.frontier[1:]
            return node 