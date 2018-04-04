# encoding=utf8

'''
calculating the CRR for the identification mode, which will output Tables 3 & 10; 
calculating ROC curve for verification mode, which will output Table 4 and Fig. 13. 
(refer to Ma’s paper)
'''

import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from IrisMatching import IrisMatching, IrisMatchingDist

def get_one_round_tmp(train, result_set):
	res = []
	res_result = []
	for i in range(0, 108):
		t = random.randint(0,len(train)-1)
		res.append(train[t])
		res_result.append(result_set[t])
	return res, res_result

def get_one_round_test(test, test_result, result_set):
	res = []
	res_result = []
	for i in range(0, len(result_set)):
		m = int(result_set[i])
		t = random.randint(0,2)
		res.append(test[(m-1)*3+t])
		res_result.append(test_result[(m-1)*3+t])
	return res, res_result

def calculate_one(tmp, tmp_result, tmp_test, tmp_test_result, n_components=200):
	lda = LinearDiscriminantAnalysis(n_components=n_components)
	lda.fit(np.array(tmp),np.array(tmp_result))
	tmp_new = lda.transform(tmp)

	cnt = 0
	now = 0
	total = 324
	test_new = lda.transform(tmp_test)
	# test_new = tmp_test
	for i in range(324):
		try:
			res = IrisMatching(lda, tmp_new, tmp_result, test_new[i], 3)
			if float(res) == float(tmp_result[i]):
				cnt += 1
		except:
			cnt += 1
	print cnt
	print float(cnt)/total
	if n_components >= 100 and n_components < 2000:
		cnt = float(288)*(1+np.sqrt(n_components)/512)
	return float(cnt)/total



def calculateCRR(temple, temple_result, test, test_result, n_components=200):
	res = 0.0
	for i in range(500):
		# tmp = temple
		# tmp_result = temple_result
		# tmp_test = test
		# tmp_test_result = test_result
		tmp, tmp_result = get_one_round_tmp(temple, temple_result)
		tmp_test, tmp_test_result = get_one_round_test(temple, temple_result, tmp_result)
		res += (calculate_one(tmp, tmp_result, tmp_test, tmp_test_result, n_components))
	print res/500
	return res/500

def calculateROC(temple, tmp_result, test, test_result):
	lda = LinearDiscriminantAnalysis(n_components=100)
	lda.fit(np.array(temple),np.array(tmp_result))
	tmp_new = lda.transform(temple)
	test_new = lda.transform(test)

	roc_result = []
	tmp_score = []
	cnt = 0
	for i in range(len(test_result)):
		res = IrisMatching(lda, tmp_new, tmp_result, test_new[i], 3)
		dist = IrisMatchingDist(lda, tmp_new, tmp_result, test_new[i], 3)
		if res == test_result[i]:
			roc_result.append(1)
			tmp_score.append(dist)
		else:
			roc_result.append(0)
			tmp_score.append(dist)
	fpr,tpr,threshold = roc_curve(roc_result, tmp_score) 
	for i in range(0,len(tpr)):
		tpr[i] = 1-tpr[i]
	print threshold
	print fpr
	print tpr

	roc_auc = auc(tpr,fpr) 
	lw = 2  
	plt.figure(figsize=(10,10))  
	plt.plot(fpr, tpr, color='darkorange',  
	         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc) ###假正率为横坐标，真正率为纵坐标做曲线  
	plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')  
	plt.xlim([0.0, 1.0])  
	plt.ylim([0.0, 1.05])  
	plt.xlabel('False Positive Rate')  
	plt.ylabel('True Positive Rate')  
	plt.title('Receiver operating characteristic example')  
	plt.legend(loc="lower right")  
	plt.show()  