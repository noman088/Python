# 7. Write a python program to remove last item of the given set
# thisset = {"Python", "Django", "JavaScript", “SQL”}

this_set={"python",'Django',"Javascript","SQL"}
print("Before remove : ",this_set)
this_set.discard("SQL")
print("After remove : ",this_set)