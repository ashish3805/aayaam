#!/bin/sh
 
ssh ubuntu@aayaam.sgsits.ac.in <<EOF
  cd /var/www/aayaam.sgsits.ac.in/public_html
  sudo git pull
  exit
EOF
