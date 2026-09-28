# Dictionaries in Python

A dictionary in Python is a collection of key-value pairs. They are **mutable**, **ordered** (from Python 3.7 onwards), and do not allow duplicate keys.

## Creating and Accessing Dictionaries

Dictionaries are created using curly braces `{}` with `key: value` syntax. 

```python
songs_artist = {"Blinding Lights": "The Weeknd", "Mockingbird": "Eminem"}

# Accessing via Key (Throws KeyError if key doesn't exist)
print(songs_artist["Mockingbird"])  # Output: Eminem

# Accessing via .get() (Safe method, returns None if key is missing)
print(songs_artist.get("Fake Love"))  # Output: None

```

*Note: Slicing (like `dict[1:3]`) or multi-key access (like `dict["Key1", "Key2"]`) is not supported in dictionaries.*


## Adding, Updating, and Deleting

- **Adding/Updating**: Just assign a value to a key. If the key exists, it updates; if not, it adds a new pair.

- `.pop(key)`: Removes the specified key and returns its value.

- `.popitem()`: Removes and returns the last inserted key-value pair as a tuple.

- `del dict[key]`: Deletes the key-value pair.

- `.clear()`: Empties the entire dictionary.

*(Dictionaries do NOT have a `.remove()` method like lists.)*

## Iterating Through Dictionaries

By default, looping through a dictionary only accesses its keys. To get both keys and values, use `.items()`.

```python

# Looping through both Key and Value
for key, value in songs_artist.items():
    print(key, value)

```

## Nested Dictionaries

A dictionary can contain another dictionary as a value. Accessing elements requires chaining the square brackets `[][]`.

```python

tea_shop = {
    "chai": {"Masala": "Spicy", "Ginger": "Zesty"}
}
print(tea_shop["chai"]["Ginger"])  # Output: Zesty

```

## Advanced Dictionary Concepts

### Dictionary Comprehension

Similar to lists, you can generate dictionaries using a one-liner loop:

```python

squared_num = {x: x**2 for x in range(6)}
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

```

### `dict.fromkeys()`

Creates a new dictionary using elements from an iterable as keys, and sets them all to a default value.

```python

keys = ["Masala", "Ginger"]
new_dict = dict.fromkeys(keys, "Delicious")
# Output: {'Masala': 'Delicious', 'Ginger': 'Delicious'}

```
## Common Dictionary Errors

- **KeyError**: Occurs when you try to access or delete a key that does not exist using square brackets `[]`.

- **AttributeError**: Occurs when you try to use list methods like `.remove()` or `.append()` on a dictionary.

- **ValueError (Unpacking)**: If you write `for key, value, test in dict.items():`, Python throws an error because `.items()` only provides 2 values per iteration (the key and the value), but you asked for 3.

## Key Learning and Interview Points

- **Membership Operator (`in`)**: When you check `if "Eminem" in songs_artist:`, it only searches the Keys, not the values.

- **String Interning / Memory Optimization**: If two different keys have the exact same string value, Python optimizes memory by pointing them to the same object.
(Example: `songs_artist["Mockingbird"] is songs_artist["Rap God"]` evaluates to `True` if both equal "Eminem").

- **Speed**: Dictionaries in Python use Hash Tables under the hood, making key lookups incredibly fast (O(1) time complexity), regardless of how large the dictionary gets.