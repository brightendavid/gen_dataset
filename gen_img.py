import cv2

video_path = r'C:\Users\brighten\Desktop\3.mp4'  # 视频地址
output_path = 'video2img1/'  # 输出文件夹
interval = 25  # 每间隔10帧取一张图片

if __name__ == '__main__':
    num = 2880
    vid = cv2.VideoCapture(video_path)
    while vid.isOpened():
        is_read, frame = vid.read()
        if is_read:
            if num % interval == 1:
                file_name = '%08d' % num
                cv2.imwrite(output_path + str(file_name) + '.png', frame)
                # 00000111.jpg 代表第111帧
                cv2.waitKey(1)
            num += 1
        else:
            break
