class demo:
    def add(self,*numbers):
        print(sum(numbers))


obj=demo()
obj.add(8.9,9,0)
obj.add(10)
obj.add(10,20)