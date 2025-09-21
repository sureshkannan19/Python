from collections import OrderedDict

od = OrderedDict()
od['apple'] = 50
od['banana'] = 50
od['grapes'] = 50
od['carrot'] = 50
od['beetroot'] = 30

print(od)
print(od.popitem()) # removes last inserted
od.move_to_end("apple")
print(od)
od.move_to_end("carrot", last=False) # moves given key to beginning
print(od)
