SET VERIFY OFF
SET HEADING OFF
SET FEEDBACK OFF
SET AUTOTRACE OFF
SET LINESIZE 32767
SET PAGESIZE 0
SET TAB ON
SET TERM OFF
SET TRIMSPOOL ON
SET TIME ON
SET SERVEROUTPUT ON
SET DEFINE ON
SET ESCCHAR $ 
SET ARRAY 5000

ALTER SESSION SET NLS_DATE_FORMAT = "DD/MM/YYYY HH24:MI:SS"
/
--spool /oracle/TratamientoPuntuales/Puntual-kmlresh-dbadmin.sql
spool Puntual-kmlresh-errores.sql
/
DECLARE
    nombre_db VARCHAR(32767) := 'kmlresh';
    cadena_columnas VARCHAR(32767);
    cadena_select VARCHAR(32767);
    contador NUMBER;
    query_conteo VARCHAR(32767);
    listado_tablas CLOB;
    v_buff VARCHAR(32767);
    
    output_spool_tabla VARCHAR(32767) := '';
    select_spool_columnas VARCHAR(32767) := '';
    select_spool_datos VARCHAR(32767) := '';
    tipo_dato_blob VARCHAR(100) := '''(BLOB)'''; 

    CURSOR tablas IS 
        SELECT t.owner, t.table_name
        FROM all_tables t
        WHERE t.owner in ('DBADMIN')
        AND t.table_name in (
            'LLAMADAS_TAS_1106','IN_TAS_LLAM_TARIFAS_PRE_1109','IN_TAS_LLAMADAS_PRE_2014','IN_TAS_LLAM_TARIFAS_PRE_1501','IN_TAS_LLAM_SERVICIOS_PRE_2014','IN_TAS_LLAM_TARIFAS_PRE_1502','MENSAJES_TAS_SERVICIOS_2012','LLAMADAS_TAS_1308','LLAMADAS_TAS_0809','IN_TAS_LLAM_SERVICIOS_PRE_2013','IN_TAS_LLAM_TARIFAS_PRE_1107','GPRS_HOTBILLING_1501','IN_TAS_LLAM_SERVICIOS_PRE_2012','GPRS_HOTBILLING_1512','IN_TAS_LLAM_TARIFAS_PRE_1110','LLAMADAS_TAS_1005','IN_TAS_LLAM_SERVICIOS_PRE_2011','IN_TAS_LLAMADAS_PRE_2012','LLAMADAS_TAS_0903','GPRS_HOTBILLING_1510','IN_TAS_LLAMADAS_PRE_2013','GPRS_HOTBILLING_1511','IN_TAS_LLAM_TARIFAS_PRE_1111','LLAMADAS_TAS_0806','IN_TAS_LLAM_TARIFAS_PRE_1112','DATOS_TAS_SERVICIOS_2013','IN_TAS_LLAM_TARIFAS_PRE_1108','IN_TAS_LLAM_TARIFAS_PRE_1106','MENSAJES_TAS_SERVICIOS_2013'
            --'FCT_TRAFICO_2016_04'
        ) 
        ORDER BY t.table_name;
    
BEGIN

    FOR tabla IN tablas
    LOOP
        cadena_columnas := '';
        cadena_select := '';
        contador := 0;        

        FOR columna IN (SELECT c.column_name, c.data_type FROM all_tab_cols c WHERE owner = tabla.owner and table_name = tabla.table_name)
        LOOP
            cadena_columnas := cadena_columnas || '|' || columna.column_name ;
            -- cadena_select := '**';    
            -- cadena_select := cadena_select || ',' || columna.column_name;    
            -- cadena_select := cadena_select || ', replace(' || columna.column_name || ', chr(10), '' '')';
            if ((columna.data_type='VARCHAR2') OR (columna.data_type='NVARCHAR2')) then
                cadena_select := cadena_select || '||''|''||replace(' || columna.column_name || ', chr(10), '' '')';
                -- cadena_select := cadena_select || ', replace(' || columna.column_name || ', chr(10), '' '')';
            -- elsif ((columna.data_type='BLOB') OR (columna.data_type='CLOB')) then
            --     cadena_select := cadena_select || '||''|''||' || tipo_dato_blob;
            --     cadena_select := cadena_select || ',' || columna.column_name;
            else
                cadena_select := cadena_select || '||''|''||' || columna.column_name; 
                -- cadena_select := cadena_select || ',' || columna.column_name;
            end if;
        END LOOP;
        cadena_columnas := substr(cadena_columnas, 2);
        cadena_select := substr(cadena_select, 8);
        -- cadena_select := substr(cadena_select, 2);
        
        output_spool_tabla := lower('spool /oracle2/csv_generados/'||nombre_db||'/'||tabla.owner||'/'||nombre_db||'-'||tabla.owner||'.'||tabla.table_name||'.csv');
        select_spool_columnas := 'select ''' || cadena_columnas || '''' || chr(10) ||  '  from dual';
        select_spool_datos := 'select /*+ PARALLEL(' || tabla.owner  || '.' || tabla.table_name || ',4)*/ ' || cadena_select || chr(10) || '  from ' || tabla.owner  || '.' || tabla.table_name;
        
        dbms_output.put_line(output_spool_tabla);
        dbms_output.put_line('/');
        dbms_output.put_line(select_spool_columnas);
        dbms_output.put_line('/');
        dbms_output.put_line(select_spool_datos);
        dbms_output.put_line('/' || chr(10) || chr(10));
    
    END LOOP;
    
EXCEPTION
    WHEN OTHERS THEN
        dbms_output.put_line('ERROR: ' || SQLERRM);
END;
/
spool off
/
EXIT
EOFEOF
