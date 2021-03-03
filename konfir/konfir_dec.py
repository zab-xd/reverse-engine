# yang ini di dec oleh Khairul:v
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Dec  5 2019, 10:47:43) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: RIZKY
import requests, os, re, time, sys
from bs4 import BeautifulSoup as parser
reload(sys)
sys.setdefaultencoding('utf8')
logo = "       \x1b[0;97mAuthor : fb.com/rizky.rasata\n   __ __          ____                    _\n  / //_/__  ___  / _(_)_____ _  ___ ____ (_)\n / ,< / _ \\/ _ \\/ _/ / __/  ' \\/ _ `(_-</ /\n/_/|_|\\___/_//_/_//_/_/ /_/_/_/\\_,_/___/_/"
url = 'https://mbasic.facebook.com'
per = 'https://mbasic.facebook.com/friends/center/requests/#friends_center_main'

def login():
	os.system('clear')
	print logo
	try:
		cookie = str(raw_input('\n+ Cookies fb ? ')).strip()
		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 'cookie': cookie}
		cookies = {'cookie': cookie}
		req = requests.get(url, headers=headers, cookies=cookies).text
		if 'mbasic_logout_button' in req:
			print '\xe2\x88\x9a Berhasil login'
			b = open('coki.log', 'w')
			b.write(cookie)
			b.close()
			time.sleep(1)
			menu()
		else:
			print '\xc3\x97 Cookies salah '
			time.sleep(1)
			login()
	except:
		print '\xc3\x97 Cookies salah'
		login()


def menu():
	os.system('clear')
	print logo
	try:
		cookie = open('coki.log', 'r').read().strip()
		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 'cookie': cookie}
		cookies = {'cookie': cookie}
	except:
		os.system('rm -rf coki.log')
		print '\xc3\x97 Cookies tidak ada'
		login()

	tez = requests.get('https://mbasic.facebook.com/profile.php?', headers=headers, cookies=cookies).text
	name = re.search('<head><title>(.*?)</title>', tez).group(1)
	if 'mbasic_logout_button' in tez:
		print '        \nWelcome =', name + '\n'
		print '1. Konfirmasi Permintaan Pertemanan'
		print '2. Hapus Permintaan Pertemanan\n'
	else:
		print '\xc3\x97 Cookies tidak ada'
		login()
	ask = raw_input('+ Pilih ? ')
	print ''
	if ask == '':
		print '\xc3\x97 Masukkan yg benar'
		exit()
	elif ask == '1':
		try:
			total = int(raw_input('+ Jumlah yg ingin anda konfirmasi ? '))
		except:
			print '! Hanya angka yg di perbolehkan'
			exit()

		print ''
		for ju in range(total):
			ju = ju + 1
			try:
				r = requests.get(per, cookies=cookies, headers=headers).text
				html = parser(r, 'html.parser')
				href = html.find('a', string='Konfirmasi', href=True)
				co = requests.get(url + href['href'], headers=headers, cookies=cookies).text
				ou = re.search('friending_list_id=1">(.*?)</a><div class="(.*?)">Permintaan diterima</div>', co)
				name = ou.group(1)
				print '[' + str(ju) + ']', 'Berhasil Konfirmasi', name, '\xe2\x9c\x93'
			except requests.exceptions.ConnectionError:
				print '\xc3\x97 Koneksi bermasalah !'
				exit()

		exit()
	elif ask == '2':
		try:
			total = int(raw_input('+ Jumlah yg ingin anda hapus ? '))
		except:
			print '! Hanya angka yg di perbolehkan'
			exit()

		print ''
		for ju in range(total):
			ju = ju + 1
			try:
				r = requests.get(per, cookies=cookies, headers=headers).text
				html = parser(r, 'html.parser')
				href = html.find('a', string='Hapus Permintaan', href=True)
				co = requests.get(url + href['href'], headers=headers, cookies=cookies).text
				ou = re.search('friending_list_id=1">(.*?)</a><div class="(.*?)">Permintaan dihapus</div>', co)
				name = ou.group(1)
				print '[' + str(ju) + ']', 'Berhasil Menghapus', name, '\xe2\x9c\x93'
			except requests.exceptions.ConnectionError:
				print '\xc3\x97 Koneksi bermasalah !'
				exit()

		exit()
	else:
		print '\xc3\x97 Masukkan yg benar'
		exit()


if __name__ == '__main__':
	menu()
	login()