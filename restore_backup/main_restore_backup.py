from restore_backup.backup_restore import BackupRestore

if __name__ == "__main__":
    backup_restore = BackupRestore()
    # backup_restore.data_backup('product')
    # backup_restore.data_backup('sale')
    backup_restore.data_restore('product')
    backup_restore.data_restore('sale')
