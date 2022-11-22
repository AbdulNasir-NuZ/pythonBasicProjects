from tkinter import *
from tkinter import ttk
from datetime import datetime
import requests
from tkinter import messagebox

root = Tk()
root.geometry("600x270")
root.title("Currency Converter -@coder.buzz")
root.resizable(0,0)

def show_data():
        amount = E1.get()
        from_currency  = c1.get()
        to_currency = c2.get()
        url =  'http://api.currencylayer.com/live?access_key=4273d2c37f738367f08780b934ce7dda&format=1'
        
        if amount == '':
               messagebox.showerror("Currency Converter", "Please Fill the Amount") 
        elif to_currency == '':
                messagebox.showerror("Currency Converter", "Please Choose the Currency") 
        
        else:
                data = requests.get(url).json() 
                currency = from_currency.strip()+to_currency.strip()
                amount = int(amount)
                cc = data['quotes'][currency]
                cur_conv = cc*amount
                E2.insert(0,cur_conv)

                text.insert('end',f'{amount} United State Dollar Equals {cur_conv} {to_currency} \n\n Last Time Update --- \t {datetime.now()}')
                
def clear():
        E1.delete(0,'end')
        E2.delete(0,'end')
        text.delete(1.0,'end')        
               

Label(root,text="Currency Converter", font=('verdana','10','bold')).place(x=200,y=15)
Label(root,text="Amount",font=('roboto',10,'bold')).place(x=20,y=15)

E1 = ttk.Entry(root,width=20,font=('roboto',10,'bold'))
E1.place(x=20,y=40)

c1 = StringVar() 
c2 = StringVar() 
currencychoose1 = ttk.Combobox(root, width = 20, textvariable = c1,font=('verdana',10,'bold')) 
  
# Adding combobox drop down list 
currencychoose1['values'] = ('USD') 

currencychoose1.place(x=300,y=40)
currencychoose1.current(0) 



E2 = ttk.Entry(root,width=20,font=('roboto',10,'bold'))
E2.place(x=20,y=80)


currencychoose2 = ttk.Combobox(root, width = 20, textvariable = c2, state='readonly',font=('verdana','10','bold')) 
  
# Adding combobox drop down list 
currencychoose2['values'] =('ALL',  
                          ' AFN', 
                          ' ARS', 
                          ' AWG', 
                          ' AUD', 
                          ' AZN', 
                          ' BSD', 
                          ' BBD', 
                          ' BYN', 
                          ' BZD	', 
                          ' BMD', 
                          ' BOB',
                          'BAM',  
                          ' BWP', 
                          ' BGN', 
                          ' BND', 
                          ' KHR', 
                          ' CAD', 
                          ' KYD', 
                          ' CLP', 
                          ' CNY', 
                          ' COP		', 
                          ' CRC', 
                          ' HRK',
                          'CUP',
                          'CZK',  
                          ' DKK', 
                          ' DOP', 
                          ' XCD', 
                          ' EGP', 
                          ' SVC', 
                          ' EUR', 
                          ' FKP', 
                          ' FJD', 
                          ' GHS	', 
                          ' GIP', 
                          ' GTQ',
                          'GGP',  
                          ' GYD', 
                          ' HNL	', 
                          ' HKD', 
                          ' HUF', 
                          ' ISK', 
                          ' INR', 
                          ' IDR', 
                          ' IRR', 
                          ' IMP		', 
                          ' ILS', 
                          ' JMD',
                          'JPY',
                          'KZT',  
                          ' KPW', 
                          ' KRW', 
                          ' KGS', 
                          ' LAK', 
                          ' LBP', 
                          ' LRD', 
                          ' MKD', 
                          ' MYR', 
                          ' MUR	', 
                          ' MXN', 
                          ' MNT',
                          'MZN',  
                          ' NAD', 
                          ' NPR', 
                          ' ANG', 
                          ' NZD	', 
                          ' NIO	', 
                          ' NGN', 
                          ' NOK', 
                          ' OMR	', 
                          ' PKR	', 
                          ' PAB', 
                          ' PYG',
                          'PEN',
                          'PHP',  
                          ' PLN', 
                          ' QAR', 
                          ' RON', 
                          ' RUB', 
                          ' SHP', 
                          ' SAR', 
                          ' RSD', 
                          ' SCR	', 
                          ' SGD	', 
                          ' SBD', 
                          ' SOS',
                          'ZAR',  
                          ' LKR', 
                          ' SEK	', 
                          ' CHF', 
                          ' SRD', 
                          ' SYP', 
                          ' TWD', 
                          ' THB', 
                          ' TTD', 
                          ' TRY ', 
                          ' TVD', 
                          ' UAH',
                          'GBP	', 
                          ' UYU', 
                          ' UZS	', 
                          ' VEF ', 
                          ' VND', 
                          ' YER',
                          'ZWD',)
  
currencychoose2.place(x=300,y=80)
currencychoose2.current() 


text = Text(root,height=7,width=52,font=('verdana','10','bold'))
text.place(x=100,y=120)

B = Button(root,text="Search",cursor="hand2",command=show_data,font=('verdana','10','bold'),borderwidth=2,bg="red",fg="white")
B.place(x=20,y=120)

clear = Button(root,text="Clear",cursor="hand2",command=clear,font=('verdana','10','bold'),borderwidth=2,bg="blue",fg="white")
clear.place(x=20,y=170)

root.mainloop()