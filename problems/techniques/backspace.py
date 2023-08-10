from collections import deque

def transform_str(s: str) -> str:
    count = 0
    in_backspace = False
    final_str = deque()

    for i in range(len(s)-1, -1, -1):
        if not in_backspace and s[i] == "#" :
            in_backspace = True
        if in_backspace and s[i] == "#":
            count +=1
        if s[i] != "#" and count > 0:
            count -=1
            continue
        if s[i] != "#":
            final_str.appendleft(s[i])
    return "".join(final_str)

val1 = "helloo#world!!#" # -> "helloworld!"
print(f"[{transform_str(val1)}]")

