import pandas as pd
import os

# 定义一个函数来合并CSV文件并添加“城市”特征
def merge_csv_files_with_city(input_folder, output_file):
    # 获取输入文件夹中的所有CSV文件
    csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]
    
    # 创建一个空的DataFrame来存储合并后的数据
    merged_data = pd.DataFrame()
    
    # 遍历每个CSV文件并合并
    for file in csv_files:
        file_path = os.path.join(input_folder, file)
        
        # 检查文件是否为空
        if os.path.getsize(file_path) > 0:
            try:
                # 尝试以UTF-8编码读取文件
                data = pd.read_csv(file_path, encoding='utf-8')
            except UnicodeDecodeError:
                # 如果失败，尝试以ISO-8859-1编码读取文件
                data = pd.read_csv(file_path, encoding='ISO-8859-1')
            
            # 添加“城市”列，值为文件名（去掉扩展名）
            data['城市'] = os.path.splitext(file)[0]
            
            # 合并数据
            merged_data = pd.concat([merged_data, data], ignore_index=True)
        else:
            print(f"Skipping empty file: {file_path}")
    
    # 将合并后的数据保存到输出文件
    merged_data.to_csv(output_file, index=False)

# 示例调用
input_folder = '/workspaces/thesis/dataset'  # 替换为实际的输入文件夹路径
output_file = '/workspaces/thesis/merged_data.csv'  # 替换为实际的输出文件路径

# 调用函数进行合并
merge_csv_files_with_city(input_folder, output_file)