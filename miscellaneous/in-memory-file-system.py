from typing import List

# design an in-memory file system

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_file = False
        self.content = ""


class FileSystem(object):
    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        cur_node = self.get_node(path)

        if cur_node.is_file:
            # return the very last element in the dictionary, which is the file
            return [self.split_path(path, '/')[-1]]

        return sorted(cur_node.children.keys())

    def mkdir(self, path: str) -> None:
        cur_node = self.put_node(path)
        cur_node.is_file = False

    def addContentToFile(self, filePath: str, content: str) -> None:
        cur_node = self.put_node(filePath)
        cur_node.is_file = True
        # append content to the end of the file
        cur_node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.get_node(filePath).content

    def get_node(self, path: str) -> TrieNode:
        cur_node = self.root

        for elem in self.split_path(path, '/'):
            cur_node = cur_node.children[elem]
        
        return cur_node

    def put_node(self, path: str) -> TrieNode:
        cur_node = self.root

        for p in self.split_path(path, "/"):
            if p not in cur_node.children:
                cur_node.children[p] = TrieNode()
            cur_node = cur_node.children[p]
        
        return cur_node
    
    def split_path(self, path: str, delimiter) -> List[str]:
        if path == delimiter:
            return []

        return path.split(delimiter)[1:]

if __name__ == "__main__":
    fs = FileSystem()
    print(fs.ls('/'))

    fs.mkdir('/a/b/c')
    print(fs.ls('/a/b'))