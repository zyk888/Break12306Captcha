import glob
import json
import sys
import os
import argparse
from image_hash.captcha_mapper import captcha_mapper
from merge_image import hamming_dist


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("dict_path", action="store",
                        help="specify the file containing buckets and mapping")
    parser.add_argument("image_dir", action="store",
                        help="specify the directory of new CAPTCHAs")

    args = parser.parse_args()
    t_dict = json.load(open(args.dict_path))
    filepaths = glob.glob(os.path.join(args.image_dir, "*.jpg"))
    rgb2final = t_dict['rgb2final']
    buckets = t_dict['buckets']
    dist = t_dict.get('dist', 15)
    hit = 0.
    total = len(filepaths) * 8.
    for f in filepaths:
        line = captcha_mapper(f)
        content = line.split('\t')
        for i in xrange(len(content) // 2):
            gray_phash, rgb_phash = content[i*2+1], content[i*2+2]
            if gray_phash not in buckets:
                continue
            if rgb_phash in rgb2final:
                hit += 1
                continue
            for t in buckets[gray_phash]:
                if hamming_dist(t, rgb_phash) <= dist:
                    hit += 1
                    break
    print "%.0f/%.0f=%.2f of new images appeared" % (hit, total, (hit/total))
