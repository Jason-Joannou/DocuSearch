import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog, scrolledtext
from .document_index.index import create_index
from .document_index.index_search import search_index

class LocalSearchEngineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Local Search Engine")

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.index_button = tk.Button(self.frame, text="Index Files", command=self.index_files)
        self.index_button.pack(padx=5, pady=5)

        self.search_button = tk.Button(self.frame, text="Search Files", command=self.perform_search)
        self.search_button.pack(padx=5, pady=5)

        self.result_text = scrolledtext.ScrolledText(self.frame, width=60, height=20)
        self.result_text.pack(padx=5, pady=5)

    def index_files(self):
        directory = filedialog.askdirectory(title="Select Directory to Index")
        if not directory:
            return

        excluded_dirs = simpledialog.askstring("Exclude Directories", "Enter directories to exclude (comma-separated):")
        if excluded_dirs:
            excluded_dirs_list = excluded_dirs.split(',')
        else:
            excluded_dirs_list = []

        included_exts = simpledialog.askstring("Include File Extensions", "Enter file extensions to include (comma-separated):")
        if included_exts:
            included_exts_list = included_exts.split(',')
        else:
            included_exts_list = []

        create_index(directory, excluded_dirs_list, included_exts_list, "indexdir")
        messagebox.showinfo("Indexing Completed", f"Indexing of directory {directory} is completed.")

    def perform_search(self):
        query = simpledialog.askstring("Search", "Enter search query:")
        if not query:
            return

        results = search_index(query, "./indexDir")
        self.result_text.delete('1.0', tk.END)
        if results:
            for title, path in results:
                self.result_text.insert(tk.END, f"Title: {title}, Path: {path}\n")
        else:
            self.result_text.insert(tk.END, "No results found.")

def main():
    root = tk.Tk()
    app = LocalSearchEngineApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()