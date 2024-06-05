#!/bin/bash
echo "START Logstash testauto"
echo "Initialize logstash with input files"
cp -rf /etc/logstash_in/* /etc/logstash/
ls /etc |grep logstash

echo "START Logstash on mock configuration"
/usr/share/logstash/bin/logstash --log.level=info  --path.settings /etc/logstash --config.reload.automatic
echo "END test"