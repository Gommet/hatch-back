import numpy as np
import cv2 as cv
from rembg import remove
import argparse


def are_similar(photo1: str, photo2: str, with_bg: int = 10, without_bg: int = 2) -> bool:
    res1, res2 = matches(photo1, photo2)
    return res1 > without_bg and res2 > without_bg

def matches(photo1: str, photo2: str) -> tuple[int, int]:
    img1bg = cv.imread(photo1,0)          # queryImage
    img2bg = cv.imread(photo2,0) # trainImage
    img1 = remove(img1bg)
    img2 = remove(img2bg)
    # Initiate SIFT detector
    # store all the good matches as per Lowe's ratio test.
    # good = []
    res1 = number_of_matches(img1, img2)
    res2 = number_of_matches(img1bg, img2bg)
    return res1, res2
 


def get_matches(img1, img2):
    sift = cv.SIFT_create()
    # find the keypoints and descriptors with SIFT
    _, des1 = sift.detectAndCompute(img1,None)
    _, des2 = sift.detectAndCompute(img2,None)
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 50)
    flann = cv.FlannBasedMatcher(index_params, search_params)
    return flann.knnMatch(des1,des2,k=2)
 
 
def number_of_matches(img1, img2):
     return sum(1 for m, n in get_matches(img1, img2) if m.distance < 0.7 * n.distance)

    
def main():
    parser = argparse.ArgumentParser(description='Return if two photos are similar.')
    parser.add_argument('photo1', action='store', type=str, help='fist photo')
    parser.add_argument('photo2', action='store', help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print(are_similar(args.photo1, args.photo2))

if __name__ == '__main__':
    main()



