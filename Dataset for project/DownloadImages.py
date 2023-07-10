import requests
from multiprocessing import Pool
import time

err_file = open("error.txt","w")
### 9260790
i = 1

def dowonlaod_img(line:str):


    time.sleep(0.75)
    output_dir = "/media/robertwang/data1/images/"
    temp = line.strip("\n").split("\t")
    name = temp[0]
    img_url = temp[1]
    try:
        global i
        img = requests.get(img_url)
        img_data = img.content
        with open(output_dir + name + '.jpg', 'wb') as handler:
            handler.write(img_data)
        img.close()
        print(i / 9300000.0)
        i = i + 128
    except Exception as e:
        err_file.write(name+"\t"+img_url+"\n")
        print(e)


if __name__ == "__main__":

    f = open("images_url2.csv","r")
    lines = f.readlines()
    p = Pool(128)
    p.map(dowonlaod_img,lines)
