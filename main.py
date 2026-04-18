class FileManager:
    def __init__(self):
        self.files = {}
        self.folders = {}

    def create_file(self, name, content):
        self.files[name] = content

    def create_folder(self, name):
        self.folders[name] = []

    def delete_file(self, name):
        if name in self.files:
            del self.files[name]
        else:
            raise ValueError("File not found")

    def delete_folder(self, name):
        if name in self.folders:
            del self.folders[name]
        else:
            raise ValueError("Folder not found")

    def add_file_to_folder(self, file_name, folder_name):
        if file_name in self.files and folder_name in self.folders:
            self.folders[folder_name].append(file_name)
        else:
            raise ValueError("File or folder not found")

    def remove_file_from_folder(self, file_name, folder_name):
        if file_name in self.files and folder_name in self.folders:
            if file_name in self.folders[folder_name]:
                self.folders[folder_name].remove(file_name)
            else:
                raise ValueError("File not found in folder")
        else:
            raise ValueError("File or folder not found")

    def get_file_content(self, name):
        if name in self.files:
            return self.files[name]
        else:
            raise ValueError("File not found")

    def get_folder_files(self, name):
        if name in self.folders:
            return self.folders[name]
        else:
            raise ValueError("Folder not found")

    def set_file_permission(self, name, permission):
        if name in self.files:
            self.files[name] = {"content": self.files[name], "permission": permission}
        else:
            raise ValueError("File not found")

    def get_file_permission(self, name):
        if name in self.files:
            if isinstance(self.files[name], dict):
                return self.files[name]["permission"]
            else:
                return "read"
        else:
            raise ValueError("File not found")

class User:
    def __init__(self, name):
        self.name = name
        self.permissions = {}

    def add_permission(self, file_name, permission):
        self.permissions[file_name] = permission

    def get_permission(self, file_name):
        if file_name in self.permissions:
            return self.permissions[file_name]
        else:
            return None

class Permission:
    def __init__(self, name):
        self.name = name

    def check_permission(self, user, file_name):
        if user.get_permission(file_name) == self.name:
            return True
        else:
            return False

class File:
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def get_content(self):
        return self.content

class Folder:
    def __init__(self, name):
        self.name = name
        self.files = []

    def add_file(self, file_name):
        self.files.append(file_name)

    def get_files(self):
        return self.files

file_manager = FileManager()
user = User("user1")
permission = Permission("read")

file_manager.create_file("file1", "content1")
file_manager.create_folder("folder1")
file_manager.add_file_to_folder("file1", "folder1")
file_manager.set_file_permission("file1", "read")
user.add_permission("file1", "read")

print(file_manager.get_file_content("file1"))
print(file_manager.get_folder_files("folder1"))
print(file_manager.get_file_permission("file1"))
print(user.get_permission("file1"))
print(permission.check_permission(user, "file1"))