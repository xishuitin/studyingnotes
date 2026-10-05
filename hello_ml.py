import numpy as np
score_dict = {
    "张三": 95,
    "李四": 88,
    "王五": 76,
    "赵六": 92
}

def calc_score_info(score_data):
    scores = list(score_data.values())
    avg = sum(scores) / len(scores)
    max_score = max(scores)
    max_name = [name for name,s in score_data.items() if s == max_score]
    return avg, max_score, max_name
avg_score, highest_score, highest_name = calc_score_info(score_dict)
print("====学生成绩信息====")
print(f"平均分: {avg_score:.2f}")
print(f"最高分: {highest_score}, 学生: {', '.join(highest_name)}")


mat_a = np.array([[1, 2], 
                  [3, 4]])
mat_b = np.array([[5, 6], [7, 8]])
mat_result = mat_a @ mat_b

print("\n====矩阵相乘结果====")
print(f"矩阵A:\n{mat_a}")
print(f"A的形状: {mat_a.shape}")
print(f"矩阵B:\n{mat_b}")
print(f"B的形状: {mat_b.shape}")
print(f"A*B的結果矩阵:\n{mat_result}")
print(f"结果矩阵的形状: {mat_result.shape}")