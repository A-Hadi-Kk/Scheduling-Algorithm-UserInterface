import tkinter as tk
from tkinter import messagebox

class Process:
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

class RoundRobinSchedulerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Round Robin CPU Scheduling")

        self.num_processes_label = tk.Label(master, text="Enter the number of processes:")
        self.num_processes_label.pack()

        self.num_processes_entry = tk.Entry(master)
        self.num_processes_entry.pack()

        self.quantum_label = tk.Label(master, text="Enter time quantum for Round Robin:")
        self.quantum_label.pack()

        self.quantum_entry = tk.Entry(master)
        self.quantum_entry.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.submit)
        self.submit_button.pack()

    def submit(self):
        try:
            num_processes = int(self.num_processes_entry.get())
            quantum = int(self.quantum_entry.get())
            self.show_process_input_window(num_processes, quantum)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

    def show_process_input_window(self, num_processes, quantum):
        process_input_window = tk.Toplevel(self.master)
        process_input_window.title("Enter Process Information")

        self.process_entries = []

        for i in range(1, num_processes + 1):
            label = tk.Label(process_input_window, text=f"Process P{i} Information:")
            label.pack()

            arrival_label = tk.Label(process_input_window, text="Arrival Time:")
            arrival_label.pack()

            arrival_entry = tk.Entry(process_input_window)
            arrival_entry.pack()

            burst_label = tk.Label(process_input_window, text="Burst Time:")
            burst_label.pack()

            burst_entry = tk.Entry(process_input_window)
            burst_entry.pack()

            self.process_entries.append((arrival_entry, burst_entry))

        submit_button = tk.Button(process_input_window, text="Submit", command=lambda: self.run_round_robin_scheduling(num_processes, quantum))
        submit_button.pack()

    def run_round_robin_scheduling(self, num_processes, quantum):
        processes = []

        for i in range(num_processes):
            arrival_time = int(self.process_entries[i][0].get())
            burst_time = int(self.process_entries[i][1].get())
            processes.append(Process(i + 1, arrival_time, burst_time))

        self.round_robin_scheduling(processes, quantum)
        self.show_gantt_chart_and_statistics("Round Robin Scheduling", processes)

    def round_robin_scheduling(self, processes, quantum):
        queue = processes.copy()
        current_time = 0

        while queue:
            process = queue.pop(0)
            if process.arrival_time > current_time:
                current_time = process.arrival_time

            if process.remaining_time <= quantum:
                process_time = process.remaining_time
            else:
                process_time = quantum
                queue.append(process)

            process.remaining_time -= process_time
            current_time += process_time

            if process.remaining_time == 0:
                process.completion_time = current_time
                process.turnaround_time = process.completion_time - process.arrival_time
                process.waiting_time = process.turnaround_time - process.burst_time
                processes.append(process)

        for process in processes:
            process.remaining_time = process.burst_time

    def show_gantt_chart_and_statistics(self, title, processes):
        result_window = tk.Toplevel(self.master)
        result_window.title(title)

        self.draw_gantt_chart(processes, result_window)

        statistics_text = self.generate_statistics_text(processes)
        statistics_label = tk.Label(result_window, text=statistics_text)
        statistics_label.pack()

    def draw_gantt_chart(self, processes, window):
        gantt_chart = []
        current_time = 0

        for process in processes:
            gantt_chart.append((current_time, process.process_id))
            current_time = process.completion_time

        gantt_chart.append((current_time, "End"))

        gantt_label = tk.Label(window, text="Gantt Chart:")
        gantt_label.pack()

        for start, process_id in gantt_chart:
            label = tk.Label(window, text=f"| P{process_id} ", relief="solid")
            label.pack(side=tk.LEFT)

        for start, process_id in gantt_chart:
            label = tk.Label(window, text=f"{start:^10}", relief="solid")
            label.pack(side=tk.LEFT)

    def generate_statistics_text(self, processes):
        statistics_text = ""

        if not processes:
            statistics_text += "No processes to calculate statistics."
            return statistics_text

        total_turnaround_time = 0
        total_waiting_time = 0
        total_processes = len(processes)

        for process in processes:
            total_turnaround_time += max(0, process.turnaround_time)
            total_waiting_time += max(0, process.waiting_time)

            statistics_text += f"Process P{process.process_id}:\n"
            statistics_text += f"  Arrival Time: {process.arrival_time}\n"
            statistics_text += f"  Burst Time: {process.burst_time}\n"
            statistics_text += f"  Turnaround Time: {max(0, process.turnaround_time)}\n"
            statistics_text += f"  Waiting Time: {max(0, process.waiting_time)}\n\n"

        average_turnaround_time = total_turnaround_time / total_processes
        average_waiting_time = total_waiting_time / total_processes

        statistics_text += f"Average Turnaround Time: {average_turnaround_time}\n"
        statistics_text += f"Average Waiting Time: {average_waiting_time}"

        return statistics_text

if __name__ == "__main__":
    root = tk.Tk()
    app = RoundRobinSchedulerApp(root)
    root.mainloop()
