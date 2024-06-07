from client import EAPIClient


# 创建默认的客户端
def create_client(access_key, secret_key, user_account, user_password, base_url):  # baseUrl要改成部署后的网关
    client = EAPIClient(access_key, secret_key, user_account, user_password, base_url)
    return client.call_api({"question": "你好"}, 3)

create_client ("your_accessKey", "your_secretKey",'your_account', "your_password", "interface_url")

