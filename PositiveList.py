class NonPositiveError(Exception):
    pass
class PositiveList(list):
    def append(self, x):
        if x>0:
            super(PositiveList, self).append(x)
        else:
            raise NonPositiveError("Не больше нуля.")
d=PositiveList()
d.append(10)
d.append(12)
d.append(1)
print(d)
d.append(0)
d.append(-1)
print(d)