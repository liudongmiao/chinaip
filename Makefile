
mac: delegated-apnic-latest
	@(cat ip-up.mac.txt ; python chinaip.py delegated-apnic-latest 16 2>/dev/null) > ip-up
	@(cat ip-down.mac.txt ; python chinaip.py delegated-apnic-latest 16 2>/dev/null) > ip-down
	@chmod +x ip-up ip-down
	@if [ `uname -s` = 'Darwin' ]; then echo 请运行: sudo cp ip-up ip-down /etc/ppp/; else echo 目前仅支持mac os x; fi
	
delegated-apnic-latest:
	curl -O http://ftp.apnic.net/stats/apnic/delegated-apnic-latest
