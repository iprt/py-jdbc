import os

if __name__ == '__main__':
    os.environ["JAVA_HOME"] = "C:/"
    print("test env")
    java_home = os.environ["JAVA_HOME"]
    print("JAVA_HOME is", java_home)
