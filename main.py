import tkinter as tk
from tkinter import messagebox
from fcfs import FCFSSchedulerApp
from sjf import SJFSchedulerApp
from rr import RoundRobinSchedulerApp
from pp import PrioritySchedulerApp

class CPUSchedulingMainApp:
    def __init__(self, master):
        self.master = master
        self.master.title("CPU Scheduling")

        self.heading_label = tk.Label(master, text="CPU Scheduling", font=("Helvetica", 16, "bold"))
        self.heading_label.pack(pady=10)

        self.fcfs_button = tk.Button(master, text="FCFS", command=self.run_fcfs)
        self.fcfs_button.pack(pady=10)

        self.sjf_button = tk.Button(master, text="SJF", command=self.run_sjf)
        self.sjf_button.pack(pady=10)

        self.round_robin_button = tk.Button(master, text="Round Robin", command=self.run_rr)
        self.round_robin_button.pack(pady=10)

        self.priority_button = tk.Button(master, text="Priority", command=self.run_pp)
        self.priority_button.pack(pady=10)

    def run_fcfs(self):
        try:
            fcfs_root = tk.Toplevel(self.master)
            fcfs_root.title("FCFS CPU Scheduling")
            fcfs_app = FCFSSchedulerApp(fcfs_root)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def run_sjf(self):
        try:
            sjf_root = tk.Toplevel(self.master)
            sjf_root.title("SJF CPU Scheduling")
            sjf_app = SJFSchedulerApp(sjf_root)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def run_rr(self):
        try:
            round_robin_root = tk.Toplevel(self.master)
            round_robin_root.title("Round Robin CPU Scheduling")
            round_robin_app = RoundRobinSchedulerApp(round_robin_root)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def run_pp(self):
        try:
            priority_root = tk.Toplevel(self.master)
            priority_root.title("Priority Scheduling CPU")
            priority_app = PrioritySchedulerApp(priority_root)
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = CPUSchedulingMainApp(root)
    root.mainloop()
