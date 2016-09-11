import struct


def is_bmp(filename):
    # if isinstance(filename, bytes):
        # f = open(filename, 'rb')
        # s = filename.read(30)
        s = struct.unpack('ccIIIIIIHH', filename)
        try:
            if s[0] == b'b' and s[1] == b'M':
                print('文件是一个Windows位图，图片大小为%d×%d,颜色数为%d' % (s[6], s[7], s[9]))
            elif s[0] == b'b' and s[1] == b'M':
                print('文件是一个OS/2位图，图片大小为%d×%d,颜色数为%d' % (s[6], s[7], s[9]))
            else:
                print('文件不是一个位图')
        finally:
            print('End')
    # else:
        # print('请输入一个二进制比特数据')


t = (b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01'
     + b'\x00\x18\x00')
is_bmp(t)
