import os
import sys
import chardet


def converter(filePath):
    if any([filePath.endswith(extension) for extension in '.srt,.ass,.txt'.split(',')]):
        with open(filePath, "rb") as F:
            text = F.read()
            enc = chardet.detect(text).get("encoding")
            if enc and enc.lower() != "utf-8":
                try:
                    text = text.decode(enc)
                    text = text.encode("utf-8")
                    with open(filePath, "wb") as f:
                        f.write(text)
                        print
                        u"%s сконвертирован." % filePath
                except:
                    print
                    u"Ошибка в имени файла: название содержит русские символы."
            else:
                print
                u"Файл %s находится в кодировке %s и не требует конвертирования." % (filePath, enc)
            print
            '-' * 40


if __name__ == '__main__':
    if len(sys.argv[1:]) == 0:
        try:
            path = input(u"Input path or file:")
        except KeyboardInterrupt:
            print
            u"Ввод отменён."
            sys.exit(0)
    else:
        path = sys.argv[1:][0]
    if os.path.isdir(path):
        last = path[-1]
        if last.endswith('/'):
            path = path
        else:
            path = path + "/"
        print
        path
        for (path, dirs, files) in os.walk(path):
            for file in files:
                filePath = path + file
                filePath = filePath.decode("utf-8")
                converter(filePath)
    elif os.path.isfile(path):
        converter(path)
sys.exit(0)