#Importing a tkinter library for GUI visualization 
import tkinter as tk
from tkinter import simpledialog, messagebox

#Initialize ATM class
class ATM:
    #Starting this init function first
    def __init__(self, master):
        self.master = master
        self.master.title("ATM Machine")
        self.pin = "1234"
        self.balance = 1000.0
        self.transaction_history = []
        
        self.create_widgets()

    # This function for create a User Interface for ATM Machine
    def create_widgets(self):
        self.lbl_welcome = tk.Label(self.master, text="Welcome to ATM Machine", font=("Arial", 18))
        self.lbl_welcome.grid(row=0, columnspan=3, pady=10)
        self.create_main_buttons()
    
    #This function for create a ATM functions Button initialize and operation that functions
    def create_main_buttons(self):
        self.btn_balance = tk.Button(self.master, text="Balance Inquiry", command=self.balance_inquiry, font=("Arial", 12))
        self.btn_balance.grid(row=2, column=0, pady=10, padx=10)

        self.btn_withdraw = tk.Button(self.master, text="Cash Withdrawal", command=self.cash_withdrawal, font=("Arial", 12))
        self.btn_withdraw.grid(row=2, column=1, pady=10, padx=10)

        self.btn_deposit = tk.Button(self.master, text="Cash Deposit", command=self.cash_deposit, font=("Arial", 12))
        self.btn_deposit.grid(row=2, column=2, pady=10, padx=10)

        self.btn_change_pin = tk.Button(self.master, text="Change PIN", command=self.change_pin, font=("Arial", 12))
        self.btn_change_pin.grid(row=3, column=0, pady=10, padx=10)

        self.btn_history = tk.Button(self.master, text="Transaction History", command=self.transaction_history_view, font=("Arial", 12))
        self.btn_history.grid(row=3, column=1, pady=10, padx=10)

        self.btn_exit = tk.Button(self.master, text="Exit", command=self.master.quit, font=("Arial", 12))
        self.btn_exit.grid(row=3, column=2, pady=10, padx=10)

  
    #Check a balance inquiry if pin is correct
    def balance_inquiry(self):
        if self.check_pin_via_popup():
            messagebox.showinfo("Balance Inquiry", f"Your current balance is: ${self.balance:.2f}")
    
    #Enter a cash withdrwal amount if pin is correct
    def cash_withdrawal(self):
        if self.check_pin_via_popup():
            amount = simpledialog.askfloat("Cash Withdrawal", "Enter the amount to withdraw:")
            if amount and amount <= self.balance:
                self.balance -= amount
                self.transaction_history.append(f"Withdrawal: -${amount:.2f}")
                messagebox.showinfo("Cash Withdrawal", f"${amount:.2f} has been withdrawn.")
            elif amount:
                messagebox.showerror("Cash Withdrawal", "Insufficient balance.")
    
    #Enter a cash deposit amount if pin is correct
    def cash_deposit(self):
        if self.check_pin_via_popup():
            amount = simpledialog.askfloat("Cash Deposit", "Enter the amount to deposit:")
            if amount:
                self.balance += amount
                self.transaction_history.append(f"Deposit: +${amount:.2f}")
                messagebox.showinfo("Cash Deposit", f"${amount:.2f} has been deposited.")
    
    #Change a new pin function
    def change_pin(self):
        if self.check_pin_via_popup():
            new_pin = simpledialog.askstring("Change PIN", "Enter your new PIN:", show="*")
            confirm_pin = simpledialog.askstring("Change PIN", "Confirm your new PIN:", show="*")
            if new_pin and new_pin == confirm_pin:
                self.pin = new_pin
                messagebox.showinfo("Change PIN", "PIN successfully changed.")
            elif new_pin:
                messagebox.showerror("Change PIN", "New PIN does not match.")
    
    #List out a transaction history view
    def transaction_history_view(self):
        if self.check_pin_via_popup():
            history = "\n".join(self.transaction_history)
            if history:
                messagebox.showinfo("Transaction History", history)
            else:
                messagebox.showinfo("Transaction History", "No transactions found.")

    #Each functons click before a popup on check a pin verification function
    def check_pin_via_popup(self):
        pin = simpledialog.askstring("PIN Verification", "Enter your PIN:", show="*")
        if pin == self.pin:
            return True
        else:
            messagebox.showerror("PIN Verification", "Incorrect PIN.")
            return False

#Run a main functions
if __name__ == "__main__":
    root = tk.Tk()
    atm = ATM(root)
    root.mainloop()
