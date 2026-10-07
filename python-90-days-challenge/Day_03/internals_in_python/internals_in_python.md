# Mutable

Mutable objects are those whose state or content can be changed after they are created. In Python, examples of mutable objects include lists, dictionaries, and sets. You can modify these objects by adding, removing, or changing elements without creating a new object.

# Immutable

Immutable objects, on the other hand, cannot be changed once they are created. Examples of immutable objects in Python include strings, tuples, and frozensets. If you want to modify an immutable object, you must create a new object with the desired changes.

# Garbage Collection

Garbage collection is a form of automatic memory management in Python. The Python memory manager automatically allocates and deallocates memory for objects. When an object is no longer needed, the garbage collector frees up the memory occupied by that object, preventing memory leaks and optimizing resource usage.

- Garbage collector - A component of the Python interpreter that automatically identifies and removes unused objects from memory.

- Reference counting - A technique used by the garbage collector to keep track of how many references point to an object. When the reference count drops to zero, the object is eligible for garbage collection.

- Circular references - A situation where two or more objects reference each other, creating a cycle that prevents the reference count from reaching zero. The garbage collector can detect and break these cycles to free up memory.




We tested the immutable objects in day 1. Now we will test the mutable objects in this day.