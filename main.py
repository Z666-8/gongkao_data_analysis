# 公考刷题数据统计小工具 - Mac老年人版，直接运行
import csv
import pandas as pd

# 读取刷题数据，解决Mac中文乱码问题
df = pd.read_csv('data.csv', encoding='utf-8-sig')

# 统计核心指标：总刷题量、平均正确率、高频错题模块
total_questions = df['刷题量'].sum()
df['正确率数值'] = df['正确率'].str.replace('%', '').astype(float)
avg_accuracy = df['正确率数值'].mean()
top_error_module = df['错题模块'].value_counts().index[0] if not df['错题模块'].empty else '无'

# 格式化输出结果，看得更清楚
print("===== 公考刷题数据统计结果 =====")
print(f"累计刷题总量：{total_questions} 道")
print(f"平均答题正确率：{avg_accuracy:.1f}%")
print(f"高频错题模块：{top_error_module}")
print("==============================")