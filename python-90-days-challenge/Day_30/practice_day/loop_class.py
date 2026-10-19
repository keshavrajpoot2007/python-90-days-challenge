class Loop:
    
    def print_times(self, value, times):
        for i in range(times):
            print(value)
            
            
my_loop = Loop()
print(my_loop.print_times("hi", 10))