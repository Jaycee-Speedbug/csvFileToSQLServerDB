rem
rem Easy bat file to launch Python3 console program
rem

echo "//"
echo "// Lance le(s) fichier(s) de tests unitaires test_*.py et redirige les résultats vers le(s) fichiers *.rpt"
echo "//"

python test_WildLifeMap.py > test_WildLifeMap.rpt

echo "//"
echo "//"

pause
