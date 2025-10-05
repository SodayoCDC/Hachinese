# 字符串转HaChinese
code_list = []
first_mid_list = []
ha_chi_list = []
result = ''

text = input('输入需要加密的内容')

for c in text:
    code_list.append(bin(ord(c)))

for i in code_list:
    first_mid_list.append(i[2:])

for binaries in first_mid_list:
    for bit in binaries:
        if bit == '0':
            ha_chi_list.append('哈基米')
        if bit == '1':
            ha_chi_list.append('曼波')
    ha_chi_list.append('纳美鲁多')
for hachi in ha_chi_list:
    result += hachi
print(result)





