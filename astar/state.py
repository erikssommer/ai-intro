class State:
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
    
    def __equals__(self, next) -> bool:
        return self.x == next.x and self.y == next.y
    
    def __not_equals__(self, next) -> bool:
        return not self.__equals__(next)
        
    