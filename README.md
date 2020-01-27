# Тестове для Kness
## перше завданя:
1) ставим python 3.7 (він асинхронний з коробки)  
2) ставим pip
3) качаєм цей говнокод
4) виконуєм командо: 
    1) (for linux) python3.7 - m pip install -r requirements.txt
    2) (for масдайки) pip install -r requirements.txt
5) еспортуєм данні з файлу командою:
     python manage.py fromcsvtodb filecsv filename name_table_in_db


## 2ге завдання:
1) ставим python 3.7 (він асинхронний з коробки)  
2) ставим pip
3) качаєм цей говнокод
4) виконуєм командо: 
    1) (for linux) python3.7 - m pip install -r requirements.txt
    2) (for масдайки) pip install -r requirements.txt
5) запускаєм сервер командою (до речі, посилання на Ваше потокове відео не працює):
     1) (for linux) python3.7 proba_rtcp.py
     2) (масдайка) python proba_rtcp.py
     3) насолоджуємся гарним вікном з потоковим відео
 6) запускаєм сервер http: 
    1) переходим в течко browser_rtcp
    2) там виконуєм команду:
        1) (ліня) python3.7 manage.py runserver
        2) (вінда) manage.py runserver
    3) вбиваєм в командний рядок бровзера:
        1) (лінукс і віндовс і макось, пофік, бо це бровзер): http://127.0.0.1:8000/ і насолоджуємось, як кожні 5 хв міняється наша кортинка.