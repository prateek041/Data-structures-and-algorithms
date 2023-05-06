# Different ways of converting string to a character array and pros and cons of using them.

There are four ways of converting a string to character array. They all have time complexity o(n) and space complexity O(n).

- toCharArray(): This is suitable for small to medium size strings.
- StringBuilder object: More efficient for large size strings.
- charAt(): This is manual looping technique.
- String constructor: Converting a character array to string.
- StringBuilder class: same use case as string constructor.
- Converting a string to character array is more efficient that using string.charAt since a new object is created for every character fetched using string.charAt().