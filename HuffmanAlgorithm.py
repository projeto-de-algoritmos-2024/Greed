mport tkinter as tk
from tkinter import ttk, messagebox
import heapq
from collections import defaultdict

class HuffmanNode:
    def _init_(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def _lt_(self, other):
        return self.freq < other.freq

class HuffmanViewer:
    def _init_(self, root):
        self.root = root
        self.root.title("Visualizador de Árvore de Huffman")
        self.root.geometry("800x600")
        
        self.input_frame = ttk.Frame(root, padding="10")
        self.input_frame.pack(fill=tk.X)
        
        self.text_label = ttk.Label(self.input_frame, text="Coloque algum texto:")
        self.text_label.pack(side=tk.LEFT)
        
        self.text_input = ttk.Entry(self.input_frame, width=50)
        self.text_input.pack(side=tk.LEFT, padx=5)
        
        self.build_button = ttk.Button(self.input_frame, text="Construir Árvore", command=self.build_tree)
        self.build_button.pack(side=tk.LEFT)
        
        # Canvas for tree visualization
        self.canvas = tk.Canvas(root, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.nodes = []
        self.current_step = 0
        
        # Navigation buttons
        self.nav_frame = ttk.Frame(root, padding="10")
        self.nav_frame.pack(fill=tk.X)
        
        self.prev_button = ttk.Button(self.nav_frame, text="Anterior", command=self.prev_step)
        self.prev_button.pack(side=tk.LEFT, padx=5)
        
        self.next_button = ttk.Button(self.nav_frame, text="Próximo", command=self.next_step)
        self.next_button.pack(side=tk.LEFT)
        
        self.step_label = ttk.Label(self.nav_frame, text="Etapa: 0")
        self.step_label.pack(side=tk.LEFT, padx=20)
    
    def calculate_frequencies(self, text):
        frequencies = defaultdict(int)
        for char in text:
            frequencies[char] += 1
        return frequencies
    
    def build_huffman_tree(self, text):
        self.nodes = []
        frequencies = self.calculate_frequencies(text)
        
        heap = []
        for char, freq in frequencies.items():
            node = HuffmanNode(char, freq)
            heapq.heappush(heap, node)
            self.nodes.append(("leaf", node))
        
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            
            internal = HuffmanNode('*', left.freq + right.freq)
            internal.left = left
            internal.right = right
            
            heapq.heappush(heap, internal)
            self.nodes.append(("internal", internal))
        
        self.current_step = 0
        self.update_visualization()
    
    def build_tree(self):
        text = self.text_input.get()
        if not text:
            messagebox.showerror("Error", "Coloque algum texto")
            return
        
        self.build_huffman_tree(text)
    
    def draw_node(self, node, x, y, dx, dy):
        radius = 25

        self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill='lightblue')
        
        text = f"{node.char}\n{node.freq}"
        self.canvas.create_text(x, y, text=text)
        
        if node.left:
            child_x = x - dx
            child_y = y + dy
            self.canvas.create_line(x, y+radius, child_x, child_y-radius)
            self.draw_node(node.left, child_x, child_y, dx/2, dy)
        
        if node.right:
            child_x = x + dx
            child_y = y + dy
            self.canvas.create_line(x, y+radius, child_x, child_y-radius)
            self.draw_node(node.right, child_x, child_y, dx/2, dy)
    
    def update_visualization(self):
        self.canvas.delete("all")
        if not self.nodes:
            return
        
        current_nodes = self.nodes[:self.current_step + 1]
        if current_nodes:
            final_node = current_nodes[-1][1]
            self.draw_node(final_node, 400, 50, 200, 100)
        
        self.step_label.config(text=f"Step: {self.current_step + 1}/{len(self.nodes)}")
    
    def next_step(self):
        if self.current_step < len(self.nodes) - 1:
            self.current_step += 1
            self.update_visualization()
    
    def prev_step(self):
        if self.current_step > 0:
            self.current_step -= 1
            self.update_visualization()

if _name_ == "_main_":
    root = tk.Tk()
    app = HuffmanViewer(root)
    root.mainloop()
