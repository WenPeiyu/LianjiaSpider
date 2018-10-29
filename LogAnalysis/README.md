## LogAnalysis 日志分析
### 简介

### 模块框架
#### 日志

### 示例
例子1(从3GPP协议存储网站下载38系列全部协议):

    >>>client = FTPClient("ftp.3gpp.org", 21, "anonymous")
    >>>client.connect()
    >>>client.download(r"/Specs/archive/38_series/", "H:/specs", "nlst") # 不支持mlsd检索目录的网站可用nlst方法替代
    
例子2(开通ftp服务器的本地的上传下载演示):

    >>>client = FTPClient("127.0.0.1", 21, "root", "root")
    >>>client.connect()
    >>>client.upload("/test/", "h:/folder1/")
    >>>client.download("/test/", "h:/folder2/")