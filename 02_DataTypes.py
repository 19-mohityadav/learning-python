# 🧠 What are Data Types?
#   A data type tells Python what kind of value a variable holds and what operations are allowed.
#   Python decides the type automatically (dynamic typing).

# 1️⃣ Numeric Data Types
# ➤ int (Integer) --> Whole numbers (no decimal)
#    ✔ Unlimited size
#    ✔ Used for counting, indexing

# ➤ float --> Decimal numbers (⚠️ Precision issue:)
print(0.1 + 0.2)   # 0.30000000000000004

# ➤ complex --> Numbers with imaginary part (Used in scientific/math apps)
z = 3 + 4j
print(z.real)   # 3.0
print(z.imag)   # 4.0

# 2️⃣ Text Data Type
# ➤ str (String) --> Text inside quotes
#                     Strings are immutable (cannot change characters)

# 3️⃣ Boolean
# ➤ bool --> Only two values(True or False)
print(10 > 5)   # True
print(3 == 7)   # False

# 4️⃣ Sequence Data Types
# ➤ list (Mutable) --> Ordered, changeable
# ➤ tuple (Immutable) --> Ordered, but cannot change
# ➤ range --> Sequence of numbers

# 5️⃣ Set Data Types
# ➤ set --> Unordered, unique elements
# ➤ frozenset --> Immutable version of set

# 6️⃣ Mapping Data Type
# ➤ dict (Dictionary) --> Key–value pairs

# 7️⃣ None Type
# ➤ None --> Means “nothing” or “empty” (Used when value is not yet assigned.)
result = None



# 🧩 Summary

# | Category | Types               |
# | -------- | ------------------- |
# | Numeric  | int, float, complex |
# | Text     | str                 |
# | Boolean  | bool                |
# | Sequence | list, tuple, range  |
# | Set      | set, frozenset      |
# | Mapping  | dict                |
# | Special  | None                |
