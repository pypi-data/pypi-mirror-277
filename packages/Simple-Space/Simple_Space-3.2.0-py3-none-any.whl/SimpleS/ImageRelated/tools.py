import os
import cv2
import numpy as np
from PIL import Image
import scipy.ndimage as ndi
import matplotlib.pyplot as plt
from skimage import img_as_ubyte
from scipy.spatial import Delaunay
from skimage.morphology import skeletonize
from SimpleS.Points.Triangle import plot_delaunay_triangle


def delaunay_detection_of_facial_parts(id,
                                         detector,
                                         predictor,
                                         image_array=None,
                                         image_path=None,
                                         show_fig=True,
                                         save_fig=False,
                                         save_path='results/DelaunayDetection_of_FacialParts/'):
    if image_array is not None:
        img = image_array
    elif image_path is not None:
        img = np.array(Image.open(image_path))
    else:
        raise ValueError("You must provide either image_array or image_path for this method to work!")
    fig, ax = plt.subplots()
    try:
        ax.imshow(img)
        detections = detector(img, 1)
    except Exception as e:
        try:
            img = Image.fromarray(img)
            ax.imshow(img)
            detections = detector(img, 1)
        except Exception as e:
            raise ValueError("There was a problem reading your image or image array. Check your path or array and try again.") from e
    keeper = []
    for k, d in enumerate(detections):
        shape = predictor(img, d)
        points = np.array([[p.x, p.y] for p in shape.parts()])
        ax.scatter(points[:, 0], points[:, 1], c='r', s=10)
        delaunay = Delaunay(points)
        keeper.append(delaunay)
        plot_delaunay_triangle(points, delaunay, ax)
    
    plt.axis('off')
    if save_fig:
        path_to_save = os.path.join(save_path, f'image{id}.jpg')
        os.makedirs(save_path, exist_ok=True)
        plt.savefig(path_to_save)
    if show_fig:
        plt.show()
    else:
        plt.close(fig)
        return keeper


def detect_centerline(image,
                                thrhold1 = 7,
                                thrhold2 = 255,
                                c_map ='gray',
                                fig_size =(6, 6),
                                plt_title ='Medial Axis',
                                plt_axis=True,
                                show = True,
                                save=False,
                                save_path = None,
                                silently = False, 
                                just_return_medial = False):
        if isinstance(image, str):
                img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
                if img is None:
                        print("Error loading image")
                        return
        try:
                _, binary = cv2.threshold(image, thrhold1, thrhold2, cv2.THRESH_BINARY)
                binary = binary > 0
                skeleton = skeletonize(binary)
        except:
                try:
                        temp = ndi.distance_transform_edt(image)
                        _, binary = cv2.threshold(temp, thrhold1, thrhold2, cv2.THRESH_BINARY)
                        binary = binary > 0
                        skeleton = skeletonize(binary)
                except:
                        try:
                                skeleton = skeletonize(img)
                        except:
                                print("Error reading image")
                                print("Nothing worked!")
                                return
        skeleton = img_as_ubyte(skeleton)
        if just_return_medial:
                return skeleton
        else:
                pass
        plt.figure(figsize=fig_size)
        plt.imshow(skeleton, cmap=c_map) if show else None
        plt.title(plt_title) if show else None
        if plt_axis:
                plt.axis('off')
        if save:
                if save_path:
                        if not save_path.endswith(('.png' ,'.jpg')):
                                save_path = os.path.join(save_path, f'{plt_title}_{thrhold1}_{c_map}.jpg')
                        else:
                                pass
                else:
                        save_path = f'{plt_title}_{thrhold1}_{c_map}.jpg'
                plt.imsave(save_path,skeleton, cmap=c_map)
        if show:
                plt.show()
        else:
                if save and not silently:
                        print(f"Result is Saved in {save_path}")
                        return
                else:
                        return