#Palindrome Text
import sys,subprocess
while True:
 n=input("Enter a text ==> ")
 print("")
 print("The palindrome of",n,"is...\n")
 print(" ",n[::-1])
 print("")
 input("Press enter to continue...")
 subprocess.run("cls",shell=True)
