MAX_CONNECTIONS = 30
CHARSET = 'utf8mb4'
CONNECT_TIMEOUT = 30

# Mysql 命令
SQL_DROP_TABLE = 'DROP TABLE IF EXISTS `{table}`'
SQL_SHOW_TABLES = 'SHOW TABLES LIKE "{table}"'
SQL_CREATE_TABLE = ('CREATE TABLE IF NOT EXISTS `{table}` ('
                    '`_id` bigint NOT NULL AUTO_INCREMENT, '
                    '`_sn` varchar(64) NOT NULL, '
                    '`_order` bigint NOT NULL, `_keywords` text NOT NULL, '
                    '`_created_by` bigint NOT NULL, '
                    '`_created_date` bigint NOT NULL, '
                    'PRIMARY KEY (`_id`) ) ENGINE=InnoDB DEFAULT CHARACTER SET=utf8 COLLATE=utf8_unicode_ci')

SQL_ALTER_TABLE_AUTO_INCREMENT = 'ALTER TABLE {table} AUTO_INCREMENT = {start}'
