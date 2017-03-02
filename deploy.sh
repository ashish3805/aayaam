 
ssh ubuntu@aayaam.sgsits.ac.in <<EOF
  cd /var/www/aayaam.sgsits.ac.in/public_html
  sudo git pull
  cd /var/www/aayaam.sgsits.ac.in/public_html/events/sheetFetch/
  sudo python /var/www/aayaam.sgsits.ac.in/public_html/events/sheetFetch/quickstart.py
  exit
EOF
