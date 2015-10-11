#!/bin/bash
gnome-terminal -e "python ~/PycharmProjects/RSOI_KURS/Src/backends/worker_server/worker_server.py" &
gnome-terminal -e "python ~/PycharmProjects/RSOI_KURS/Src/backends/users_server/users_server.py" &
gnome-terminal -e "python ~/PycharmProjects/RSOI_KURS/Src/backends/comments_server/comments_server.py" &
gnome-terminal -e "python ~/PycharmProjects/RSOI_KURS/Src/backends/admin_server/admin_server.py" &
