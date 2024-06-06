# 创建一个读取excel文件，展示excel中sheet数量，每个sheet的数据结构等信息的库

import pandas as pd

def 读取excel信息(file_path):
    """
    读取给定路径的excel文件，展示excel中sheet数量，每个sheet的数据结构等信息

    参数:
    file_path (str): excel文件的路径

    返回:
    dict: 包含每个sheet名称及其数据结构信息的字典
    """
    try:
        # 读取excel文件
        excel_file = pd.ExcelFile(file_path)
        # 获取所有sheet名称
        sheet_names = excel_file.sheet_names
        # 初始化结果字典
        result = {}
        
        for sheet in sheet_names:
            # 读取每个sheet的数据
            df = pd.read_excel(file_path, sheet_name=sheet)
            # 获取数据结构信息
            data_info = {
                "行数": df.shape[0],
                "列数": df.shape[1],
                "列名": df.columns.tolist()
            }
            # 将信息存入结果字典
            result[sheet] = data_info
        
        return result
    except Exception as e:
        # 记录错误日志
        with open("error_log.txt", "a") as log_file:
            log_file.write(f"读取excel信息时出错: {e}\n")
        return None

