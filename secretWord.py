#-*- coding: utf-8 -*-

secretWord = "throughput"	# 맞춰야 할 단어
correctLetters = ["t", "a", "u"]	# 사용자가 입력한 알파벳
result = ""	# 결과로 출력되는 문장


for word in secretWord:
     if word in correctLetters:
             result += word
     else:
             result += "_"
			 
print result