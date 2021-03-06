#!/usr/bin/env python
#coding=utf8

from directory.sensitiveWord import *
from directory.webshell import *
from directory.codition_code import *

#过滤类
class FilterShell:
	#基于敏感文件名过滤
	def filename(self, ext, name):
		if ext == "php":
			if name in php_webshell:
				return True
			else:
				return False
		elif ext == "asp":
			if name in asp_webshell:
				return True
			else:
				return False
		elif ext == "apsx":
			if name in aspx_webshell:
				return True
			else:
				return False
		elif ext == "jsp":
			if name in jsp_webshell:
				return True
			else:
				return False
		elif ext == "all":
			if name in (php_webshell + asp_webshell + aspx_webshell + jsp_webshell):
				return True
			else:
				return False
		else:
			print "args error!"
			exit(0)
    
    	#基于敏感内容过滤
	def content(self, ext, ctent):
		if ext == "php":
			for word in php_sensitive_words.keys():
				if word in ctent:
					return php_sensitive_words.get(word)
			return False
		elif ext == "asp":
			for word in asp_sensitive_words.keys():
				if word in ctent:
					return asp_sensitive_words.get(word)
			return False
		elif ext == "aspx":
			for word in aspx_sensitive_words.keys():
				if word in ctent:
					return aspx_sensitive_words.get(word)
			return False
		elif ext == "jsp":
			for word in jsp_sensitive_words.keys():
				if word in ctent:
					return jsp_sensitive_words.get(word)
			return False
		elif ext == "all":
			all_sensitive_words.update(php_sensitive_words)
			all_sensitive_words.update(asp_sensitive_words)
			all_sensitive_words.update(jsp_sensitive_words)
			all_sensitive_words.update(aspx_sensitive_words)
			for word in all_sensitive_words.keys():
				if word in ctent:
					return all_sensitive_words.get(word)
			return False
		else:
			print "args error!"
			exit(0)
