#检验秘钥
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.exceptions import InvalidSignature
import json
import sys
import base64

def verify_license():
    try:
        # 加载公钥
        public_key_pem = b"""-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCXUGE97OI9fk6zOTo3Pq+G1ebC
3a+AtsinBGS4BRu0r2Xkgz+Frb+p2l8WA5oRQuw6AdlmYosmTCDU60oogHb3ukVx
oxBjpPP77dP+GtThq8oAAxCwNMrggtVFRuMgvysJGteLH956rDBYBMoHpBqK9ZxN
bi7Eq/0tz33usn69owIDAQAB
-----END PUBLIC KEY-----"""
        public_key = load_pem_public_key(public_key_pem)

        # 读取证书文件
        with open("license.cert", "rb") as f:
            data = f.read().split(b"\n----SIGNATURE----\n")
            cert_data, signature = data[0], data[1]

        # 验证签名
        public_key.verify(
            signature,
            cert_data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        cert_info = json.loads(cert_data.decode())
        return True
    except (FileNotFoundError, InvalidSignature, KeyError, ValueError) as e:
        print("证书验证失败:", str(e))
        return False

if __name__ == "__main__":
    if verify_license():
        #授权验证成功
        print (str(base64.b64decode("5L2g55yL55yL5L2g5ZCO6Z2i5ZGi"),"utf-8"))
        while True:
            print (str(base64.b64decode("5L2g5YaN55yL55yL5L2g5ZCO6Z2i5ZGi"),"utf-8"))
    else:
        print("未授权使用。")
        sys.exit(1)
