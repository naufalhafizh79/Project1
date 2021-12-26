
import os
from os import system


#	AWAL

def Operasi_Komparasi():

	os.system ('cls')

	print ("Selamat Datang Di Operasi Komparasi ,, Silahkan Pilih Salah Satu")
	print ("1. A Lebih Kecil Dari B")
	print ("2. A Lebih Besar Dari B")
	print ("3. A Sama Dengan B")
	print ("4. A Tidak Sama Dengan B")
	print ("99. Beranda")

	inputt = str(input(" =====> "))

	if inputt == '1':

		os.system ('cls')

		print ("Lebih Kecil Dari \n")
		a = int(input("Masukan Nilai A : "))
		b = int (input("Masukan Nilai B : "))
		print ("\n")
		hasil = a < b
		print ("Nilai A = " , a )
		print ("Nilai B = " , b )
		print ("______________________________________\n")

		print ( "Apakah" , a , "lebih kecil dari" , b , " ? : " , hasil )


	elif inputt == '2':

		os.system ('cls')

		print ("Lebih Besar Dari \n")
		a = int(input("Masukan Nilai A : "))
		b = int (input("Masukan Nilai B : "))
		print ("\n")
		hasil = a > b
		print ("Nilai A = " , a )
		print ("Nilai B = " , b , "\n")
		print ("______________________________________\n")

		print ( "Apakah" , a , "lebih Besar dari" , b , " ? : " , hasil )

	elif inputt == '3':

		os.system ('cls')

		print ("Sama Dengan Dari \n")
		a = int(input("Masukan Nilai A : "))
		b = int(input("Masukan Nilai B : "))
		print ("\n")
		hasil = a == b
		print ("Nilai A = " , a )
		print ("Nilai B = " , b , "\n")
		print ("______________________________________\n")

		print ( "Apakah " , a , " Sama Dengan " , b , " ? : " , hasil )

	elif inputt == '4':

		os.system ('cls')

		print ("Tidak Sama Dengan")
		a = int(input("Masukan Nilai A : "))
		b = int(input("Masukan Nilai B : "))
		print("\n")
		hasil = a != b
		print ("Nilai A = " , a )
		print ("Nilai B = " , b , "\n")
		print ("______________________________________\n")

		print ( "Apakah " , a , " Tidak Sama Dengan " , b , " ? : " , hasil )


	elif inputt == 99:
		Beranda()
		os.system ('cls')

	else:
		print ("Pilihan Anda Tidak Ada Dalam menu !!!")
  


	inputt = str(input("Lagi ?  Y / N  : "))



	if inputt == 'Y' :
		Operasi_Komparasi()

	if inputt == 'y' :
		Operasi_Komparasi()

	else :
		Beranda()



















def Beranda():
	os.system('cls')
	Beranda = True
	while Beranda == True :


	
		print ("""

		_________________________________________________  
		_________________________________________________
		,--.   ,--.     ,--,--.                           
		|  |   |  |,---.|  |  |,---.,---.,--,--,--.,---.  
		|  |.'.|  | .-. |  |  | .--| .-. |        | .-. : 
		|   ,'.   \   --|  |  \ `--' '-' |  |  |  \   --. 
		'--'   '--'`----`--`--'`---'`---'`--`--`--'`----' 
		_________________________________________________   

		Pilih Salah Satu Dibawah Ini :
		1. Operasi Komparasi
		2.
		3.
		4.
		5.
		6.
		7.
		8.
		9.
		10. Restart
		11. Exit
		""")


		Pilihan_Beranda = str(input("======> "))
		
		


		if Pilihan_Beranda == '1':
			Operasi_Komparasi()



		if Pilihan_Beranda == '10':
			os.system('cls')
			os.system('python Projek.py')
			
		elif Pilihan_Beranda == '11':
			print ("Keluar")
			os.system ('cls')
			Beranda = False
			exit()

		else:
			print ("Pilihan Anda Tidak Ada Di Dalam Menu !!!")
			













menu = True



while menu == True :
	os.system('cls')


	print ("""
                                  
		,--.  ,--.        ,--.,--.        
		|  '--'  | ,--,--.|  ||  | ,---.  
		|  .--.  |' ,-.  ||  ||  || .-. | 
		|  |  |  |\ '-'  ||  ||  |' '-' ' 
		`--'  `--' `--`--'`--'`--' `---'  
		                  

		                Play ? Y/N                
	""")
	
	menu = str(input("	------> "))

	if menu == 'Y' :
		Beranda()

	elif menu == 'y' :
		Beranda()

	else:
		menu = False



