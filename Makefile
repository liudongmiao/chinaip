
mac: delegated-apnic-latest
	@(cat ip-up.mac.txt ; python chinaip.py delegated-apnic-latest 16 2>/dev/null; echo 202.141.160.0/19) > ip-up
	@(cat ip-down.mac.txt ; python chinaip.py delegated-apnic-latest 16 2>/dev/null; echo 202.141.160.0/19) > ip-down
	@chmod +x ip-up ip-down
	@cp ip-up ip-down mac/
	@if [ `uname -s` = 'Darwin' ]; then echo 请运行: sudo cp ip-up ip-down /etc/ppp/; else echo 目前仅支持mac os x; fi
	
delegated-apnic-latest:
	curl -O http://ftp.apnic.net/stats/apnic/delegated-apnic-latest

.PHONY: mac
