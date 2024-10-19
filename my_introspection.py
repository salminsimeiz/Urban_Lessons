from pprint import pprint


def introspection_info(obj):
    """Определяет полезную информацию об объекте (item)"""
    if hasattr(obj, "__name__"):
        print(f"NAME: {obj.__name__}")
    if hasattr(obj, "__class__"):
        print(f"CLASS: {obj.__class__.__name__}")
    print(f"ID: {id(obj)}")
    print(f"TYPE: {type(obj)}")
    print(f"VALUE: {repr(obj)}")
    if callable(obj):
        print("CALLABLE: YES")
    else:
        print("CALLABLE: NO")
    print("ATTRIBUTES & METHODS:")
    pprint(dir(obj))
    if hasattr(obj, "__doc__"):
        doc = getattr(obj, "__doc__").strip().split("\n")[0]
        print(f"DOC: {doc}")


if __name__ == "__main__":
    # introspection_info(obj)
    pass