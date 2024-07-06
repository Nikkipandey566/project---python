#class ExcelChartGenerator:
def __init(self, master, credentials):
    self.master = master
    #self.master.title("Excel Chart Generator")
    #self.data = None
    #self.credentials = credentials
    self.login()

def login(self):
    self.login_window = tk.Toplevel(self.master)
    self.login_window.title("Login")
    self.label = tk.Label(self.login_window, text="Please enter your credentials:")
    self.label.pack()
    self.username_label = tk.Label(self.login_window, text="Username:")
    self.username_label.pack()
    self.username_entry = tk.Entry(self.login_window)
    self.username_entry.pack()

    self.password_label = tk.Label(self.login_window, text="Password:")
    self.password_label.pack()
    self.password_entry = tk.Entry(self.login_window, show="*")
    self.password_entry.pack()

    self.login_button = tk.Button(self.login_window, text="Login",
    command=self.check_login)
    self.login_button.pack()

def check_login(self):
    entered_username = self.username_entry.get()
    entered_password = self.password_entry.get()

#if self.credentials.get(entered_username) == entered_password:
    messagebox.showinfo("Login Successful", "Login successful!")
    self.login_window.destroy()
    self.setup_ui()
#else:
    messagebox.showerror("Login Failed", "Invalid username or password")


def setup_ui(self):
    self.label = tk.Label(self.master, text="Click the button to load Excel data and generate a chart:")
    self.label.pack()
    self.load_excel_button = tk.Button(self.master, text="Load Excel File", command=self.load_excel_file)
    self.load_excel_button.pack()
    self.generate_chart_button = tk.Button(self.master, text="Generate Chart", command=self.generate_chart, state=tk.DISABLED)
    self.generate_chart_button.pack()


def load_excel_file(self):
    file_path = filedialog.askopenfilename(title="Select Excel File",
    filetypes=[("Excel files", "*.xlsx;*.xls")])
    if file_path:
        try:
            self.data = pd.read_excel(file_path)
            self.generate_chart_button["state"] = tk.NORMAL
            messagebox.showinfo("File Loaded", f"Excel file loaded: {file_path}")
        except Exception as e:
                messagebox.showerror("Error", f"Error loading Excel file: {e}")

def generate_chart(self):
    if self.data is not None:
        categories = self.data['Category']
        values = self.data['Values']
        plt.clf()
        plt.bar(categories, values)
        plt.xlabel('Categories')


        plt.ylabel('Values')
        plt.title('Excel Data Bar Chart')
        canvas = FigureCanvasTkAgg(plt.gcf(), master=self.master)
        canvas.draw()
        canvas.get_tk_widget().pack()


        plt.show(block=False)
    else:
        messagebox.showinfo("Generate Chart", "No Excel data loaded. Please load an Excel file first.")

def main():
    Define_your_login_credentials_credentials = {"Niveditha.P": "nive@123", "Nikki Pandey": "nikki@123", "Suraiya Naaz": "suraiya@123", "Pavithra Gouda": "pavi@123"}
    root = tk.Tk()
    app = ExcelChartGenerator(root, credentials)
    root.mainloop()
    if name	== " main ": main()
