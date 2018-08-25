from scipy.stats import beta
a1_prior = 1
b1_prior =1
visitors_A = 12345 # 网站A的访问人数
visitors_B = 1616  # 网站B的访问人数
conversions_from_A = 1200 # 网站A的转化人数
conversions_from_B = 150 # 网站B的转化人数
 
posterior_A = beta(a1_prior+ conversions_from_A,b1_prior + visitors_A -conversions_from_A)
posterior_B = beta(a1_prior+conversions_from_B,b1_prior + visitors_B-conversions_from_B)
# 对后验概率进行采样，用rvs方法生成样本
samples = 20000
samples_posterior_A = posterior_A.rvs(samples)
samples_posterior_B = posterior_B.rvs(samples)
# 对后验概率进行比较
cmp_value = samples_posterior_A > samples_posterior_B
mean_value = cmp_value.mean()
print (mean_value)
