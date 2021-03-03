# coding:utf-8
# Tertusbol Oleh Kang Pacman
# Sepesial Thanks To Khairul Syaban | Nanta XE
# coding=utf-8
import requests,os,sys,re
import datetime,random,json,time,sys
from threading import Thread
reload(sys)
sys.setdefaultencoding('utf8')

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

logo = """                     \033[0;93m ××××××××××××××××××× 
	              \033[0;95m FACEBOOK & AUTHOR    
	            \033[0;97m> \033[0;95mFB.COM/RIZKY.RASATA \033[0;97m<

          \033[0;31m█▀▄ █▀█ ▀█▀     █▀▀ █▀█ █▀▀ █▀▀ █▀▄ █▀█ █▀█ █ █
          █▀▄ █ █  █  ▄▄▄ █▀▀ █▀█ █   █▀▀ █▀▄ █ █ █ █ █▀▄
         \033[0;37m ▀▀  ▀▀▀  ▀      ▀   ▀ ▀ ▀▀▀ ▀▀▀ ▀▀  ▀▀▀ ▀▀▀ ▀ ▀\n"""

def login():
	os.system('clear')
	print logo
	try:
		cookie = raw_input("\033[0;95m   •\033[0;97m Cookie \033[0;91m>\033[0;92m ")
		data = {
		            'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', # don't change this user agent.
			        'referer' : 'https://m.facebook.com/',
			        'host' : 'm.facebook.com',
			        'origin' : 'https://m.facebook.com',
			        'upgrade-insecure-requests' : '1',
			        'accept-language' : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			        'cache-control' : 'max-age=0',
			        'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			        'content-type' : 'text/html; charset=utf-8',
			         'cookie' : cookie }
		coki = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = data)
		cari = re.search('(EAAA\w+)', coki.text)
		hasil = cari.group(1)
		pup = open('coki.log', 'w')
		pup.write(cookie)
		pup.close()
		pip = open('login.txt', 'w')
		pip.write(hasil)
		pip.close()
		print '   \033[0;92m√ Login Berhasil'
		time.sleep(2)
		menu()
	except AttributeError:
		print '   \033[0;91m× Cookie Salah'
		time.sleep(2)
		login()
	except UnboundLocalError:
		print '   \033[0;91m× Cookie Salah'
		time.sleep(2)
		login()
	except requests.exceptions.SSLError:
		os.system('clear')
		print '   \033[0;91m× Koneksi Bermasalah'
		exit()

def menu():
	os.system('clear')
	try:
		toket = open('login.txt','r').read()
	except IOError:
		print '   \033[0;91m× Cookie invalid'
		os.system('rm -rf login.txt && rm -rf coki.log')
		login()
	try:
		o = requests.get('https://graph.facebook.com/me/?access_token='+toket)
		op = json.loads(o.text)
		a = op['name']
	except UnboundLocalError:
		print '   \033[0;91m× Cookie Invalid'
		os.system('rm -rf login.txt && rm -rf coki.log')
		login()
	except KeyError:
		print '   \033[0;91m× Cookie Invalid'
		os.system('rm -rf login.txt && rm -rf coki.log')
		login()
	except requests.exceptions.ConnectionError:
		print '   \033[0;91m× Koneksi Bermasalah !'
		exit()
	print logo
	jalan ('   \033[0;91m• \033[0;97mWELCOME \033[0;93m->\033[0;92m '+a+'\n');time.sleep(0.09)
	print ('   \033[0;93m1 \033[0;92m•\033[0;36m Bot Komen');time.sleep(0.09)
	print ('   \033[0;93m2 \033[0;92m•\033[0;36m Donasi');time.sleep(0.09)
	print ('   \033[0;93m3 \033[0;92m•\033[0;36m Exit\n');time.sleep(0.09)
	pilih_menu()
		
def pilih_menu():
	masok = raw_input('   \033[0;93m•\033[0;95m > \033[0;92m')
	if masok =="":
		print '   \033[0;91m× Isi yg benar'
		pilih_menu()
	elif masok == "1":
		bot_komen()
	elif masok == "2":
		jalan ('\n  \033[0;93m • \033[0;96mAnda Akan Di Arahkan Ke Browser')
		os.system('xdg-open https://saweria.co/Rizky02')
		raw_input('\n\033[0;93m   • \033[0;91mEnter Untuk Kembali ..')
		menu()
	elif masok == "3":
		exit()
	else:
		print '   \033[0;91m× Isi yg benar'
		pilih_menu()
    #cok = requests.get(url + tot['href'], headers=headers, cookies=cookies).text
    
def bot_komen():
	os.system('clear')
	try:
		toket = open('login.txt','r').read()
	except KeyError:
		print '   \033[0;91m× Cookie invalid'
		os.system('rm -rf login.txt && rm -rf coki.log')
		exit()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		k = json.loads(o.text)
		a = k['name']
	except AttributeError:
		print '   \033[0;91m× Cookie invalid'
		os.system('rm -rf login.txt && rm -rf coki.log')
		exit()
	print logo
	print '   \033[0;91m• \033[0;97mWELCOME \033[0;93m->\033[0;92m '+a+'\n'
	print '   \033[0;93m1 \033[0;92m•\033[0;97m Komentar Manual'
	print '   \033[0;93m2 \033[0;92m•\033[0;97m Komentar Kata Lucu'
	print '   \033[0;93m3 \033[0;92m•\033[0;97m Komentar Kata Motivasi'
	print '   \033[0;93m4 \033[0;92m•\033[0;97m Komentar Kata Random'
	print '   \033[0;93m0 \033[0;91m•\033[0;97m Kembali\n'
	pilih_komen()

def pilih_komen():
	coy = raw_input('   \033[0;93m•\033[0;95m > \033[0;92m')
	if coy == "":
		print '   \033[0;91m× Isi yg benar'
		pilih_komen()
	elif coy == "1":
		print '   \033[0;93m• \033[0;95mGunakan Tanda \033[0;93m<>\033[0;95m Untuk Komen Berbeda! '
		komentar = raw_input('   \033[0;93m• \033[0;97mKomentar \033[0;93m>\033[0;92m ')
		kok = komentar
		rando = kok.split("<>")
	elif coy == "2":
		rando = ["Cinta adalah pengorbanan, tapi kalau pengorbanan mulu sih namanya penderitaan.",
		"Bekerjalah seperti tuyul. Nggak kelihatan, nggak perlu pujian, nggak cari perhatian, tapi hasil jelas.",
		"Jika doamu belum terkabul maka bersabar, ingatlah bahwa yang berdoa bukan cuma kamu!",
		"Tertawa bisa jadi obat terbaik. Tapi kalau kamu tertawa tanpa alasan yang jelas, mungkin kamu butuh obat.",
		"Ironi dalam hidup Manusia menciptakan ponsel, ponsel makin pintar Manusia tidak.",
		"Persahabatan itu ibarat kita ngompol di celana, setiap orang dapat melihatnya, tapi hanya Anda yang bisa merasakan kehangatannya.",
		"Ikan bandeng makan kawat orang ganteng numpang lewat",
		"Maksud hati cuma KENTUT, apa daya ampasnya malah NGIKUT"]
	elif coy == "3":
		rando = ["Tidak ada seorang pun yang bisa kembali ke masa lalu dan memulai awal yang baru lagi. Tapi semua orang bisa memulai hari ini dan membuat akhir yang baru.” - Maria Robinson",
		"Tidak ada yang bisa membuatmu merasa rendah diri tanpa seizinmu. - Eleanor Roosevelt",
		"Jangan pernah menyesali sehari dalam hidupmu. Hari-hari baik memberimu kebahagiaan dan hari-hari buruk memberimu pengalaman.",
		"Jangan takut berjalan lambat, takutlah jika hanya berdiri diam.",
		"Waktumu terbatas, jangan habiskan untuk hidup orang lain.” -Steve Jobs",
		"Kesuksesan dan kegagalan sama-sama bagian dari hidup. Keduanya sama-sama sementara.” - Shahrukh Khan",
		"Jika kamu mencari satu orang yang akan mengubah hidupmu, lihatlah di cermin.",
		"Kamu laiknya karya seni. Tidak semua orang akan mengerti dirimu, tetapi orang-orang yang mengerti, tidak akan pernah melupakanmu.",
		"Terkadang kita diuji bukan untuk menunjukkan kelemahan kita, tetapi untuk menemukan kekuatan kita.",
		"Semakin keras kamu bekerja untuk sesuatu, semakin besar perasaanmu saat mencapainya."]
	elif coy == "4":
		rando = ["Tidak ada seorang pun yang bisa kembali ke masa lalu dan memulai awal yang baru lagi. Tapi semua orang bisa memulai hari ini dan membuat akhir yang baru.” - Maria Robinson",
		"Tidak ada yang bisa membuatmu merasa rendah diri tanpa seizinmu. - Eleanor Roosevelt",
		"Jangan pernah menyesali sehari dalam hidupmu. Hari-hari baik memberimu kebahagiaan dan hari-hari buruk memberimu pengalaman.",
		"Jangan takut berjalan lambat, takutlah jika hanya berdiri diam.",
		"Cinta adalah pengorbanan, tapi kalau pengorbanan mulu sih namanya penderitaan.",
		"Bekerjalah seperti tuyul. Nggak kelihatan, nggak perlu pujian, nggak cari perhatian, tapi hasil jelas.",
		"Jika doamu belum terkabul maka bersabar, ingatlah bahwa yang berdoa bukan cuma kamu!",
		"Tertawa bisa jadi obat terbaik. Tapi kalau kamu tertawa tanpa alasan yang jelas, mungkin kamu butuh obat.",
		"Ironi dalam hidup Manusia menciptakan ponsel, ponsel makin pintar Manusia tidak.",
		"Persahabatan itu ibarat kita ngompol di celana, setiap orang dapat melihatnya, tapi hanya Anda yang bisa merasakan kehangatannya.",
		"Ikan bandeng makan kawat orang ganteng numpang lewat",
		"Maksud hati cuma KENTUT, apa daya ampasnya malah NGIKUT",
		"Waktumu terbatas, jangan habiskan untuk hidup orang lain.” -Steve Jobs",
		"Kesuksesan dan kegagalan sama-sama bagian dari hidup. Keduanya sama-sama sementara.” - Shahrukh Khan",
		"Jika kamu mencari satu orang yang akan mengubah hidupmu, lihatlah di cermin.",
		"Kamu laiknya karya seni. Tidak semua orang akan mengerti dirimu, tetapi orang-orang yang mengerti, tidak akan pernah melupakanmu.",
		"Terkadang kita diuji bukan untuk menunjukkan kelemahan kita, tetapi untuk menemukan kekuatan kita.",
		"Semakin keras kamu bekerja untuk sesuatu, semakin besar perasaanmu saat mencapainya.",]
	elif coy == "0":
		menu()
	else:
		print '   \033[0;91m× Isi yg benar'
		pilih_komen()
	
	tol = raw_input('   \033[0;93m•\033[0;97m Unlimited Komentar \033[0;92mY\033[0;97m/\033[0;93mN \033[0;91m>\033[0;92m ')
	if tol == "":
		print '   \033[0;91m× Isi yg benar'
		pilih_komen()
	elif tol == "Y" or tol == "y":
		jumlah = int("1000")
	elif tol == "N" or tol == "n":
		while True:
			try:
				jumlah = int(raw_input('   \033[0;93m•\033[0;97m Jumlah Komentar \033[0;93m>\033[0;92m '))
				break
			except ValueError:
				print '   \033[0;91m× Isi Yg Benar'
	else:
		print '   \033[0;91m× Isi Yg Benar'
		pilih_komen()
	try:
		print '   \033[0;91m•\033[0;96m Minimal 40 Detik'
		delay = int(raw_input('   \033[0;93m• \033[0;97mLambat Komentar \033[0;93m>\033[0;92m '))
		if 40 > delay:
			print '   \033[0;91m× Delay Minimal 40 Detik'
			exit()
	except ValueError:
		print '   \033[0;91m× Isi Yg Benar'
		pilih_komen()
	try:
		url = 'https://mbasic.facebook.com'
		toket = open('login.txt','r').read()
		cookie = open('coki.log','r').read().strip()
		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 'cookie' : cookie}
		cookies = {'Cookie': cookie}
	except KeyError:
		print '   \033[0;91m× Cookie Invalid'
		os.system('rm -rf login.txt && rm -rf coki.log')
		exit()
					
	class Run(Thread):
		def run(self):
			for ju in range(jumlah):
				time.sleep(delay)
				ju = ju + 1
				while True:
					try:
						ling = requests.get(url + '/home.php', headers=headers, cookies=cookies).text
						#cari_id = re.search('groups(.*?)/permalink/(.*?)/', ling)
						cari_id = re.search('fbid=(.*?)&amp;id=(.*?)&amp;', ling)
						id_post = cari_id.group(1)
						nama = cari_id.group(2)
						#bung = requests.get(url+'/'+id_post, headers=headers, cookies=cookies).text
						tag_nama = nama.replace(nama, '@['+nama+':]')
						break
					except requests.exceptions.ConnectionError:
						rap = random.choice(['\033[0;96m','\033[0;93m','\033[0;95m','\033[0;91m','\033[0;92m'])
						print "\r%s   • Menunggu Koneksi .."%(rap),;sys.stdout.flush();time.sleep(1)
						pass
					except:
						pass
				try:
					web = datetime.datetime.now()
					waktu = web.strftime("%H:%M:%S / %d-%m-%Y ")
					hour = web.hour
					if 03 < hour < 06:
					  boy = "Selamat Dini Hari 💜"
					elif 06 <= hour < 11:
					  boy = "Selamat Pagi 💙"
					elif 11 <= hour < 15:
					  boy = "Selamat Siang 💛"
					elif 15 <= hour < 18:
					  boy = "Selamat Sore 💚"
					else:
					  boy = "Selamat Malam 🖤"
					pantun = random.choice(rando)
					pesan = boy+'\n'+tag_nama+'\n'+pantun+'\n'+waktu
					req = requests.post("https://graph.facebook.com/"+(id_post)+"/comments?message="+pesan+"&access_token="+toket)
					bib = json.loads(req.text)
					if 'id' in bib:
						jalan ('\n   \033[0;93m• \033[0;97m[\033[0;94m'+str(ju)+'\033[0;97m]\033[0;92m Berhasil')
						jalan ('   \033[0;93m• \033[0;97mLink Post \033[0;95m>\033[0;92m m.facebook.com/'+id_post)
						jalan ('   \033[0;93m• \033[0;97mKomentar \033[0;95m >\033[0;92m '+pantun[:15]+'xxx')
					elif 'error' in bib:
						jalan ('\n   \033[0;93m• \033[0;97m[\033[0;94m'+str(ju)+'\033[0;97m]\033[0;91m Gagal')
						jalan ('   \033[0;93m• \033[0;97mLink Post \033[0;95m>\033[0;91m m.facebook.com/'+id_post)
						jalan ('   \033[0;93m• \033[0;97mKomentar \033[0;95m >\033[0;91m '+pantun[:15]+'xxx')
				except:
					pass
					
	th = Run()
	th.start()
	th.join()
	raw_input('\n\033[0;93m   • \033[0;91mEnter Untuk Kembali ..')
	bot_komen()
		
if __name__ == '__main__':
	menu()
	login()

# Awokawokawok Ngerekod:v