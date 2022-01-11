import subprocess #สำหรับ รัน terminal command

if __name__== "__main__":
    subprocess.run(["ls","-l"])
    for i in [2,5,6,9]:
        subprocess.run(["python", "python pyhon_script_101.py", "8", "--x", f"{i}", "--yval", "8"])