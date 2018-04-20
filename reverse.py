
def reverse(s):
    """Write a function that takes a string as a parameter and returns a new
    string that is the reverse of the old string."""
    if len(s) == 1:
        return s
    return reverse(s[1:]) + s[0]

print reverse("beautiful")