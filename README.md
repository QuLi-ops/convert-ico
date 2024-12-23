# Icon Generator

一个简单的图标生成工具，可以快速生成网站所需的各种尺寸的图标文件。

## 功能特点

- 一键生成多种尺寸的图标
- 支持拖拽操作
- 自动生成以下格式：
  - favicon.ico (32×32) - 用于网站标签页图标
  - icon.png (180×180) - 用于通用图标
  - apple-icon.png (180×180) - 用于 iOS 设备

## 使用方法

1. 在/dist目录下找到 `icon_generator.exe`
2. 准备一张高质量的源图片（建议尺寸大于 180×180）
3. 将图片直接拖放到 `icon_generator.exe` 上
4. 程序会在图片所在目录自动生成3个文件 
`favicon.ico` 
`icon.png` 
`apple-icon.png`
5.如果使用的是next.js 13+， app路由 直接把这三个文件放到app目录下即可


## 支持的格式

### 输入格式
- PNG
- JPG/JPEG
- 其他常见图片格式

### 输出文件
- ICO (favicon)
- PNG (标准图标)

## 建议

- 使用正方形图片作为源文件，避免图标变形
- 源图片分辨率建议至少 180×180 像素
- 使用简洁清晰的图案，以确保小尺寸图标的可识别性
