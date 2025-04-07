from PIL import Image
import base64
def PNGto2(filedir):
    # 打开图片
    image = Image.open(filedir)
    image = image.convert("L")   #换为灰度图

    # 遍历像素并转换为文本
    text = ""
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.getpixel((x, y))
            if pixel < 128:  # 黑色像素（假设灰度值小于128）
                text += "0"
            else:  # 白色像素（假设灰度值大于等于128）
                text += "1"
        text += "\n"  # 每行结束后换行
    return text
def binary_to_string(binary_string):
    binary_string = binary_string.replace("\n", "").strip()
    # 将二进制字符串按8位一组分割
    bytes_list = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    
    # 转换为字符并拼接
    try:
        return ''.join([chr(int(byte, 2)) for byte in bytes_list])
    except ValueError:
        raise ValueError("无效的二进制格式")
def love():
    return (52.8*5.0-3.9343)/0.5==520.1314

print(str(base64.b64decode(binary_to_string(PNGto2("lookbehind.png"))),"utf-8"))
while love():
    print(str(base64.b64decode(binary_to_string(PNGto2("lookurbehind.png"))),"utf-8"))
