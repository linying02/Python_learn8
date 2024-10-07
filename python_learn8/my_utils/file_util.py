def print_file_info(file_name):
    f = None
    try:
        f = open(file_name,"r",encoding="UTF_8")
    except Exception as e:
        print("文件不存在")
        print(e)
    else:
        content = f.read()
        print(content)
    finally:
        if f:
            f.close()
def append_to_file(file_name,date):
    f = open(file_name,"a",encoding="UTF_8")
    f.write(date)
    f.flush()
    f.close()
append_to_file("E:/Python4.txt","7777777777")

