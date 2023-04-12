import os
def delete(dir1,dir2):
    files1 = os.listdir(dir1) # xml
    files2 = os.listdir(dir2) # pictures
    for i in range(len(files1)):
        files1[i] = files1[i][:-4]
    print(files1)

    for name in files2:
        name2 = name[:-4]
        # print(name2)
        if (name2 in files1):
            pass
        else:
            # name1 =name+".png"
            print(name)
            di =os.path.join(dir2,name)
            print(di)
            os.remove(di)





        # print(src_size)
        # src = Image.open(src_dir + "/" + name).convert("RGB")
        # src = np.array(src)
        #
        # src_re = BiLinear_interpolation(src, src_size[1], src_size[0])
        # result = Image.fromarray(src_re.astype(np.uint8))
        # result.save(save_dir + "/" + name)




if __name__ == '__main__':
    delete(r"C:\Users\brighten\Desktop\MyDataset\Annotations",r"C:\Users\brighten\Desktop\MyDataset\JPEGImage")