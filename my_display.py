import matplotlib.pyplot as plt
import cv2

def displayImageListFromImport(rows, columns, path_plt,):
    plt.style.use('ggplot')

    fig = plt.figure(figsize=(12, 12))

    for i in range(1, rows * columns + 1):
        fig.add_subplot(rows, columns, i)
        img_plt_path = path_plt[i]
        plt_image = plt.imread(img_plt_path)
        plt.imshow(plt_image,)
        # plt.axes('off')
    plt.show()