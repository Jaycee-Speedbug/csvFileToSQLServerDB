rem
rem Easy bat file to launch Python3 console program
rem

cls

echo "//"
echo "// Lance le(s) fichier(s) de tests unitaires test_*.py et redirige les résultats vers le(s) fichiers *.rpt"
echo "//"

python WildLife\test_WildLifeMap.py > WildLife\test_WildLifeMap.rpt

python DatabaseConnect\test_SQLServerConnector.py > DatabaseConnect\test_SQLServerConnector.rpt

echo "//"
echo "//"

pause
