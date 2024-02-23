# pdf2img-img2txt
## CPU环境下速度很快
一、pytesseract简介
tesseract原意为：宇宙魔方;超立方体;超正方体;四维超正方体;四次元立方体

1.1 pytesseract库
pytesseract为Python开源的OCR（光学字符识别）库，能够识别图片上的数字、英文和中文等。

1.2 pytesseract用途
它要求字迹规整、清晰可见，适合识别电脑和手机截屏等。对各种验证码的识别效果一般。

二、pytesseract安装
pytesseract库属于人工智能(AI)领域的库，AI领域的库安装一般都有点麻烦，不是一条pip就能完成的，需要配置底层应用和依赖库。

2.1 安装和配置底层应用Tesseract-OCR
Tesseract-OCR 是一款由HP实验室开发由Google维护的开源OCR（Optical Character Recognition , 光学字符识别）引擎。与Microsoft Office Document Imaging（MODI）相比，我们可以不断的训练的库，使图像转换文本的能力不断增强；如果团队深度需要，还可以以它为模板，开发出符合自身需求的OCR引擎。

2.1.1 GitHub 官网地址：查看源码
https://github.com/tesseract-ocr/tesseract
在这可以查看和下载源码，自己编译，如果不想查看源码，只想直接使用，请下载下面的官网安装包
2.1.4 配置环境变量
配置系统变量：path
在这里插入图片描述
添加 TESSDATA_PREFIX 系统变量，值为：C:\Program Files\Tesseract-OCR\tessdata
在这里插入图片描述
3.配置系统变量：path，新增 %TESSDATA_PREFIX%
在这里插入图片描述
重启电脑
