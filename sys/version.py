import sys

print(dir(sys))

print(sys.version)
print(sys.version_info)
print(sys.platform)
print(sys.modules)

print(sys.modules["os"])
print(sys.modules.keys())
print(sys.builtin_module_names)
print(sys.path)
print(sys.argv)

def main():
    if len(sys.argv) > 1:
        print(sys.argv[1])

if __name__ == "__main__":
    main()

