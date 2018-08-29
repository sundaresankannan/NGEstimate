# Created for General Util
import hashlib
import uuid

class Util():
	def __init__(self,pwd):
		pass

	def pwdenctypted(pwd):
		#salt = uuid.uuid4().hex
		sha_signature = hashlib.sha256(pwd.encode()).hexdigest()#+'$' + salt
		return sha_signature
	
	def matchHashedText(hashedText,providedpwd):
		 #_hashedText, salt = hashedText.split('$')
		 return  hashedText == hashlib.sha256(providedpwd.encode()).hexdigest()