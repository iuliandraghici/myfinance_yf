list1 = ["a", "b", "c"]
list2 = ["c", "a", "b"]

print(list1[0], list2[0])
print(list1 == list2)

list1.append(["d", "e"])  # we add the list ['d', 'e'] to the end of list1, on index 3
print(list1)
print(list1[3])

d = {"a": 0, "b": 0, "c": 0}
print(len(d))

d2 = {"a": 1, "b": 2, "c": 4, "d": 8}
print(d2.items())  # will return the list of items grouped in tuples (key, value)
print(d2.values())  # will return the list of values [1, 2, 4, 8]
print(d2.keys())

#  <this is what we add> for ... if <condition>
# for -> if -> left part
new_list = ["a" for x in ["1", "2", "3", "a", "b"] if not x.isnumeric()]
# for x in ["1", "2", "3", "a", "b"]
#     if ...
#         new_list.append("a")
print(new_list)

a = ["foo", "bar", "baz", "qux", "quux", "corge"]
print(a[4:2])
