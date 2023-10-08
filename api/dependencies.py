from config import STORAGE_PATH
from db.repositories import FileStorageRepository


def get_file_repository() -> FileStorageRepository:
    return FileStorageRepository(storage_path=STORAGE_PATH)
