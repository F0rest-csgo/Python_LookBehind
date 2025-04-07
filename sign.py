from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key
import json

# 加载私钥
with open("private_key.pem", "rb") as f:
    private_key = load_pem_private_key(f.read(), password=None)

# 证书内容
cert_data = {
    "valid_until": "2099-12-31",
    "license_to": "F0rest"
}

# 生成签名
signature = private_key.sign(
    json.dumps(cert_data).encode(),
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# 保存证书文件和签名
with open("license.cert", "wb") as f:
    f.write(json.dumps(cert_data).encode())
    f.write(b"\n----SIGNATURE----\n")
    f.write(signature)
