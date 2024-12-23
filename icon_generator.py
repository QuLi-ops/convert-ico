from PIL import Image
import sys
import os

def create_icons(input_image_path):
    try:
        # 创建调试日志
        debug_path = os.path.join(os.path.dirname(input_image_path), 'debug.txt')
        with open(debug_path, 'w', encoding='utf-8') as f:
            f.write(f'程序开始运行\n')
            f.write(f'输入文件路径: {input_image_path}\n')
        
        # 打开原始图片
        img = Image.open(input_image_path)
        
        # 获取输出目录（与输入图片相同目录）
        output_dir = os.path.dirname(input_image_path)
        
        with open(debug_path, 'a', encoding='utf-8') as f:
            f.write(f'输出目录: {output_dir}\n')
        
        # 生成 favicon.ico (32x32)
        favicon = img.resize((32, 32), Image.Resampling.LANCZOS)
        favicon_path = os.path.join(output_dir, 'favicon.ico')
        favicon.save(favicon_path, format='ICO')
        
        with open(debug_path, 'a', encoding='utf-8') as f:
            f.write(f'已生成 favicon.ico\n')
        
        # 生成 icon.png (180x180)
        icon = img.resize((180, 180), Image.Resampling.LANCZOS)
        icon_path = os.path.join(output_dir, 'icon.png')
        icon.save(icon_path, format='PNG')
        
        with open(debug_path, 'a', encoding='utf-8') as f:
            f.write(f'已生成 icon.png\n')
        
        # 生成 apple-icon.png (180x180)
        apple_icon_path = os.path.join(output_dir, 'apple-icon.png')
        icon.save(apple_icon_path, format='PNG')
        
        with open(debug_path, 'a', encoding='utf-8') as f:
            f.write(f'已生成 apple-icon.png\n')
        
        # 创建结果文件
        with open(os.path.join(output_dir, 'result.txt'), 'w', encoding='utf-8') as f:
            f.write('图标生成成功！\n')
            f.write(f'生成的文件：\n')
            f.write(f'- {favicon_path}\n')
            f.write(f'- {icon_path}\n')
            f.write(f'- {apple_icon_path}\n')
        
    except Exception as e:
        # 将错误写入文件
        error_path = os.path.join(output_dir, 'error.txt')
        with open(error_path, 'w', encoding='utf-8') as f:
            f.write(f'发生错误: {str(e)}')
        # 同时写入调试文件
        with open(debug_path, 'a', encoding='utf-8') as f:
            f.write(f'发生错误: {str(e)}\n')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        create_icons(sys.argv[1])
    else:
        # 如果没有参数，创建错误日志
        with open('no_input.txt', 'w', encoding='utf-8') as f:
            f.write('没有接收到输入文件\n')
