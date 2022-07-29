#install dependincies first
pip install -r ./pyDepends.txt
#might need to include node...
clear
#run program to convert py to exe
#https://datatofish.com/executable-pyinstaller/
pyinstaller --onefile ./index.py
clear
#run exe
./dist/index

#open in webbrowser.
firefox --private ./index.html