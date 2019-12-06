from blob.blob_query import insert_blob
from blob.blob_read_write import read_file_blob
from blob.create_table_blob import create_table

if __name__ == "__main__":
    create_table()
    data = read_file_blob("img/python-logo.png")
    print(type(data))

    insert_query = "INSERT INTO images (name, pic) VALUES(%s, %s)"
    update_query = "UPDATE images SET name=%s, pic=%s WHERE no=%S"
    read_query = "SELECT pic FROM images WHERE no = %s"
    delete_query = "delete from images where no = %s"
    select_query = "select no, name from images"

    insert_blob(insert_query, 'python-logo', 'img/python-logo.png')