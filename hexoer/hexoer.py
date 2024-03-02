import os
import subprocess
import time

def hexoer():
    # get all the file names
    path = os.getcwd()
    files = os.listdir(path)
    files.remove(os.path.basename(__file__))
    postsPath = os.path.abspath(os.path.dirname(path)) + "\source\_posts"

    counter = 0
    total = len(files)
    for file in files:
        # get create time
        modiTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(os.path.getmtime(file)))
        # create an empty hexo-style md file
        # ---
        # title: xxx
        # date: Y-m-d H:M:S
        # ---
        cmd = "hexo new " + file[:-3]
        ret = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
        out, err = ret.communicate()
        newName = out.decode('utf-8')
        newName = os.path.basename(newName[newName.find("Created") + 9 : -1])

        # modify hexo-style md file
        data = ""
        with open(postsPath + '\\' + newName, 'r', encoding = 'utf-8') as newFile:
            for line in newFile:
                if line.find("date:") != -1:
                    line = line[:6] + modiTime + '\n'
                data += line
        with open(postsPath + '\\' + newName, 'w', encoding = 'utf-8') as newFile:
            newFile.write(data)
            # append old file's content to new file
            with open(path + '\\' + file, 'r', encoding = 'utf-8') as oldFile:
                newFile.write(oldFile.read())
        
        # counter
        print("{}/{}".format(count, total))
        count += 1


if __name__ == "__main__":
    hexoer()