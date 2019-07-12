def merge_dictonaries(src, target):
    for key in target:
        if key in src:
            src[key] = src[key] + target[key]
        else:
            src[key] = target[key]
    return src
