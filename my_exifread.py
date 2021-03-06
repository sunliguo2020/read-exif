import exifread
import os
import shutil

'''
{'MI 5s', 'HUAWEI G730-U00', 'ARS-AL00'}

'''


def mymovefile(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        print("{0} is not exits!".format(srcfile))
    else:
        fpath, fname = os.path.split(dstfile)
        if not os.path.exists(fpath):
            os.mkdir(fpath)
        shutil.move(srcfile, dstfile)
        print("move {0} -> {1}".format(srcfile, dstfile))


def mycopyfile(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        print("{0} is not exits!".format(srcfile))
    else:
        fpath, fname = os.path.split(dstfile)
        if not os.path.exists(fpath):
            os.mkdir(fpath)
        shutil.copy(srcfile, dstfile)
        print("copy {0} -> {1}".format(srcfile, dstfile))


def exif_Image_Model(file_name, type='Image Model'):
    """
    返回 jpg文件中exif的 设备型号(Image Model)
    :param file_name:
    :return:
    """
    if not os.path.isfile(file_name):
        return

    try:
        f = open(file_name, 'rb')
        tag = {}
        tag = exifread.process_file(f)
    except Exception as e:
        print("读取exif失败", file_name, e)
    # else:
    #     tag = {}
    finally:
        f.close()

    result = tag.get(type)

    if result is not None:
        image_camera = str(result).strip()
    else:
        image_camera = None

    return image_camera


def get_img_model(img_dir):
    """
    给定目录，返回文件路径名和相机型号的字典。
    :param dir:要查询的目录
    :return:键位
    """

    img_model_dict = {}

    for root, dirs, files in os.walk(img_dir, topdown=False):
        for file_name in files:

            if os.path.splitext(file_name)[-1][1:] == "jpg":
                file_path_name = os.path.join(root, file_name)

                file_image_model = exif_Image_Model(file_path_name)

                print(file_path_name, file_image_model)

                if file_image_model is not None:
                    img_model_dict[file_path_name] = file_image_model

    return img_model_dict


if __name__ == "__main__":
    # img_camera_dict = get_img_model(r'E:\孙婉贻')
    # print(set(img_camera_dict.values()))
    # print(len(img_camera_dict))
    #
    # for file_path,camera in img_camera_dict.items():
    #     #print(file_path,camera)
    #     file_name=os.path.split(file_path)[-1]
    #     if camera != "MI 5s":
    #         print(file_path,camera)
    #         #mymovefile(file_path,os.path.join("h:\\",camera,file_name))
    #
    #     #print("file_path:{0},camear:{1}".format(file_path,camera))
    #
    #     #mymovefile(file_path,os.path.join("h:\\",camera,file_name))

    for root, dirs, files in os.walk(r'E:\Nikon Transfer\abc'):
        for f in files:

            file_path = os.path.join(root, f)
            print(file_path)

            result = exif_Image_Model(file_path, type="Image DateTime")
            if result:
                dest_dir= os.path.join(r'E:\Nikon Transfer\abc',result[:10].replace(':',"-"))
                print(dest_dir)
                mymovefile(file_path,os.path.join(dest_dir,f))


