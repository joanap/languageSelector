#!/bin/bash
# -*- coding: utf-8 -*-

ARRAY=(pt en es it fr)

for i in ${ARRAY[*]}
do
    echo "Normalize $i"
    normalize=NOR.txt
    python normalize.py $i/$i.txt $i/$i$normalize

    echo "Bigram count $i"
    python nGramCount.py $i/$i$normalize 2 $i/$i.bigrama

    echo "Trigram count $i"
    python nGramCount.py $i/$i$normalize 3 $i/$i.trigrama
    echo "###############################"
done


# Frase 1
echo "Identifying language of Sentence 1"
python calcLang.py "Per tutta la campagna, Dilma ha promesso forti cambiamenti per venire incontro al malcontento scoppiato nella seconda metà del suo mandato, ma offrendo pochi dettagli." > Resultado.txt
echo "###########################################" >> Resultado.txt

# Frase 2
echo "Identifying language of Sentence 2"
python calcLang.py "La presidenta brasileña, Dilma Rousseff, ha ganado la segunda vuelta electoral celebrada este domingo con un 51,64% de los votos, frente al 48,55% del socialdemócrata Aécio Neves, según datos del Tribunal Superior Electoral con un 99,99% del censo escrutado en unas elecciones que el presidente del Supremo Tribunal Federal (STF), Ricardo Lewandowski, ha calificado como \"una verdadera fuesta de la democracia\"." >> Resultado.txt
echo "###########################################" >> Resultado.txt

# Frase 3
echo "Identifying language of Sentence 3"
python calcLang.py "Marcelo Rebelo de Sousa reagiu neste domingo às críticas que o primeiro-ministro fez no sábado aos comentadores políticos e aos jornalistas, acusando-os de serem “preguiçosos” e “patéticos”." >> Resultado.txt
