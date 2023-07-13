import os

if __name__ == '__main__':
    print("set JAVA_HOME")
    os.environ["JAVA_HOME"] = "./jre"

    print("get JAVA_HOME :", os.environ["JAVA_HOME"])
