#!/bin/bash
python fetcher_app.py
P1=$!
hypercorn background_process:asgi_app &
P2=$!
wait $P1 $P2