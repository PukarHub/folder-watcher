def give__extensions(onlyfiles):
    extensions = []
    for x in onlyfiles:
        ext = x.split('.')
        extensions.append(ext[-1])
    extensions = set(extensions)
    return extensions 

