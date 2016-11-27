from PIL import Image
import numpy as np
import os


def calc_perceptual_hash(image_path, mode):
    """ Functions to calculate perceptual hashes of RGB or GRAY images
    :type image_path: str
    :type mode: str
    :rtype: np.ndarray
    """

    def helper(_arr):
        """ A helper function to calculate perceptual hash for a single channel or gray scale"""
        assert isinstance(_arr, np.ndarray) and _arr.shape == (8, 8)
        _arr_mean = _arr.mean()
        _arr_filtered = 1 * (_arr > _arr_mean)  # change bool to 1s and 0s
        _arr_hash = _arr_filtered.flatten()
        return _arr_hash

    # Sanity check
    assert os.path.exists(image_path), '{} does not exist!'.format(image_path)
    assert mode in {'RGB', 'GRAY'}, '{} mode does not exist!'.format(mode)

    # Open a new image and resize it
    image = Image.open(image_path).resize((8, 8))

    if mode == 'GRAY':
        # change RGB images to GRAY
        image_array = np.asarray(image.convert('L'))
        image_hash = helper(image_array)
        return image_hash

    else:
        image_array = np.asanyarray(image)

        red_hash = helper(image_array[:, :, 0])
        green_hash = helper(image_array[:, :, 1])
        blue_hash = helper(image_array[:, :, 2])

        image_hash = np.concatenate((red_hash, green_hash, blue_hash))

        return image_hash


def image_diff(img_fname1, img_fname2):
    assert os.path.exists(img_fname1) and os.path.exists(img_fname2)

    phash1, phash2 = map(calc_perceptual_hash, (img_fname1, img_fname2))

    return np.sum(phash1 != phash2)


def calc_num_2_bin_one_count():
    with open('../data/num_2_bin_one_count.csv', 'w') as writer:
        cur_num = 0
        while cur_num < 2 ** 192:
            cur_one_count = sum(map(int, bin(cur_num)[2:]))
            writer.write('{},{}\n'.format(cur_num, cur_one_count))
            cur_num += 1
            if sum(map(int, str(cur_num))) == 1:
                print cur_num


def test():
    print image_diff('../data/bfzw.png', '../data/sxey.png')
    print image_diff('../data/mh.png', '../data/xf.png')
    print image_diff('../data/bfzw.png', '../data/xf.png')
    print image_diff('../data/bfzw.png', '../data/mh.png')
    print image_diff('../data/sxey.png', '../data/mh.png')
    print image_diff('../data/sxey.png', '../data/xf.png')


if __name__ == '__main__':
    test()
    # calc_num_2_bin_one_count()
