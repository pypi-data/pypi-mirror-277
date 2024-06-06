from flask import request


def getIpAdd():
    if request:
        ip = (request.environ.get('HTTP_X_FORWARDED_FOR') or request.environ.get("HTTP_PROXY_CLIENT_IP") or request.environ.get("HTTP_WL_PROXY_CLIENT_IP")
              or request.environ.get("HTTP_X_REAL_IP") or request.environ.get("") or request.environ.get('REMOTE_ADDR'))
        return "127.0.0.1" if ip == "0:0:0:0:0:0:0:1" else one_more_ip(ip)
    return None


def one_more_ip(ip):
    for item in str(ip).split(","):
        if len(item.strip()) > 0:
            return item.strip()
    return None


def isMatchedIp(blackStr: str, ip):
    if not blackStr or not ip:
        return False
    return ip in blackStr.split(";")
