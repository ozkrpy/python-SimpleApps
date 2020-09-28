cd /oracle/csv_generados/dwh/repgi
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-dwh-repgi.out 2>&1 &
cd /oracle/csv_generados/dwh/dbadmin
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-dwh-dbadmin.out 2>&1 &
cd /oracle/csv_generados/dwh/reportes
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-dwh-reportes.out 2>&1 &
cd /oracle/csv_generados/dwh/edata
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-dwh-edata.out 2>&1 &
cd /oracle/csv_generados/dwh/widget
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-dwh-widget.out 2>&1 &
cd /oracle/csv_generados/dwh/bimobile
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-dwh-bimobile.out 2>&1 &
cd /oracle/csv_generados/dwh/kdd
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-dwh-kdd.out 2>&1 &
cd /oracle/csv_generados/dwh/staging
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-dwh-staging.out 2>&1 &
cd /oracle/csv_generados/dwh/mapas
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-dwh-mapas.out 2>&1 &
cd /oracle/csv_generados/dwh/dwh
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-dwh-dwh.out 2>&1 &
cd /oracle/csv_generados/dwh/kdd_staging
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-dwh-kdd_staging.out 2>&1 &
cd /oracle/csv_generados/dwh/segmentador
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-dwh-segmentador.out 2>&1 &
cd /oracle/csv_generados/kml/camaleon
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-kml-camaleon.out 2>&1 &
cd /oracle/csv_generados/kml/dwh
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-kml-dwh.out 2>&1 &
cd /oracle/csv_generados/kml/migra
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-kml-migra.out 2>&1 &
cd /oracle/csv_generados/kml/traspaso
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-kml-traspaso.out 2>&1 &
cd /oracle/csv_generados/kml/falcon
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-kml-falcon.out 2>&1 &
cd /oracle/csv_generados/kml/reportes
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-kml-reportes.out 2>&1 &
cd /oracle/csv_generados/kml/dbreglas2
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-kml-dbreglas2.out 2>&1 &
cd /oracle/csv_generados/kml/factura
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-kml-factura.out 2>&1 &
cd /oracle/csv_generados/kml/dbreglas
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-kml-dbreglas.out 2>&1 &
cd /oracle/csv_generados/kml/dbadmin
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-kml-dbadmin.out 2>&1 &
cd /oracle/csv_generados/kmlhis/traspaso
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-kmlhis-traspaso.out 2>&1 &
cd /oracle/csv_generados/kmlhis/cpp
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-kmlhis-cpp.out 2>&1 &
cd /oracle/csv_generados/kmlhis/reportes
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-kmlhis-reportes.out 2>&1 &
cd /oracle/csv_generados/kmlhis/dbadmin
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-kmlhis-dbadmin.out 2>&1 &
cd /oracle/csv_generados/repgi/edata
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-repgi-edata.out 2>&1 &
cd /oracle/csv_generados/repgi/staging
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-repgi-staging.out 2>&1 &
cd /oracle/csv_generados/repgi/mstr_oracle
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-repgi-mstr_oracle.out 2>&1 &
cd /oracle/csv_generados/repgi/ods
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-repgi-ods.out 2>&1 &
cd /oracle/csv_generados/repgi/repgi
echo $(pwd)
find . -name '*.csv' | xargs wc -l > /home/oracle11/contador_archivos_csv/contador-archivos-repgi-repgi.out 2>&1 &
