import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import os

# 定义一个函数来对CSV文件进行One-Hot编码
def onehot_encode_csv(input_file, output_file):
    # 读取CSV文件
    merged_data = pd.read_csv(input_file)
    
    # 初始化OneHotEncoder
    encoder = OneHotEncoder(sparse_output=False)
    
    # 假设需要对“城市”列进行One-Hot编码
    if '城市' in merged_data.columns:
        # 进行One-Hot编码
        encoded_data = encoder.fit_transform(merged_data[['城市']])
        
        # 将编码后的数据转换为DataFrame
        encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(['城市']))
        
        # 将编码后的数据与原始数据合并
        merged_data = merged_data.drop('城市', axis=1)
        merged_data = pd.concat([merged_data, encoded_df], axis=1)
    
    # 将合并后的数据保存到输出文件
    merged_data.to_csv(output_file, index=False)

# 示例调用
input_file = '/workspaces/thesis/merged_data.csv'  # 替换为实际的输入文件路径
output_file = '/workspaces/thesis/encoded_merged_data.csv'  # 替换为实际的输出文件路径

# 调用函数进行One-Hot编码
onehot_encode_csv(input_file, output_file)

print("One-hot编码完成，结果已保存到encoded_data.csv")