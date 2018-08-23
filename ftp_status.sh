#!/bin/bash
# This script tests the FTP login status
# Author Harkamal  Dadwal - Groundswell Group
# Dated 10 - 7 - 12
#
NOW=$(date +"%m-%d-%Y %H:%M:%S")
while read line
do
        echo $line | grep -q '#'

         if [ $? -eq 0 ]; then
                continue
        else

                HOST=`echo $line | cut -d" " -f1`
                #echo " host is: ${HOST}"
                USER=`echo $line | cut -d" " -f2`
                #echo " User name is: ${USER}"
                PASSWD=`echo $line | cut -d" " -f3`
                #echo " Password is: ${PASSWD}"
                OUTPUT=`ftp -nv $HOST << EOB
                user $USER $PASSWD
                EOB`

                echo $OUTPUT | grep -iq 'User logged in'

                if [ $? -eq 0 ]; then
                        echo "${NOW} FTP Login Successfull for ${USER} on ${HOST} >"
                        else
                        echo "${NOW} FTP Login Failed for ${USER} on ${HOST} >"
                fi
        fi
done < ftp_config

