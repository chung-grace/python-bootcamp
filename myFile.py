# aList = [1, 2, 3, "pop", "sunday"]

# for item in aList:
#     print(item)
#     if item == "sunday":
#         print("yay")

import sys

def main():
    print(sys.argv, type(sys.argv))
    print(len(sys.argv))
    print(sys.argv[0])
    print(sys.argv[1])

if __name__ == '__main__':
    main()
