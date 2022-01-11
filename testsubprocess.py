import subprocess #สำหรับ รัน terminal command

if __name__== "__main__":
    subprocess.run(["ls","-l"])
    for i in [2,5,6,9]:
        subprocess.run(["python", "pyhon_script_101.py", "8", "--x", f"{i}", "--yval", "8"])


    ## use output of subprocess
    pro = subprocess.Popen(["ls","-l"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = pro.communicate()
    print(out)    


    ##HW ให้ print เฉพาะ ตัวเลขผลลัพธ์การคูณ
    ##for i in [2,5,6,9]:
    ##    subprocess.run(["python", "pyhon_script_101.py", "8", "--x", f"{i}", "--yval", "8"])