#!/bin/bash

:>ftp_mail.txt

./ftp_status.sh 2>/dev/null > ftp_out.txt

  while read line

  do
         echo $line | grep -qi 'Failed'

                 if [ $? -eq 0 ]; then
                        echo $line >> ftp_mail.txt
                 else
                         continue
                 fi

  done < ftp_out.txt

if [ -s ftp_mail.txt ]; then

# Note: Need to confirm weather to keep log of file ftp failure status.
        cat ftp_mail.txt | mail -s "about to fill" "waiting for rodney to provide"

fi
